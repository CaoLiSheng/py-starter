# -*- coding: utf-8 -*-
# coding=utf-8
import queue
import math

Pop = [60, 60, 60, 60, 80]
per = 30


class PQStruct:
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
        PQ.put(PQStruct(Pop[s]/math.sqrt(2), s))

    for _ in range(R - len(Pop)):
        pp = PQ.get()
        Rep[pp.i] = Rep[pp.i] + 1
        p = Pop[pp.i]/math.sqrt(Rep[pp.i] * (Rep[pp.i] + 1))
        print(pp.i, Rep[pp.i], "{:10.3f}".format(pp.p), "{:10.3f}".format(p))
        PQ.put(PQStruct(p, pp.i))

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
