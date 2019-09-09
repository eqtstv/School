import pickle

with open ('C:/my_pc/Code/moje/Algosy/kolorowanie grafow/queen6x6.pickle', 'rb') as fp:
    edges = pickle.load(fp)


edges1 = [
         [1, 2],
         [1, 4],
         [2, 3],
         [2, 4],
         [2, 5],
         [3, 6],
         [4, 5],
         [4, 6],
         [5, 6],
         ]

def check_neighbours(graph, vertice):
    neighbours = []

    for edge in graph:
        if (vertice in edge):
            v_index = edge.index(vertice)
            if (v_index == 0):
                neighbours.append(edge[1])
            else:
                neighbours.append(edge[0])
    
    return neighbours



def color_graph(graph):

    v_quan = max(max(graph))

    vertices = list(range(1, v_quan+1))
    colors = list(range(0, v_quan))
    v_colors = [None] * v_quan

    v_colors[0] = colors[0]

    for vertice in vertices:
        free_colors = list(range(0, v_quan))
        neighbours = check_neighbours(graph, vertice)

        for neighbour in neighbours:
            neighbour_color = v_colors[neighbour-1]

            if (neighbour_color != None and neighbour_color in free_colors):
                free_colors.remove(neighbour_color)

            v_colors[vertice-1] = min(free_colors)

    return v_colors, max(v_colors)




print(color_graph(edges))