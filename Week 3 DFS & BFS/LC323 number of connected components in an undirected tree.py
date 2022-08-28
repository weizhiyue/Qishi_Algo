class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # construct the graph
        graph = {i: [] for i in range(n)}
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        # use DFS to find the # of connected components
        num_cnt = 0
        self.visited = set()
        for i in range(n):
            if i not in self.visited:
                self.dfs(graph, i, self.visited)
                num_cnt += 1
        return num_cnt
    
    def dfs(self, graph, node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(graph, neighbor, visited)
