"""2D list are applied in machine learning and data science"""

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1] = 20
print(matrix[0][1])


for row in matrix:
    for item in row:
        print(item)