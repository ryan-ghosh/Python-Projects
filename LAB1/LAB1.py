from lab1_utilities import *

def get_installations_from_file(file_name):
    open_file = open(file_name, 'r')
    read = open_file.readlines()
    installations = []
    x = []
    for i in read:
        x.append(i.strip().split("\t"))
    x = x[1:]
    for i in x:
        if i[15] == 'INDOORS':
            door = True
        if i[15] == "OUTDOORS":
            door = False
        installations.append(Installation(i[0], int(i[2]), (float(i[7]), float(i[8])), door))

    return installations


def euclidean_distance(position1, position2):
    x = position2[0] - position1[0]
    y = position2[1] - position1[1]
    s = (x**2 + y**2)**0.5
    return s


def get_adjacency_mtx(installations):
    outer_matrix = []
    inner_matrix = []
    for i in range(len(installations)):
        for j in range(len(installations)):
            inner_matrix.append(0.0)
        outer_matrix.append(inner_matrix)
        inner_matrix = []
    for i in range(len(installations)):
        for j in range(len(installations)):
            ward1 = int(installations[i].ward)
            ward2 = int(installations[j].ward)
            position1 = installations[i].position
            position2 = installations[j].position
            if not installations[i].indoor and not installations[j].indoor:
                k = 1.0
            else:
                k = 1.5
            if abs(ward1 - ward2) <= 1:
                s = euclidean_distance(position1, position2)
                outer_matrix[i][j] = k*s
    return outer_matrix


def make_graph(installations):
    graph = []
    for i in installations:
        graph.append(i.name)
    return Graph(graph, get_adjacency_mtx(installations))



def find_shortest_path(installation_A, installation_B, graph):
    visited = []
    unvisited = []
    distances = []
    previous = []
    name2idx = graph.artwork_to_index
    current = name2idx[installation_A] ## start node
    count = name2idx[installation_B] ## end node
    for i in range(len(graph.adjacency_mtx)):
        distances.append(float('inf')) ## initialize all distances to infinity
    distances[current] = 0
    for i in range(len(graph.adjacency_mtx)):
        previous.append(-1) ## impossible distance for reference
    for i in graph.installations:
        unvisited.append(name2idx[i]) ## change string to indexes
    while unvisited != [] and current in unvisited:
        min_distance = float("inf")
        visited.append(current)
        unvisited.remove(current)
        for i in unvisited:
            if graph.adjacency_mtx[current][i] != 0 and distances[current] + graph.adjacency_mtx[current][i] < distances[i]:
                distances[i] = distances[current] + graph.adjacency_mtx[current][i]
                previous[i] = current ## update
        for i in unvisited:
            if distances[i] < min_distance:
                min_node = i
                min_distance = distances[i]
        current = min_node
    if previous[count] == -1:
        return (None, [])
    else:
        path = [graph.installations[count]]
        end = count
        while previous[end] != -1:
            end = previous[end]
            path.append(graph.installations[end])
        path.reverse()
        return (distances[count], path)