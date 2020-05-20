class Node:
    def __init__(self, name=None, color="white", successors=None):
        self.name = name
        self.color = color
        self.successors = successors


def top_order(G):
    def recurse(n):
        if n in S:
            return False
        S.append(n)

        res.append(n.name)
        for u in n.successors:
            if not(recurse(u)):
                return False
        return True

    for n in G:
        S, res = [], []
        if not(recurse(n)):
            return [-1]
        if len(S) == len(G):
            return res
    return [-1]


n = Node("Quelle")
m = Node("Senke")
n.successors = [m]
m.successors = []
print(top_order([m, n]))
print(top_order([n, m]))
m.successors = [n]
print(top_order([m, n]))
print(top_order([n, m]))
