import numpy as np

class Edge:
    def __init__(self, v_out, v_in, weight):
        self.v_out = v_out
        self.v_in = v_in
        self.weight = weight

    def return_info(self):
        info_list = np.array([self.v_out, self.v_in, self.weight])
        return info_list

class Vertex:
    def __init__(self, v_index):
        self.v_index = v_index
        self.neighbor_edges = np.array([])

    def return_index(self):
        return self.v_index

    def return_edges(self):
        return self.neighbor_edges

    def return_neighbor_edges(self):
        #stwórz listę do przechowywania danych o krawędziach
        neighbor_edges = np.empty((0, 3), dtype=int)
        #wyodrębnij dane o każdej krawędzi
        for i in self.neighbor_edges:
            neighbor_edges = np.vstack((neighbor_edges, Edge.return_info(i)))
        return neighbor_edges

    def add_edge(self, v_in, weight):
        self.neighbor_edges = np.append(self.neighbor_edges, Edge(self.v_index, v_in, weight))

    def delete_edge(self, v_in, weight):
        #utwórz krawędź do testowania
        test_edge = np.array([v_in, weight])
        #wyodrębnij informacjie o każdej krawędzi
        test_matrix = np.empty((0, 2), dtype=int)
        for i in self.neighbor_edges:
            v_in_out = np.array([Edge.return_info(i)[1], Edge.return_info(i)[2]])
            test_matrix = np.vstack((test_matrix, v_in_out))
        #utwórz listę krawędzi typu bool gdzie False -> krawędź jest taka sama jak testowa
        bool_mask = np.any(test_matrix != test_edge, axis=1)
        #stwórz listę indeksów krawędzi które są różne od testowanej
        uniq_edge_list = np.where(bool_mask)
        #zwróć listę bez podanej krawędzi
        self.neighbor_edges = self.neighbor_edges[uniq_edge_list]

    def clear_neighbors(self):
        self.neighbor_edges = np.array([])

