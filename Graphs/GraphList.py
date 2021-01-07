class UndirectedGraphList:
    '''
    Implementation of an undirected Graph using an adjacency list
    '''

    def __init__(self):
        self.adj_list = {} 

    def add_vertex(self, val):
        if val not in self.adj_list:
            self.adj_list[val] = set()

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.adj_list[vertex1].add(vertex2)
        self.adj_list[vertex2].add(vertex1)

    def get_vertex(self):
        '''
        Generator that returns the next vertex in the adjacency list
        '''
        for vertex in sorted(self.adj_list):
            yield vertex

    def get_neighbor(self, vertex):
        '''
        Generator that returns the next vertex adjacent to the given vertex
        '''
        if vertex in sorted(self.adj_list):
            for neighbor in sorted(self.adj_list[vertex]):
                yield neighbor

    def dfs_iterative(self):
        '''
        Returns the parents of each node as determined by DFS.
        '''
        parents = {}
        visit_stack = []

        for vertex in self.get_vertex():

            visit_stack.append(vertex)

            while visit_stack:
                v = visit_stack.pop()

                for neighbor in self.get_neighbor(v):
                    if neighbor not in parents:
                        parents[neighbor] = v
                        visit_stack.append(neighbor)
        return parents

    def dfs_recursive(self):
        '''
        Returns the parents of each node as determined by DFS.
        '''

        parents = {}

        for vertex in self.get_vertex():
            if vertex not in parents:
                self._dfs_util(vertex, parents)

        return parents

    def _dfs_util(self, vertex, parents):
        for neighbor in self.get_neighbor(vertex):
            if neighbor not in parents:
                parents[neighbor] = vertex
                self._dfs_util(neighbor, parents)

        
