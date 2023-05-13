import sympy
import numpy as np
from sympy.geometry import Point3D
from lib import get_all_points, get_geodesics
import graphix
import json
import math


def draw_data():
    with open("reg_points.json", "r") as inp:
        data = json.load(inp)
    data = {float(k): v for k, v in data.items()}
    graphix.draw_geodesic_counts_func(data, 'The number of different lengths of geodesics', 'The number of different lengths of geodesics', draw=False, save_name='../regular_graphixes/default')
    graphix.draw_geodesic_counts_func(data, 'The number of different lengths of geodesics', 'Exponent indicator', lambda x: math.log(x), draw=False, save_name='../regular_graphixes/Exp')
    graphix.draw_geodesic_counts_func(data, 'The number of different lengths of geodesics', 'Sub-exponent indicator', lambda x: 1 if x == 1 else math.log(math.log(x))/math.log(x), draw=False, save_name='../regular_graphixes/sub-exp')


def count():
    A = Point3D(0, 0, 0)
    B = Point3D(1, 0, 0)
    C = Point3D(sympy.S(1) / 3, sympy.S(1) / 2, 0)
    D = Point3D(sympy.S(2) / 3, sympy.S(1) / 2, 1)

    count = 10
    max_r = 5.5
    start = 1
    for r in np.linspace(start, max_r, count):
        print(f'now {r}')
        points = get_all_points(A, B, C, D, r)
        # graphix.draw_points(points)
        all_geodesic = get_geodesics(points)
        # graphix.draw_geodesic(all_geodesic)
        with open("points.json", "r") as inp:
            old_data = json.load(inp)
        old_data[r] = len(all_geodesic)
        with open("points.json", "w") as out:
            json.dump(old_data, out, indent=2)
        # graphix.draw_geodesic_counts(old_data)
        print(f'done {r}')


def main():
    # draw_data()
    count()


if __name__ == '__main__':
    main()