class Graph:
    def __init__(self):
        self.vertices = np.array([])
        self.edges = np.array([])

    def return_vertex(self, v_index):
        #zwróć wierzchołek (obiekt)
        return self.vertices[v_index - 1]

    def return_neighbor_edges(self, v_index):
        return Vertex.return_neighbor_edges(self.vertices[v_index - 1])

    def return_vertices_list(self):
        vertices = np.array([], dtype=int)
        for i in self.vertices:
            vertices = np.append(vertices, Vertex.return_index(i))
        return vertices

    def return_edges_list(self):
        edges = np.empty((0, 3), dtype=int)
        for i in self.edges:
            edges = np.vstack((edges, Edge.return_info(i)))
        return edges

    def add_vertex(self):
        #stwórz nowy wierzchołek (następny w kolei)
        new_vertex = Vertex(len(self.vertices) + 1)
        self.vertices = np.append(self.vertices, new_vertex)
        return new_vertex

    def delete_vertex(self, v_index):
        #usuwanie wierzchołka z listy
        self.vertices = np.delete(self.vertices, v_index - 1)

        #usuwanie krawędzi wychodziących z wierzchołka
        #przypisz wierzchołek
        outgoing_v = self.return_vertex(v_index)
        #wyczyść krawędzie wychodzące
        outgoing_v.clear_neighbors()

        #usuwanie krawędzi połączonych z usuwanym wierzchołkiem
        for i in self.edges:
            #wyodrębnij informacje o krawędzi
            v_out = Edge.return_info(i)[0]
            v_in = Edge.return_info(i)[1]
            #sprawdź indeks danej krawędzi
            edge_index = np.argwhere(self.edges == i)
            #jeżeli krawędź jest z lub do usuwanego wierzchołka - usuń ją
            if(v_out == v_index or v_in == v_index):
                self.edges = np.delete(self.edges, edge_index)

        #usuwanie krawędzi przychodzących do usuwanego wierzchołka
        #iteruj po wierzchołkach
        for i in self.vertices:
            #przypisz krawędzie i-tego wierzchołka
            edges = Vertex.return_edges(i)
            #iteruj po krawędziach
            for j in edges:
                #wyodrębnij v_in j-tej krawędzi
                v_in = Edge.return_info(j)[1]
                #sprawdź indeks danej krawędzi
                edge_index = np.argwhere(edges == j)
                #jeżeli krawędź prowadzi do usuwanego wierzchołka - usuń ją
                if(v_in == v_index):
                    i.neighbor_edges = np.delete(i.neighbor_edges, edge_index)
                    
        print('Poprawnie usunieto wierzcholek: ' + str(v_index) + '\n')

    def add_edge(self, v_out, v_in, weight):
        #sprawdź czy istnieją podane wierzchołki
        #przpisz wszystkie wierzchołki do listy
        vertices = self.return_vertices_list()
        #zwróć true jeżeli wierzchołki v_out i v_in istnieją
        vertices_exist = (v_out in vertices and v_in in vertices)

        #sprawdź czy nie ma już takiej krawędzi
        #stwórz krawędź testową
        test_edge = np.array([v_out, v_in])
        #wyodrębnij v_out i v_in z każdej krawędzi
        test_matrix = np.empty((0, 2), dtype=int)
        for i in self.edges:
            v_in_out = np.array([Edge.return_info(i)[0], Edge.return_info(i)[1]])
            test_matrix = np.vstack((test_matrix, v_in_out))
        #zwróć true jeżeli nie ma takiej krawędzi (v_out, v_in)
        no_edge_duplicate = np.all(np.any(test_matrix != test_edge, axis=1))
        #jeżeli nie ma duplikatu krawędzi i podane wierzchołki istnieją dodaj krawędź
        if (no_edge_duplicate == True and vertices_exist == True):
            #stwórz nową krawędź do dodania
            new_edge = Edge(v_out, v_in, weight)
            #dodaj krawędź do listy krawędzi
            self.edges = np.append(self.edges, new_edge)
            #zwróć wierzchołek do którego dodaje krawędź sąsiadującą
            outgoing_v = self.return_vertex(v_out)
            #dodaj krawędź sąsiadującą do danego wierzchołka
            outgoing_v.add_edge(v_in, weight)

            print('Dodano krawedz: ' +str(v_out) + ' ' + str(v_in) + ' ' + str(weight) +'\n')
        else:
            print('Nie mozna dodac: ' +str(v_out) + ' ' + str(v_in) + ' ' + str(weight))
            print('Sprawdz wprowadzone dane \n')

    def delete_edge(self, v_out, v_in, weight):
        #usuń krawędź z lity
        #utwórz krawędź do testowania
        test_edge = np.array([v_out, v_in, weight])
        #wyodrębnij informacjie o każdej krawędzi
        test_matrix = np.empty((0, 3), dtype=int)
        for i in self.edges:
            v_in_out = np.array([Edge.return_info(i)[0], Edge.return_info(i)[1], Edge.return_info(i)[2]])
            test_matrix = np.vstack((test_matrix, v_in_out))
        #utwórz listę krawędzi typu bool gdzie False -> krawędź jest taka sama jak testowa
        bool_mask = np.any(test_matrix != test_edge, axis=1)
        #stwórz listę indeksów krawędzi które są różne od testowanej
        uniq_edge_list = np.where(bool_mask)
        #zwróć listę bez podanej krawędzi
        self.edges = self.edges[uniq_edge_list]

        #usuń krawędź z listy sąsiadów wierzchołka
        #zwróć wierzchołek z którego usuwasz krawędź
        outgoing_v = self.return_vertex(v_out)
        #usuń krawędź sąsiadującą wierzchołka
        outgoing_v.delete_edge(v_in, weight)

        #wyświetl komunikaty 
        if(np.all(bool_mask) == True):
            print('Podana krawedz nie istnieje: ' +str(v_out) + ' ' + str(v_in) + ' ' + str(weight) +'\n')
        else:
            print('Poprawnie usunieto: ' +str(v_out) + ' ' + str(v_in) + ' ' + str(weight) +'\n')



vers = Graph()

vers.add_vertex()
vers.add_vertex()
vers.add_vertex()
vers.add_vertex()
vers.add_vertex()
vers.add_vertex()

vers.add_edge(1, 2, 6)
vers.add_edge(2, 3, 5)
vers.add_edge(1, 4, 8)
vers.add_edge(2, 6, 5)

print(vers.return_neighbor_edges(1))
print(vers.return_neighbor_edges(2))
vers.delete_vertex(2)

print(vers.return_neighbor_edges(1))
print(vers.return_neighbor_edges(2))


print(vers.return_vertices_list())
print(vers.return_edges_list())
