import pytest
from src.graphs import Graphs

class TestGraphs:

    def setup_method(self):
        self.sol = Graphs()

    def test_num_islands(self):
        grid1 = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        assert self.sol.num_islands(grid1) == 1

        grid2 = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        assert self.sol.num_islands(grid2) == 3

    def test_shortest_path_bfs(self):
        adj = {
            1: [2, 3],
            2: [1, 4],
            3: [1, 4],
            4: [2, 3, 5],
            5: [4]
        }
        assert self.sol.shortest_path_bfs(adj, 1, 5) == 3
        assert self.sol.shortest_path_bfs(adj, 1, 4) == 2
        assert self.sol.shortest_path_bfs(adj, 1, 1) == 0
        assert self.sol.shortest_path_bfs(adj, 1, 99) == -1
