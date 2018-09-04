import random as rand

relative_coords = [(-1, -1), (0, -1), (1, -1), (1, 0), 
                   (1, 1), (0, 1), (-1, 1), (-1, 0)]

class Node():
    def __init__(self, rows, cols, x, y, blocked):
        self.rows = rows
        self.cols = cols

        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0

        self.neighbors = []
        self.previous = None
        self.blocked = blocked


    def get_neighbors(self, grid):
        for k in relative_coords:
            if (self.x + k[0] >= 0 and self.x + k[0] < self.rows) and \
               (self.y + k[1] >= 0 and self.y + k[1] < self.cols):
                possible_neighbor = grid[self.x + k[0]][self.y + k[1]]
                if not possible_neighbor.blocked:
                    self.neighbors.append(possible_neighbor)

    def __str__(self):
        return "Node at x={}, y={}.".format(self.x, self.y)


def generate_nodes(rows, cols):
    node_set = []
    for i in range(rows):
        sub_node_set = []
        for j in range(cols):
            blocked = False
            if rand.random() < 0.3:
                blocked = True
            sub_node_set.append(Node(rows, cols, i, j, blocked))
        node_set.append(sub_node_set)

    node_set[0][0].blocked = False
    node_set[rows // 2][cols // 2].blocked = False
    node_set[rows - 1][0].blocked = False
    node_set[0][cols - 1].blocked = False
    node_set[rows - 1][cols - 1].blocked = False

    for i in node_set:
        for j in i:
            j.get_neighbors(node_set)

    return node_set