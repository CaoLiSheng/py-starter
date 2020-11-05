# -*- coding: utf-8 -*-
# coding=utf-8

# import numpy as np
from matplotlib import pyplot as plt

# x = np.linspace(0, 10, 1000)
# y1 = np.sin(x) + 1
# y2 = np.cos(x ** 2) + 1
x = [
    '2020-02-02 12:00:00',
    '2020-02-02 12:00:01',
    '2020-02-02 12:00:02',
    '2020-02-02 12:00:03',
    '2020-02-02 12:00:04',
    '2020-02-02 12:00:05'
]
y1 = [11, 12, 13, 14, 15, 10]

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='y1')
# plt.plot(x, y1, label='$sin x+1$', color='red', linewidth=2)
# plt.plot(x, y2, 'b--', label='$cos x^2 + 1$')

plt.xticks(x, x, rotation=20)
plt.xlabel('Timestamp ')
plt.ylabel('Packages')
plt.title('A simple example')
plt.ylim(0, 20)
plt.legend()
plt.show()
# plt.savefig('foo.png')
