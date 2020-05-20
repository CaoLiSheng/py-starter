# -*- coding: utf-8 -*-
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y1 = np.sin(x) + 1
y2 = np.cos(x ** 2) + 1

plt.figure(figsize=(8, 4))
plt.plot(x, y1, label='$sin x+1$', color='red', linewidth=2)
plt.plot(x, y2, 'b--', label='$cos x^2 + 1$')

plt.xlabel('Time(s) ')
plt.ylabel('Volt')
plt.title('A simple example')
plt.ylim(0, 2.2)
plt.legend()
plt.show()
