from copy import deepcopy


class CSP:

    def __init__(self, graph):
        self.graph = graph

    def checkWholeGraph(self):
        for node in self.graph:
            if not self.checkNodeConstraints(node):
                return False
        return True

    def checkNodeConstraints(self, node):
        constraint = 0
        if node['shape'] == 'P':
            constraint = self.calculateConstraintValue(node['neighbours'], 'sum', 'left')
        elif node['shape'] == 'H':
            constraint = self.calculateConstraintValue(node['neighbours'], 'sum', 'right')
        elif node['shape'] == 'S':
            constraint = self.calculateConstraintValue(node['neighbours'], 'mul', 'right')
        elif node['shape'] == 'T':
            constraint = self.calculateConstraintValue(node['neighbours'], 'mul', 'left')
        elif node['shape'] == 'C':
            return True
        if node['value'] == constraint or constraint is None:
            return True
        return False

    def calculateConstraintValue(self, neighbours, type, side):
        acc = 0
        if type == 'mul':
            acc = 1
        for neighbour in neighbours:
            if self.graph[neighbour]['value'] == -1:
                return None
            if type == 'sum':
                acc += self.graph[neighbour]['value']
            elif type == 'mul':
                acc *= self.graph[neighbour]['value']
        if side == 'left':
            return int(str(acc)[0])
        elif side == 'right':
            string = str(acc)
            return int(string[len(string)-1])

    def applyUnitConstraint(self, node):
        value = node['value']
        if len(node['neighbours']) == 1:
            neighbour = node['neighbours'][0]
            domain = deepcopy(self.graph[neighbour]['domain'])
            revised = False
            for d in domain:
                if d != value:
                    self.graph[neighbour]['domain'].remove(d)
                    revised = True
                if revised:
                    if domain != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        self.graph[neighbour]['domainHistory'].append(domain)

    def applySquareConstraints(self, node):
        value = node['value']
        if value in [1, 3, 5, 7, 9]:
            for neighbour in node['neighbours']:
                domain = deepcopy(self.graph[neighbour]['domain'])
                revised = False
                for d in self.graph[neighbour]['domain']:
                    if d == 2 or d == 4 or d == 6 or d == 8:
                        self.graph[neighbour]['domain'].remove(d)
                        revised = True
                    if revised:
                        if domain != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            self.graph[neighbour]['domainHistory'].append(domain)
        self.applyUnitConstraint(node)

    def applyPentagonConstraints(self, node):
        # Can think of any pentagon constraint?
        self.applyUnitConstraint(node)

    def applyTriangleConstraints(self, node):
        # Can think of any triangle constraint?
        self.applyUnitConstraint(node)

    def applyHexagonConstraints(self, node):
        # Can think of any hexagon constraint?
        self.applyUnitConstraint(node)

    def applyCircleConstraints(self, node):
        # Can think of any hexagon constraint?
        self.applyUnitConstraint(node)

