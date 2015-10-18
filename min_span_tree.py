import math as m
import itertools
import heapq


def Edge(points):
    a = points[0]
    b = points[1]
    return m.sqrt(m.pow(m.fabs(a[0] - b[0]), 2) + m.pow(m.fabs(a[1] - b[1]), 2))


def Min_Span_Tree(points):
    #find all edges & put into a priorityQ
    heap = []
    for pair in itertools.combinations(points, 2):
        heapq.heappush(heap, (Edge(pair), pair))

    inside_tree = set()
    answer = 0

    outside_tree = points

    initial = outside_tree.pop()

    while outside_tree:
        inside_tree.update(initial)

        shortest = min([item for item in heap if initial in item[1]])
        answer += shortest[0]
        x, y = shortest[1]
        inside_tree.update(x, y)

        next_point = outside_tree.pop()

        initial = next_point

    return answer
