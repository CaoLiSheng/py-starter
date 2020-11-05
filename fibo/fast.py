# -*- coding: utf-8 -*-
# coding=utf-8
import math


def FastRecFibo(n):
    if n == 0:
        return 1, 0
    if n == 1:
        return 0, 1

    m = math.floor(n / 2)
    hprv, hcur = FastRecFibo(m)         # (F(m-1),F(m))

    prev = hprv * hprv + hcur * hcur    # F(2m-1)
    curr = hcur * (hprv + hprv + hcur)  # F(2m)
    next = prev + curr                  # F(2m+1)

    if n % 2 == 0:
        return prev, curr
    else:
        return curr, next


for i in range(11):
    print(i, "th Fibo -> ", FastRecFibo(i)[1])
