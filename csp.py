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

