from copy import deepcopy


class CSPBacktracking:

    def __init__(self, csp):
        self.csp = csp
        self.graph = deepcopy(csp.graph)

    def isComplete(self):
        graph = self.csp.graph
        for node in graph:
            if node['value'] == -1:
                return False
        return True

    def getUnassignedNode(self, mrv):
        graph = self.csp.graph
        min = 20
        minNode = None
        for node in graph:
            if node['value'] == -1:
                if not mrv:
                    return node
                else:
                    length = len(node['domain'])
                    if minNode is None:
                        min = length
                        minNode = node
                    else:
                        if length < min:
                            min = length
                            minNode = node
        return minNode

    def checkNeighbours(self, node):
        graph = self.csp.graph
        hasUnvisitedNode = False
        for neighbour in node['neighbours']:
            value = graph[neighbour]['value']
            if value != -1:
                if not self.csp.checkNodeConstraints(graph[neighbour]):
                    return False
            else:
                hasUnvisitedNode = True
        if hasUnvisitedNode:
            return True
        else:
            return self.csp.checkNodeConstraints(node)

    def forwardChecking(self, node):
        graph = self.csp.graph
        if node['shape'] == 'S':
            self.csp.applySquareConstraints(node)
        elif node['shape'] == 'P':
            self.csp.applyPentagonConstraints(node)
        elif node['shape'] == 'T':
            self.csp.applyTriangleConstraints(node)
        elif node['shape'] == 'H':
            self.csp.applyHexagonConstraints(node)
        for node in graph:
            if not node['domain']:
                return False
        return True

    def backtrack(self):
        if self.isComplete():
            return True
        node = self.getUnassignedNode(mrv=True)
        for d in node['domain']:
            node['value'] = d
            if self.checkNeighbours(node):
                isSuccess = True #self.forwardChecking(node)
                if isSuccess:
                    result = self.backtrack()
                    if result != False:
                        return True
        node['value'] = -1
        return False

    def run(self):
        self.backtrack()
        for node in self.csp.graph:
            print(node['value'])
        print(self.csp.checkWholeGraph())
