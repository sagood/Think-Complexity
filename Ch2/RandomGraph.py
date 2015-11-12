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


def main(script, n=10, p=0.2, *args):
    n = int(n)
    p = float(p)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = RandomGraph(vs)
    g.add_random_edges(p)
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()


if __name__ == '__main__':
    import sys

    main(*sys.argv)
