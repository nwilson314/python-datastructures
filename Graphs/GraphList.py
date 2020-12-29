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
        for vertex in self.adj_list:
            yield vertex

    def get_neighbor(self, vertex):
        '''
        Generator that returns the next vertex adjacent to the given vertex
        '''
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                yield neighbor
        
