"""
Возможно ли провести вертикальную ось симметрии?

Точки, лежащие на оси симметрии, симметричны сами себе.


is_vert_sym([(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0), (4, 0)]) # True, axis_x = 2
is_vert_sym([(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0)]) # False
is_vert_sym([]) # True
is_vert_sym([(0, 0)]) # True, axis_x = 0
is_vert_sym([(0, 0), (10, 0)]) # True, axis_x = 5
is_vert_sym([(0, 0), (0, 5), (10, 5), (10, 0)]) # True, axis_x = 5

is_vert_sym([(0, 0), (11, 1)]) # False
is_vert_sym([(0, 0), (1, 0), (3, 0)]) # False, axis_x = 1.5
"""
from collections import defaultdict


def is_vert_sym(points: list[tuple[int]]) -> bool:
    if len(points) == 0:
        return True
    # code
    max_x, min_x = None, None
    mapa = defaultdict(int)

    for x, y in points:
        if (max_x, min_x) == (None, None):
            max_x, min_x = x, x
        else:
            if max_x < x:
                max_x = x
            if min_x > x:
                min_x = x
        mapa[(x, y)] += 1

    if max_x + min_x == 0:
        axis_x = 0
    else:
        axis_x = (max_x + min_x) / 2

    while len(mapa) > 0:
        (x, y), count = next(iter(mapa.items()))
        new_x = x - (x- axis_x) * 2

        if new_x == x:
            del mapa[(x,y)]
        elif mapa.get((new_x, y)):
            if mapa[(x, y)] != mapa[(new_x,y)]:
                return False, axis_x
            del mapa[(x,y)]
            del mapa[(new_x, y)]
        else:
            return False, axis_x
    return True, axis_x
