class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError('Edges must connect exactly two vertices.')
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.

    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, u, v):
        try:
            e = self[u][v]
            return e
        except KeyError:
            return None

    def remove_edge(self, e):
        v, w = e
        del self[v][w]
        del self[w][v]

    def vertices(self):
        return self.keys()

    def edges(self):
        es = set()
        for d in self.values():
            es.update(d.values())
        return es

    def out_vertices(self, v):
        return self[v].keys()

    def out_edges(self, v):
        return self[v].values()

    def add_all_edges(self):
        vs = self.vertices()

        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if i != j:
                    self.add_edge(Edge(v, w))


def main(script, *args):
    v = Vertex('v')
    print(v)
    w = Vertex('w')
    print(w)
    e = Edge(v, w)
    print(e)
    g = Graph([v, w], [e])
    print(g)

    """ test get_edge """
    e = g.get_edge(v, w)
    print(e)

    """ test remove_edge """
    g.remove_edge(e)
    print(g)

    u = Vertex('u')
    g.add_vertex(u)
    g.add_edge(Edge(u, v))
    g.add_edge(Edge(u, w))

    """ test vertices """
    vs = g.vertices()
    print(vs)

    """ test edges """
    es = g.edges()
    print(es)

    """ test out_vertices """
    out_vs = g.out_vertices(u)
    print(out_vs)

    """ test out_edges """
    out_es = g.out_edges(u)
    print(out_es)

    """ test add_all_edges """
    g.add_all_edges()
    print(g)

if __name__ == '__main__':
    import sys

    main(*sys.argv)
