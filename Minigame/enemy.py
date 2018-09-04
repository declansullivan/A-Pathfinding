class Enemy():
    def __init__(self, start, end):
        self.start = start
        self.current = start
        self.end = end
        self.route = None


    def edit_route(self, route):
        if len(route) == 0:
            self.route = None
        else:
            for i in range(len(route)):
                if self.current == route[i]:
                    self.route = route[(i + 1)::]

    def move(self):
        if self.route:
            self.current = self.route[0]