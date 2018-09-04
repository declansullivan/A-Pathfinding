import math, time
import node, enemy

class AStar():
    def __init__(self, root, canvas, width, height, rows, cols):
        self.root = root
        self.canvas = canvas
        self.width = width
        self.height = height
        
        self.rows = rows
        self.cols = cols

        self.node_width = self.width // self.cols
        self.node_height = self.height // self.rows

        self.nodes = node.generate_nodes(self.rows, self.cols)

        self.end = self.nodes[self.cols // 2][self.rows // 2]

        e = enemy.Enemy(self.nodes[0][0], self.end)
        e2 = enemy.Enemy(self.nodes[self.rows - 1][0], self.end)
        e3 = enemy.Enemy(self.nodes[0][self.cols - 1], self.end)
        e4 = enemy.Enemy(self.nodes[self.rows - 1][self.cols - 1], self.end)

        self.enemies = [e, e2, e3, e4]
        # self.enemies = [e]


    def draw(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i])):
                current = self.nodes[i][j]
                blocked = current.blocked
                color = "white"

                enemy_spots = [i.current for i in self.enemies]

                if current == self.end:
                    color = "green"
                if current in enemy_spots:
                    color = "red"
                if blocked:
                    color = "black"

                x = current.x * self.node_width
                y = current.y * self.node_height

                rect = self.canvas.create_rectangle(x, y, x + self.node_width, \
                                                    y + self.node_height, \
                                                    fill=color, width = 1)
                self.canvas.move(rect, 0, 0)


    def up(self):
        if self.end.y - 1 >= 0 and not self.nodes[self.end.x][self.end.y - 1].blocked:
            self.end = self.nodes[self.end.x][self.end.y - 1]
            self.update_enemy()

    def down(self):
        if self.end.y + 1 < self.rows and not self.nodes[self.end.x][self.end.y + 1].blocked:
            self.end = self.nodes[self.end.x][self.end.y + 1]
            self.update_enemy()

    def left(self):
        if self.end.x - 1 >= 0 and not self.nodes[self.end.x - 1][self.end.y].blocked:
            self.end = self.nodes[self.end.x - 1][self.end.y]
            self.update_enemy()
    
    def right(self):
        if self.end.x + 1 < self.cols and not self.nodes[self.end.x + 1][self.end.y].blocked:
            self.end = self.nodes[self.end.x + 1][self.end.y]
            self.update_enemy()

    def update_enemy(self):
        for i in self.enemies:
            i.end = self.end


    def enemy_move(self, route, enemy):
        enemy.edit_route(route)
        enemy.move()


    def heuristic_cost(self, node1, node2):
        return math.sqrt((node2.x - node1.x) ** 2 + (node2.y - node1.y) ** 2)


    def optimal_route(self, node):
        route = []
        while node.previous:
            route.insert(0, node)
            node = node.previous
        route.insert(0, node)
        return route


    # Defining variables to increase readability.
    def astar(self, enemy):
        open_set = [enemy.start]
        closed_set = []

        enemy.start.g = 0
        enemy.start.f = self.heuristic_cost(enemy.start, enemy.end)

        current = enemy.start
        end = self.end

        while open_set:
            current = open_set[0]
            for i in open_set:
                if i.f < current.f:
                    current = i

            if current == end:
                self.enemy_move(self.optimal_route(current), enemy)
                break

            open_set.remove(current)
            closed_set.append(current)

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
                i.f = i.g + self.heuristic_cost(i, end)

    
    def run(self):
        root = self.root
        canvas = self.canvas
        self.draw()

        enemy_positions = [i.current for i in self.enemies]

        while self.end not in enemy_positions:
            self.draw()
            root.update()
            canvas.delete("all")
            for i in self.enemies:
                self.astar(i)
            enemy_positions = [i.current for i in self.enemies]
            time.sleep(0.15)
        
    def keep_window(self):
        self.draw()
