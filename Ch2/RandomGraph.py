import string
from random import random

from Ch2.Graph import *
from Ch2.GraphWorld import CircleLayout, GraphWorld


class RandomGraph(Graph):
    def add_random_edges(self, p):
        vs = self.vertices()
        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if i >= j: continue
                if random() > p: continue
                self.add_edge(Edge(v, w))
                self.add_edge(Edge(w, v))


def show_graph(g):
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()


def test_graph(n, p):
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]
    g = RandomGraph(vs)
    g.add_random_edges(p)
    return g.is_connected()


def test_p(n, p0, iteration):
    p = p0
    while p <= 1.0:
        count = 0
        for i in range(iteration):
            if test_graph(n, p):
                count += 1

        print('p = {0:.2f}: {1:.2f}'.format(p, count / iteration))
        p += 0.05


def main(script, n=20, p=0.1, *args):
    n = int(n)
    p = float(p)
    # ex 2-6
    test_p(n, p, 1000)


if __name__ == '__main__':
    import sys

    main(*sys.argv)
