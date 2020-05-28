#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 10, 100)
print(x1)
plt.plot(x1, 1/2-x1, (2+x1)/4)
