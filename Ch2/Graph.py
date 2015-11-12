from queue import Queue


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

    def add_regular_edges(self, d=2):
        # see reference:  https://en.wikipedia.org/wiki/Regular_graph
        vs = self.vertices()
        if d >= len(vs):
            raise (ValueError, "cannot build a regular graph.")

        if d % 2 == 0:
            self.add_regular_edges_even(d)
        else:
            if len(vs) % 2 != 0:
                raise (ValueError, "cannot build a regular graph.")
            self.add_regular_edges_even(d - 1)
            self.add_regular_edges_odd()

    def add_regular_edges_even(self, d=2):
        vs = self.vertices()
        vs2 = list(vs) * 2
        for i, v in enumerate(vs):
            for j in range(1, d // 2 + 1):
                w = vs2[i + j]
                self.add_edge(Edge(v, w))

    def add_regular_edges_odd(self):
        vs = self.vertices()
        n = len(vs)
        vs2 = list(vs) * 2
        for i in range(n // 2):
            v = vs2[i]
            w = vs2[i + n // 2]
            self.add_edge(Edge(v, w))

    def is_connected(self):
        self.bfs()
        for v in self.vertices():
            if not v.visited:
                return False
        return True

    def bfs(self):
        for v in self.vertices():
            v.visited = False
        q = Queue()
        start_node = list(self.vertices())[0]
        q.put(start_node)
        start_node.visited = True

        while not q.empty():
            u = q.get()
            for v in self[u].keys():
                if not v.visited:
                    q.put(v)
                    v.visited = True


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

    """ test is_connected """
    print(g.is_connected())

if __name__ == '__main__':
    import sys

    main(*sys.argv)
