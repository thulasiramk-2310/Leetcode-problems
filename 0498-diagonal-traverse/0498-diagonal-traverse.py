class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        pieces = collections.defaultdict(list)

        for j in range(n):
            for i in range(m):
                pieces[i + j].append(mat[i][j])
        
        ans = []
        for i in range(m + n):
            if i % 2 == 0:
                ans += pieces[i]
            else:
                ans += pieces[i][::-1]
        return ans