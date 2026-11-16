#!/usr/bin/env python3
"""Synthetic read-only inspector tests; these do not test Canva."""
from pathlib import Path
import tempfile
import unittest

from PIL import Image

from inspect_png import inspect_png


class InspectorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def save(self, name, mode="RGBA", color=(0, 0, 0, 0), size=(12, 20)):
        path = self.root / name
        image = Image.new(mode, size, color)
        if mode == "RGBA" and color[-1] == 0 and "blank" not in name:
            image.putpixel((5, 5), (255, 0, 0, 255))
        image.save(path)
        return path

    def inspect(self, path, **kwargs):
        return inspect_png(
            path, expected_width=12, expected_height=20,
            require_transparent=True, **kwargs
        )

    def test_valid_transparent_png(self):
        report = self.inspect(self.save("valid.png"))
        self.assertTrue(report["metadata_checks_passed"])
        self.assertEqual(len(report["sha256"]), 64)
        self.assertEqual(report["alpha"]["visible_pixel_count"], 1)

    def test_expected_delivery_hash_matches(self):
        path = self.save("matching.png")
        measured = self.inspect(path)
        report = self.inspect(path, expected_sha256=measured["sha256"])
        self.assertTrue(report["metadata_checks_passed"])
        self.assertEqual(report["size_bytes"], path.stat().st_size)

    def test_mismatched_delivery_hash_rejected(self):
        report = self.inspect(self.save("changed.png"), expected_sha256="0" * 64)
        self.assertFalse(report["metadata_checks_passed"])

    def test_opaque_rgb_rejected(self):
        report = self.inspect(self.save("rgb.png", "RGB", (255, 255, 255)))
        self.assertFalse(report["metadata_checks_passed"])

    def test_opaque_rgba_rejected(self):
        report = self.inspect(self.save("rgba.png", color=(255, 255, 255, 255)))
        self.assertFalse(report["metadata_checks_passed"])

    def test_blank_alpha_rejected(self):
        report = self.inspect(self.save("blank.png"))
        self.assertFalse(report["metadata_checks_passed"])

    def test_wrong_size_rejected(self):
        report = self.inspect(self.save("size.png", size=(13, 20)))
        self.assertFalse(report["metadata_checks_passed"])

    def test_non_png_rejected(self):
        report = self.inspect(self.save("format.jpg", "RGB", (255, 255, 255)))
        self.assertFalse(report["metadata_checks_passed"])
        self.assertIn("File is not PNG.", report["errors"])

    def test_enlarged_canvas_does_not_claim_native_detail(self):
        source = self.save("source.png", size=(6, 10))
        report = self.inspect(self.save("export.png"), source=source)
        self.assertTrue(report["metadata_checks_passed"])
        self.assertEqual(report["source"]["width"], 6)
        self.assertEqual(report["source"]["export_to_source_width_ratio"], 2.0)
        self.assertTrue(report["source"]["export_canvas_exceeds_source_on_an_axis"])
        self.assertTrue(any("does not add raster detail" in w for w in report["warnings"]))

    def test_opaque_glyph_probe_reports_actual_color(self):
        report = self.inspect(self.save("probe.png"), probes=[(5, 5)])
        self.assertEqual(report["pixel_samples"][0]["rgba"], [255, 0, 0, 255])
        self.assertTrue(report["metadata_checks_passed"])

    def test_transparent_probe_cannot_verify_fill(self):
        report = self.inspect(self.save("transparent_probe.png"), probes=[(0, 0)])
        self.assertEqual(report["pixel_samples"][0]["rgba"][3], 0)
        self.assertTrue(any("cannot alone establish" in w for w in report["warnings"]))

    def test_probe_outside_image_rejected(self):
        report = self.inspect(self.save("outside_probe.png"), probes=[(12, 0)])
        self.assertFalse(report["metadata_checks_passed"])

    def test_partial_alpha_warns(self):
        report = self.inspect(self.save("partial.png", color=(1, 2, 3, 128)))
        self.assertTrue(report["metadata_checks_passed"])
        self.assertTrue(any("no fully transparent pixels" in w for w in report["warnings"]))

    def test_transparent_pixels_do_not_prove_clean_background(self):
        path = self.save("patch.png", color=(255, 255, 255, 255))
        with Image.open(path) as image:
            image.putpixel((0, 0), (0, 0, 0, 0))
            image.save(path)
        report = self.inspect(path)
        self.assertTrue(report["metadata_checks_passed"])
        self.assertTrue(any("patches" in w for w in report["warnings"]))


if __name__ == "__main__":
    unittest.main()
