from tkinter import *
import random as rand
import math

# Neighbors, including diagonals, from northwest to west.
# Values are backwards due to window coordinate system.
relative_coords = [(-1, -1), (0, -1), (1, -1), (1, 0), 
                   (1, 1), (0, 1), (-1, 1), (-1, 0)]

width = 800
height = 800
rows = 50
columns = 50

pixel_width = width // rows
pixel_height = height // columns


class Node():
    def __init__(self, x, y, blocked):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0

        self.draw_x = self.x * pixel_width
        self.draw_y = self.y * pixel_height

        self.neighbors = []
        self.previous = None
        self.blocked = blocked

    def get_neighbors(self, grid):
        for k in relative_coords:
            if (self.x + k[0] >= 0 and self.x + k[0] < rows) and \
               (self.y + k[1] >= 0 and self.y + k[1] < columns):
                possible_neighbor = grid[self.x + k[0]][self.y + k[1]]
                if not possible_neighbor.blocked:
                    self.neighbors.append(possible_neighbor)

    def __str__(self):
        return "Node at x={}, y={}.".format(self.x, self.y)

# Draws list of Nodes.
def draw(node=None, completed=False, route=None):
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            current_node = nodes[i][j]
            
            blocked = current_node.blocked
            color = "white"

            if completed:
                if current_node in route:
                    color = "red"
            else:
                if current_node == node:
                    color = "green"
                elif current_node == end or current_node == start:
                    color = "red"
                elif current_node in open_set:
                    color = "red"
                elif current_node in closed_set:
                    color = "blue"

            if blocked:
                color = "black"

            x = current_node.draw_x
            y = current_node.draw_y

            rect = canvas.create_rectangle(x, y, x + pixel_width, y + pixel_height, fill=color, width=1)
            canvas.move(rect, 0, 0)

# Generates a nested list of Nodes to move through.
def generate_nodes():
    node_set = []
    for i in range(rows):
        sub_node_set = []
        for j in range(columns):
            blocked = False
            if rand.random() < 0.3 and \
                  (i, j) != (0, 0) and \
                  (i, j) != (rows - 1, columns - 1):
                blocked = True
            sub_node_set.append(Node(i, j, blocked))
        node_set.append(sub_node_set)

    for i in node_set:
        for j in i:
            j.get_neighbors(node_set)

    return node_set
        
# Heuristic cost of each movement.
def cost(node1, node2):
    delta_x = node2.x - node1.x
    delta_y = node2.y - node1.y
    dist = math.sqrt(((delta_x ** 2) + (delta_y ** 2)))
    return dist

# Displays optimal route.
def optimal_route(node):
    route = []
    while node.previous:
        route.append(node)
        node = node.previous
    route.append(node)
    draw(completed=True, route=route)
    
# A* algorithm.
def pathfind():
    while open_set:
        root.update()
        canvas.delete("all")

        current = open_set[0]
        for i in open_set:
            if i.f < current.f:
                current = i

        if current == end:
            optimal_route(current)
            return

        open_set.remove(current)
        closed_set.append(current)
        draw(current)

        for i in current.neighbors:
            if i in closed_set:
                continue
            possible_g = current.g + 1

            if i not in open_set:
                open_set.append(i)
            elif possible_g >= i.g:
                continue

            i.previous = current
            i.g = possible_g
            i.f = i.g + cost(i, end)


if __name__ == "__main__":
    root = Tk()
    root.geometry("{}x{}".format(width, height))

    canvas = Canvas(root, width=width, height=height)
    canvas.pack()

    nodes = generate_nodes()
    start = nodes[0][0]
    end = nodes[rows - 1][columns - 1]

    closed_set = []
    open_set = [start]
    
    start.g = 0
    start.f = cost(start, end)

    root.after(0, pathfind)
    root.mainloop()