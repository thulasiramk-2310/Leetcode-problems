class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        starts = []

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    starts.append([r, c, ])


        for row, col in starts:
            r, c = row, col
            temp = []
            while r < ROWS and c < COLS:
                temp.append(grid[r][c])
                r += 1
                c += 1

            temp.sort()
            r, c = row, col
            di = 1 if col else -1
            i = 0 if col else len(temp) - 1
            while r < ROWS and c < COLS:
                grid[r][c] = temp[i]
                i += di
                r += 1
                c += 1

        return grid
                    