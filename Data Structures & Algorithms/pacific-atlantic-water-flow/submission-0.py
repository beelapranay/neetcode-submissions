class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean):
            ocean.add((r, c))

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in ocean
                and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, ocean)
        
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])
        
        return res


        