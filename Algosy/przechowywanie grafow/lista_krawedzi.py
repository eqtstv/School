import numpy as np

class ListOfEdges:
    def __init__(self):
        self.items = np.empty((0, 3), dtype=int)

    def return_list(self):
        return self.items

    def delete_vertex(self, v_index):
        #zwróć listę która nie ma wartości v_index w pierwszej kolumnie
        self.items = self.items[self.items[:, 0] != v_index, :]
        #zwróć listę która nie ma wartości v_index w drugiej kolumnie
        self.items = self.items[self.items[:, 1] != v_index, :]

    def add_edge(self, v_out, v_in, weight):
        #sprawdź czy krawędź już istnieje
        #utwórz krawędź testową
        test_edge = np.array([v_out, v_in])
        #bierz pod uwagę tylko dwie pierwsze kolumny macierzy
        test_matrix = self.items[:, :2]
        #zwróć czy w macierzy jest już podana krawędź (True/False)
        no_duplicate = np.all(np.any(test_matrix != test_edge, axis=1))
        #jeżeli nie ma dodaj ją, jeżei jest wyświetl komunikat
        if (no_duplicate == True):
            #dodaj nową krawędź na koniec listy
            new_edge = np.array([v_out, v_in, weight])
            self.items = np.vstack((self.items, new_edge))
        else:
            print('Podana krawedz juz istnieje' + str(test_edge))

    def delete_edge(self, v_out, v_in, weight):
        #utwórz krawędź do testowania
        test_edge = np.array([v_out, v_in, weight])
        #utwórz listę krawędzi typu bool gdzie False -> krawędź jest taka sama jak testowa
        bool_mask = np.any(self.items != test_edge, axis=1)
        #stwórz listę indeksów krawędzi które są różne od testowanej
        uniq_edge_list = np.where(bool_mask)
        #zwróć listę bez podanej krawędzi
        self.items = self.items[uniq_edge_list]


m = ListOfEdges()
m.add_edge(1, 3, 8)
m.add_edge(3, 4, 1)
m.add_edge(2, 5, 6)
m.add_edge(0, 0, 0)
m.add_edge(2, 4, 3)
m.add_edge(5, 4, 2)
m.add_edge(3, 3, 1)


print(m.return_list())

m.delete_vertex(3)

print(m.return_list())