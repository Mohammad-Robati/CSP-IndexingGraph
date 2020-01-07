from csp import CSP
from backtracking import CSPBacktracking
numberOfNodes = int(input())
numberOfEdges = int(input())
shapes = input().split()
graph = []
i = 0
for shape in shapes:
    graph.append({'index': i,
                  'value': -1,
                  'shape': shape,
                  'neighbours': [],
                  'domain': [i+1 for i in range(9)]})
    i += 1
for i in range(numberOfEdges):
    pair = input().split()
    graph[int(pair[0])]['neighbours'].append(int(pair[1]))
    graph[int(pair[1])]['neighbours'].append(int(pair[0]))
csp = CSP(graph)
cspSolver = CSPBacktracking(csp)
cspSolver.run()