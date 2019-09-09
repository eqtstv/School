import pickle
import itertools


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


def graph_check(graph, colors):
    for edge in graph:
        if (colors[edge[0]-1] == colors[edge[1]-1]):
            return False
    return True

def make_colors(base, v_quan):
    colors = []
    base = list(range(0, base))
    for i in itertools.product(base,repeat=v_quan):
        colors.append(i)

    return colors



def color_graph_precise(graph):
    base = 2
    v_quan = max(max(graph))
    colors = []

    for base in range(v_quan):
        colors = make_colors(7, v_quan)
        for colored_graph in colors:
            if (graph_check(graph, colored_graph) == True):
                return colored_graph, max(colored_graph)

    return False       



print('Graph colors: ' + str(color_graph_precise(edges1)[0]))
print('Min q of colors: ' + str(color_graph_precise(edges1)[1]))