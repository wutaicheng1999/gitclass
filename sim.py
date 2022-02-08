import math
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(v1-v2) for v1, v2 in zip(x,y))

def jaccard_dist(x, y):
    return len(x.symmetric_difference(y))/len(x.union(y))

def cosine_sim(x, y):
    if (len(x) != len(y)):
        print('Cannot be calculated')
    dot_product = 0
    x_cross = 0
    y_cross = 0
    for i in range(len(x)):
        dot_product += (x[i]*y[i])
        x_cross += x[i]**2
        y_cross += y[i]**2

    return dot_product/(math.sqrt(x_cross) * math.sqrt(y_cross))