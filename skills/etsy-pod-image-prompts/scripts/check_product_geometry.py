"""Conservative 2D screen for supplied front-face corner anchors; never physical proof."""
import argparse
import json
import math
from pathlib import Path


def screen(record):
    base = {'status': 'HOLD', 'physical_ratio_verified': False,
            'scope': '2D supplied-anchor screen only; visual/source/owner gates remain separate'}
    def hold(reason):
        return {**base, 'reason': reason}
    try:
        w, h = float(record['physical_width']), float(record['physical_height'])
        iw, ih = map(float, record['image_size_px'])
        tol = float(record['relative_tolerance'])
        uncertainty = float(record['relative_corner_uncertainty'])
        p = [tuple(map(float, q)) for q in record['corners_TL_TR_BR_BL']]
    except (KeyError, TypeError, ValueError):
        return hold('Missing or invalid measurements')
    values = [w, h, iw, ih, tol, uncertainty] + [c for q in p for c in q]
    if not all(math.isfinite(v) for v in values):
        return hold('Non-finite measurement')
    if min(w, h, iw, ih) <= 0 or not 0 < tol < 1 or not 0 <= uncertainty <= tol:
        return hold('Invalid dimensions/tolerance or uncertainty exceeds tolerance')
    source = str(record.get('physical_dimension_source', '')).strip()
    if not source or not record.get('tolerance_rationale'):
        return hold('Source and tolerance rationale required')
    if record.get('dimension_source_review') != 'verified' or source.casefold() in {'tbc', 'unknown', 'unverified', 'missing', 'none', 'n/a'}:
        return hold('Physical dimension source is unverified/TBC')
    if record.get('front_face_view_review') != 'near_frontal_confirmed':
        return hold('Near-frontal view not independently reviewed')
    if len(p) != 4 or any(len(q) != 2 for q in p):
        return hold('Exactly four 2D corners required')
    if any(not (0 <= x < iw and 0 <= y < ih) for x, y in p):
        return hold('Corner outside native image bounds')
    v = [(p[(i+1)%4][0]-p[i][0], p[(i+1)%4][1]-p[i][1]) for i in range(4)]
    edges = [math.hypot(x, y) for x, y in v]
    if min(edges) < 1:
        return hold('Degenerate edges')
    cross = [v[i][0]*v[(i+1)%4][1]-v[i][1]*v[(i+1)%4][0] for i in range(4)]
    if not (all(c > 0 for c in cross) or all(c < 0 for c in cross)):
        return hold('Non-convex, unordered or degenerate corners')
    asymmetry = max(abs(edges[0]-edges[2])/((edges[0]+edges[2])/2),
                    abs(edges[1]-edges[3])/((edges[1]+edges[3])/2))
    right_angle_error = max(abs(math.degrees(math.acos(max(-1, min(1,
                            (v[i][0]*v[(i+1)%4][0]+v[i][1]*v[(i+1)%4][1]) /
                            (edges[i]*edges[(i+1)%4])))))-90) for i in range(4))
    if asymmetry > 0.05 or right_angle_error > 5:
        return hold('Perspective/skew prevents this near-frontal screen')
    measured = (edges[0]+edges[2])/(edges[1]+edges[3])
    target = w/h
    error = measured/target - 1
    # Conservative uncertainty interval must fit inside the chosen tolerance.
    passed = abs(error) + uncertainty <= tol
    return {**base, 'status': 'SCREEN_PASS' if passed else 'REVISE',
            'target_width_height_ratio': target, 'measured_width_height_ratio': measured,
            'relative_error': error, 'relative_corner_uncertainty': uncertainty,
            'relative_tolerance': tol, 'opposing_edge_asymmetry': asymmetry,
            'max_right_angle_deviation_deg': right_angle_error,
            'reason': 'Supplied-anchor consistency within tolerance' if passed else 'Ratio/uncertainty outside tolerance'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    args = parser.parse_args()
    record = json.loads(args.record.read_text(encoding='utf-8'))
    result = screen(record)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'SCREEN_PASS' else 2


if __name__ == '__main__':
    raise SystemExit(main())
