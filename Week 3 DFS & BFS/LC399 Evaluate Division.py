class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Store the graph
        graph = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1.0 / v
        # print(graph)
        
        # Check the queries
        self.ans = []
        for x, y in queries:
            print("check:", x, y)
            if x not in graph and y not in graph:
                self.ans.append(-1.0)
                continue
            self.visited = set()
            self.ans.append(self.divide(x, y, graph))
        return self.ans
    
    def divide(self, A, B, graph):
        # If A == B, then the result is 1.0
        if A == B:
            return 1.0
        # Mark A
        self.visited.add(A)
        # Iterate through all the neighbors of A
        for C in graph[A]:
            if C in self.visited:
                continue
            self.visited.add(C)
            d = self.divide(C, B, graph)
            if d > 0:
                return d * graph[A][C]
        return -1.0
