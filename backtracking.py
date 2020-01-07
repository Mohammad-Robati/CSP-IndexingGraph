class CSPBacktracking:

    def __init__(self, csp):
        self.csp = csp

    def isComplete(self):
        graph = self.csp.graph
        for node in graph:
            if node['value'] == -1:
                return False
        return True

    def getUnassignedNode(self):
        graph = self.csp.graph
        for node in graph:
            if node['value'] == -1:
                return node

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

    def forwardChecking(self):
        pass

    def backtrack(self):
        if self.isComplete():
            return True
        node = self.getUnassignedNode()
        for d in node['domain']:
            node['value'] = d
            if self.checkNeighbours(node):
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
