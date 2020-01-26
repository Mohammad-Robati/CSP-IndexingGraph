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
                  'domain': [i+1 for i in range(9)],
                  'domainHistory': [[i+1 for i in range(9)]]})
    i += 1
for i in range(numberOfEdges):
    pair = input().split()
    graph[int(pair[0])]['neighbours'].append(int(pair[1]))
    graph[int(pair[1])]['neighbours'].append(int(pair[0]))
csp = CSP(graph)
cspSolver = CSPBacktracking(csp)
cspSolver.run()

# 4
# 4
# P S P T
# 0 1
# 1 2
# 1 3
# 2 3

# 9
# 8
# C P H S S H H T C
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6
# 6 7
# 7 8

# 9
# 8
# C S H S S H P T C
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6
# 6 7
# 7 8

