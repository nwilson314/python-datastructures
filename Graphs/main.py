import pytest

from GraphList import UndirectedGraphList

def test_graph1_undirected_list():
    udg = UndirectedGraphList()
    udg.add_edge(0, 1)
    udg.add_edge(1, 2)
    udg.add_edge(2, 3)
    udg.add_edge(1, 7)
    udg.add_edge(3, 7)
    udg.add_edge(7, 8)
    udg.add_edge(3, 4)
    udg.add_edge(3, 5)
    udg.add_edge(4, 5)
    udg.add_edge(5, 6)
    udg.add_edge(6, 7)
    udg.add_edge(6, 8)

    return udg


class TestUndirectedGraphList:
    def test_dfs_iterative(self):
        g = test_graph1_undirected_list() 
        parents = g.dfs_iterative()

        assert parents == {0: 1, 1: 0, 2: 1, 3: 7, 4: 5, 5: 6, 6: 7, 7: 1, 8: 7}

    def test_dfs_recursive(self):
        g = test_graph1_undirected_list() 
        parents = g.dfs_recursive()

        assert parents == {0: 1, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7}
