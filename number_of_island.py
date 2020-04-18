class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.lands = {
            (row, col)
            for row, line in enumerate(grid)
            for col, land in enumerate(line)
            if land == '1'
        }

        island_counter = 0
        # Remove islands from the bag one by one
        while self.lands:
            island_seed = next(iter(self.lands))  # pick a random land
            island_counter += 1
            self.remove_island(island_seed)

        return island_counter
    
    def remove_island(self, coordinates):
        try:
            self.lands.remove(coordinates)
        except KeyError:
            return

        x, y = coordinates
        self.remove_island((x - 1, y))
        self.remove_island((x + 1, y))
        self.remove_island((x, y - 1))
        self.remove_island((x, y + 1))
