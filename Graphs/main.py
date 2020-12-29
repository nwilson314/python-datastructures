import pytest

from GraphList import UndirectedGraphList

def test_graph1_undirected_list():
    g = UndirectedGraphList()
    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(2, 6)
    g.add_edge(3, 2)
    g.add_edge(5, 8)
    g.add_edge(6, 5)
    g.add_edge(7, 5)
    g.add_edge(7, 5)
    return g


class TestUndirectedGraphList:
    def test_dfs1(self):
        g = test_graph1_undirected_list() 
        