import math
def vector_from_points(p1, p2):
    '''
    (list, list) -> list
    take 2 list coordinates and output their resultant vector as a list
    '''
    q = []
    for i in range(0, len(p2)):
        q.append(p2[i] - p1[i])
    return q

def vector_length(v):
    '''
    (list) -> float
    takes list input and uses the euclidean distance formula to produce the scalar output
    '''
    q = 0
    for i in range(0, len(v)):
        if len(v) == 0:
            return -1
        else:
            q += (v[i])**2
    x = q**0.5
    return x
def angle_between(v, w):
    '''
    (list, list) -> float
    takes equal component lists and output their angle using the cosine formula
    '''
    t = 0
    for i in range(0, len(v)):
        t += v[i] * w[i]
    r = t / (vector_length(v) * vector_length(w))
    x = math.acos(r)
    return math.degrees(x)
def dot_product(v,w):
    '''
    (list, list) -> float
    Takes 2 lists as inputs and outputs float dot product
    '''
    t = 0
    for i in range(0, len(v)):
        if vector_length(v) == 0 or vector_length(w) == 0:
            t = 0
        else:
            t += v[i] * w[i]
    return t

def unit_vector(v):
    '''
    (list) -> list
    Takes list of coordinates as input and outputs the corresponding unit vector
    '''
    n = []
    for i in range(0, len(v)):
        n.append(v[i] / vector_length(v))
    return n
def cross_product(v,w):
    '''
    (list, list) -> list
    takes two vector lists as input and outputs the cross product as a list
    '''
    if len(v) > 3 or len(w) > 3:
        return []
    for i in range(0,3):
        if len(v) < 3:
            for i in range(0, 3):
                v.append(0)
        if len(w) < 3:
            for i in range(0, 3):
                w.append(0)
    f1 = v[1] * w[2] - v[2] * w[1]
    f2 = w[0] * v[2] - w[2] * v[0]
    f3 = v[0] * w[1] - v[1] * w[0]
    f = [f1, f2, f3]
    return f


def scalar_projection(v,w):
    '''
    (list, list) -> float
    takes 2 vector lists as inputs and gives the scalar projection of the first vector onto the second as an output
    '''
    f = dot_product(v, w) / vector_length(v)
    return f

def vector_projection(v,w):
    '''
    (list, list) -> list
    Takes two vector lists as inputs and returns the vector projection of the first vector onto the second as the output
    '''
    a = []
    for i in range(0, len(v)):
        a.append(v[i] * dot_product(v,w))
    b = []
    for i in range(0, len(a)):
        b.append(a[i] / (vector_length(v))**2)
    return b


if __name__ == "__main__":
    print(vector_from_points([3, -1, 0], [10, 0, 1]))
    print(vector_length([2, 1]))
    print(angle_between([0, 1, 0, 1], [1, 3, 4, 5]))
    print(dot_product([0, 0, 0, 0], [0, 0, 0, 0]))
    print(unit_vector([2, 1]))
    print(cross_product([2, 8], [1, 4, 3]))
    print(scalar_projection([0, 3], [1.5, 2]))
    print(vector_projection([0, 3], [1.5, 2]))
