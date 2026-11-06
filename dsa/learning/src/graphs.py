from collections import deque

class Graphs:
    """
    Practice fundamental Graph algorithms (DFS, BFS, Connected Components).
    """

    def num_islands(self, grid: list[list[str]]) -> int:
        """
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
        return the number of islands.
        
        Example:
            grid = [
              ["1","1","0","0","0"],
              ["1","1","0","0","0"],
              ["0","0","1","0","0"],
              ["0","0","0","1","1"]
            ] -> 3
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # Mark visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)
        return island_count

    def shortest_path_bfs(self, adj: dict[int, list[int]], start: int, target: int) -> int:
        """
        Given an unweighted adjacency list, find the shortest distance (in number of edges)
        from start to target. Return -1 if unreachable.
        
        Example:
            adj = {1: [2, 3], 2: [4], 3: [4], 4: []}, start = 1, target = 4 -> 2
        """
        if start == target:
            return 0
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            node, dist = queue.popleft()
            if node == target:
                return dist
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return -1
