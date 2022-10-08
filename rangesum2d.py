class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col = len(matrix),len(matrix[0])
        
        self.presum = [[0]*(col + 1) for x in range(row + 1)]
        for x in range(row):
            presum = 0
            for y in range(col):
                presum = presum + matrix[x][y]
                above = self.presum[x][y + 1]
                self.presum[x + 1][y + 1] = presum + above
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ro1,co1,ro2,co2 = row1 + 1,col1 + 1,row2+1,col2+1
        
        bottomleft = self.presum[ro2][co2]
        above = self.presum[ro1 - 1][co2]
        left = self.presum[ro2][co1 - 1]
        topleft = self.presum[ro1 - 1][co1 - 1]
        return bottomleft -above - left + topleft
                


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)