class Solution(object):
    def numIslands(self, grid):

        isIsland="1"
        notIsland="0"
        
        len_row= len(grid)
        len_col= len(grid[0])
        
        island_count = 0
        directions=((-1,0),(1,0),(0,1),(0,-1))
        
        def count_validIslands(i, j):
            
            return True if 0 <= i < len_row and 0 <= j < len_col and grid[i][j] == isIsland else False
                
        
        for row in range(len_row):
            for col in range(len_col):
                if count_validIslands(row, col):
                    island_count += 1
                    queue = deque([(row, col)])
                    while len(queue) != 0:
                        row_ofQueue, column_ofQueue = queue.popleft()
                        if grid[row_ofQueue][column_ofQueue] == isIsland:
                            grid[row_ofQueue][column_ofQueue] = notIsland
                            for row_move, column_move in directions:
                                if count_validIslands(row_ofQueue + row_move, column_ofQueue + column_move):
                                    queue.append((row_ofQueue + row_move, column_ofQueue + column_move))

        return island_count