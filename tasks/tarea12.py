#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# 1.
points = (
    [(0,0), (4,2)], 
    [(7,2), (9, -4)], 
    [(19, 0), (15, 4)],
    [(22, -2), (22,4)],
    [(29, 1), (25, 1)],
    [(34, 2), (31, -3)],
    [(32, -6), (25, -9)],
    [(17, -7), (21, -7)],
    [(13, -10), (15, -5)],
    [(4, -6), (10, -9)],
    [(1, -6), (1, -9)]
)

for i, points_pair in enumerate(points, 1):
    print(f'Vector {i}')
    a, b = points_pair
    AB = np.array(b) - np.array(a)
    x, y = AB
    print(f'Componentes: {AB}')
    print("Módulo: {}".format(np.linalg.norm(AB)))
    print("Dirección: {}".format(np.degrees(np.arctan2(y, x))))
