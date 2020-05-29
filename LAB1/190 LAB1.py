from lab1_utilities import *


def get_installations_from_file(file_name):
    open_file = open(file_name, 'r')
    read = open_file.readlines()
    x = []
    installations = []
    for i in read:
        x.append(i.strip())
    x = x[1:]
    print(x)
    for i in x:
        installations.append(Installation(i[0], i[1], i[2], i[3]))

    return installations


def euclidean_distance(position1, position2):
    x = position2[0] - position1[0]
    y = position2[0] - position1[0]
    s = (x**2 + y**2)**0.5
    return s


def get_adjacency_mtx(installations):

    pass


def make_graph(installations):
    # implement
    pass


def find_shortest_path(installation_A, installation_B, graph):
    # implement
    pass

if __name__ == "__main__":
    print(get_installations_from_file('public_artwork_data.txt'))