import math as m
import itertools
import heapq


def Edge(points):
    a = points[0]
    b = points[1]
    return m.sqrt(m.pow(m.fabs(a[0] - b[0]), 2) + m.pow(m.fabs(a[1] - b[1]), 2))


def Min_Span_Tree(outside_tree):
    heap = []
    for pair in itertools.combinations(outside_tree, 2):
        heapq.heappush(heap, (Edge(pair), pair))

    inside_tree = set()
    answer = 0
    heapq.heapify(list(outside_tree))
    initial = outside_tree.pop()

    while outside_tree:
        inside_tree.update(initial)

        shortest = min([item for item in heap if initial in item[1]])
        answer += float(shortest[0])
        x, y = shortest[1]
        inside_tree.update(x, y)
        heap.remove(shortest)

        next_point = outside_tree.pop()

        initial = next_point

    return answer


if __name__ == "__main__":

    infile = open("data.txt", "r")

    number_of_cases = int(infile.readline())
    infile.readline()
    for case in range(number_of_cases):
        number_of_points = int(infile.readline())

        points = []
        for point in range(number_of_points):

            data = infile.readline().strip('\n').split(" ")
            point = (float(item) for item in data)
            points.append(tuple(point))

        answer = Min_Span_Tree(points)
        print("%.2f" % round(answer, 2))
        infile.readline()

    infile.close()
