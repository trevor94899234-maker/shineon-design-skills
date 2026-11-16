#!/usr/bin/env python3
"""Read-only PNG dimension/alpha/hash inspection. Requires Pillow; does not edit pixels."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

from PIL import Image


def file_sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inspect_png(path, expected_width=None, expected_height=None,
                require_transparent=False, source=None, probes=None, expected_sha256=None):
    path = Path(path)
    report = {
        "file": str(path),
        "scope": "File metadata and alpha only; not fidelity, editability, or print approval.",
        "errors": [],
        "warnings": [],
    }
    with Image.open(path) as image:
        report.update({
            "format": image.format,
            "mode": image.mode,
            "width": image.width,
            "height": image.height,
        })
        if image.format != "PNG":
            report["errors"].append("File is not PNG.")
        if expected_width is not None and image.width != expected_width:
            report["errors"].append("Width does not match the requested export.")
        if expected_height is not None and image.height != expected_height:
            report["errors"].append("Height does not match the requested export.")
        image.load()
        rgba = image.convert("RGBA")
        alpha = rgba.getchannel("A")
        hist = alpha.histogram()
        pixels = image.width * image.height
        visible = pixels - hist[0]
        report["alpha"] = {
            "minimum": alpha.getextrema()[0],
            "maximum": alpha.getextrema()[1],
            "fully_transparent_fraction": hist[0] / pixels,
            "partially_transparent_fraction": sum(hist[1:255]) / pixels,
            "fully_opaque_fraction": hist[255] / pixels,
            "nonopaque_fraction": (pixels - hist[255]) / pixels,
            "visible_pixel_count": visible,
            "visible_bbox": alpha.getbbox(),
            "corner_values": [
                alpha.getpixel((0, 0)),
                alpha.getpixel((image.width - 1, 0)),
                alpha.getpixel((0, image.height - 1)),
                alpha.getpixel((image.width - 1, image.height - 1)),
            ],
        }
        if probes:
            report["pixel_samples"] = []
            for x, y in probes:
                if not (0 <= x < image.width and 0 <= y < image.height):
                    report["errors"].append(f"Pixel probe ({x}, {y}) is outside the image.")
                    continue
                value = list(rgba.getpixel((x, y)))
                report["pixel_samples"].append({"x": x, "y": y, "rgba": value})
                if value[3] != 255:
                    report["warnings"].append(
                        f"Probe ({x}, {y}) is not fully opaque; it cannot alone establish the text fill color."
                    )
        if visible == 0:
            report["errors"].append("PNG is fully transparent and contains no visible artwork.")
        if require_transparent and hist[255] == pixels:
            report["errors"].append("PNG is fully opaque; usable transparency is absent.")
        if require_transparent and hist[0] == 0 and hist[255] != pixels:
            report["warnings"].append(
                "Only partial alpha found, with no fully transparent pixels; visually inspect the background."
            )
        if image.info.get("dpi"):
            report["dpi_metadata"] = list(image.info["dpi"])
            report["warnings"].append(
                "DPI metadata does not establish physical size or source detail."
            )
    report["sha256"] = file_sha256(path)
    report["size_bytes"] = path.stat().st_size
    if expected_sha256 is not None and report["sha256"] != expected_sha256.lower():
        report["errors"].append("File hash differs from the expected original export bytes.")
    if source is not None:
        source = Path(source)
        with Image.open(source) as original:
            sw, sh = original.size
            report["source"] = {
                "file": str(source),
                "width": sw,
                "height": sh,
                "sha256": file_sha256(source),
                "size_bytes": source.stat().st_size,
                "export_to_source_width_ratio": report["width"] / sw,
                "export_to_source_height_ratio": report["height"] / sh,
                "export_canvas_exceeds_source_on_an_axis": (
                    report["width"] > sw or report["height"] > sh
                ),
                "aspect_ratio_relative_difference": abs(
                    (report["width"] / report["height"]) / (sw / sh) - 1
                ),
            }
        if report["source"]["export_canvas_exceeds_source_on_an_axis"]:
            report["warnings"].append(
                "Export canvas exceeds source dimensions. This does not add raster detail; "
                "inspect actual placement to determine artwork resampling."
            )
    report["warnings"].append(
        "Visually inspect light/dark proofs for patches, haze, ghosts, and art drift. "
        "Verify independent editable text in Canva separately."
    )
    report["metadata_checks_passed"] = not report["errors"]
    return report


def parse_probe(value):
    try:
        x, y = (int(part) for part in value.split(","))
        if x < 0 or y < 0:
            raise ValueError
        return x, y
    except ValueError:
        raise argparse.ArgumentTypeError("Use a nonnegative pixel coordinate pair X,Y.")


def parse_sha256(value):
    lowered = value.lower()
    if len(lowered) != 64 or any(c not in "0123456789abcdef" for c in lowered):
        raise argparse.ArgumentTypeError("Expected SHA-256 must have 64 hexadecimal characters.")
    return lowered


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--expected-width", type=int)
    parser.add_argument("--expected-height", type=int)
    parser.add_argument("--require-transparent", action="store_true")
    parser.add_argument("--source", type=Path)
    parser.add_argument("--probe", type=parse_probe, action="append", default=[],
                        help="Read an observed glyph-interior pixel X,Y; repeat as needed.")
    parser.add_argument("--expected-sha256", type=parse_sha256,
                        help="Verify delivery bytes against a measured original export hash.")
    args = parser.parse_args()
    for value in (args.expected_width, args.expected_height):
        if value is not None and value <= 0:
            parser.error("Expected dimensions must be positive.")
    try:
        report = inspect_png(
            args.path, args.expected_width, args.expected_height,
            args.require_transparent, args.source, args.probe, args.expected_sha256
        )
    except (OSError, ValueError, Image.DecompressionBombError) as error:
        print(json.dumps({
            "metadata_checks_passed": False,
            "file": str(args.path),
            "errors": [str(error)],
        }, indent=2))
        return 2
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["metadata_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
