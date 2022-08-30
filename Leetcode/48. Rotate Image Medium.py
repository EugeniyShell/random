class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        y = len(matrix[0])-1
        for z in range(len(matrix[0])//2):
            for x in range(y-2*z):
                matrix[z][x+z],matrix[x+z][y-z],matrix[y-z][y-x-z],matrix[y-x-z][z] = matrix[y-x-z][z],matrix[z][x+z],matrix[x+z][y-z],matrix[y-z][y-x-z]
