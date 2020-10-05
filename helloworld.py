# -*- coding: utf-8 -*-
# coding=utf-8
import queue
import math

print("'hello，世界!'")

Pop = [6, 6, 9, 12, 5]
per = 3


class PP:
    p = 0
    i = 0

    def __init__(self, p, i):
        self.p = p
        self.i = i

    def __lt__(self, other):
        return self.p > other.p

    def __eq__(self, other):
        return self.p == other.p


def ApportionCongress(R):
    Rep = []
    PQ = queue.PriorityQueue(len(Pop))

    for s in range(len(Pop)):
        Rep.append(1)
        PQ.put(PP(Pop[s]/math.sqrt(2), s))

    for _ in range(R - len(Pop)):
        pp = PQ.get()
        print(pp.i, pp.p)
        Rep[pp.i] = Rep[pp.i] + 1
        p = Pop[pp.i]/math.sqrt(Rep[pp.i] * (Rep[pp.i] + 1))
        print(p)
        PQ.put(PP(p, pp.i))

    return Rep


# print(ApportionCongress(3))


def HHGuess(D):
    reps = 0
    Rep = []

    for s in range(len(Pop)):
        q = Pop[s]/D
        if q * q < math.floor(q) * math.ceil(q):
            Rep.append(math.floor(q))
        else:
            Rep.append(math.ceil(q))
        reps += Rep[s]

    return (reps, Rep)


ret = HHGuess(per)
print(ret[1], ApportionCongress(ret[0]))
