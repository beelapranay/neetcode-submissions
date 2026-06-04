class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = 0
        visited = set()

        for a, b in edges:
            graph[b].append(a)
            graph[a].append(b)
        
        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res
        
