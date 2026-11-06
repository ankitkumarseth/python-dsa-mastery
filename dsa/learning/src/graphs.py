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
        pass

    def shortest_path_bfs(self, adj: dict[int, list[int]], start: int, target: int) -> int:
        """
        Given an unweighted adjacency list, find the shortest distance (in number of edges)
        from start to target. Return -1 if unreachable.
        
        Example:
            adj = {1: [2, 3], 2: [4], 3: [4], 4: []}, start = 1, target = 4 -> 2
        """
        pass
