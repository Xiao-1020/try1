n = int(input())
matrix = [[0] * n for _ in range(n)]
num = 1
top, bottom, left, right = 0, n - 1, 0, n - 1


while num <= n * n:
    # 从左到右填充上边界
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    # 从上到下填充右边界
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    # 从右到左填充下边界
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    # 从下到上填充左边界
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1


for i in range(n):
    for j in range(n):
        print("{:3}".format(matrix[i][j]), end='')
    print()