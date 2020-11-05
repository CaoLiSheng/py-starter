# -*- coding: utf-8 -*-
# coding=utf-8

def FastLIS(arr):
    arr.insert(0, float("-inf"))
    # print(arr)

    arrLen = len(arr)
    LISBigger = []
    for i in range(arrLen):
        tmp = []
        for j in range(arrLen + 1):
            tmp.append(0)
        LISBigger.append(tmp)
    # print(LISBigger)

    j = arrLen
    while j >= 0:
        j -= 1
        for i in range(j):
            skip = LISBigger[i][j+1]
            take = LISBigger[j][j+1] + 1
            if arr[i] >= arr[j]:
                LISBigger[i][j] = skip
            else:
                LISBigger[i][j] = max(skip, take)
    # print(LISBigger)
    return LISBigger[0][1]


def FastLIS2(arr):
    arr.insert(0, float("-inf"))

    arrLen = len(arr)
    LISBigger = []
    for i in range(arrLen):
        LISBigger.append(0)

    j = arrLen
    while j >= 0:
        j -= 1
        for i in range(j):
            skip = LISBigger[i]
            take = LISBigger[j] + 1
            if arr[j] > arr[i] and take > skip:
                LISBigger[i] = take
    return LISBigger[0]


print(FastLIS([2, 1, 3, 1, 3, 4]))
print(FastLIS2([2, 1, 3, 1, 3, 4]))
