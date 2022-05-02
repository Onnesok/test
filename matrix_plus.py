def matrx(matrix1, matrix2):
    cnt = 0
    if len(matrix1) == len(matrix2):
        for i in range(len(matrix1)):
            if len(matrix1[i]) == len(matrix2[i]):
                for j in range(len(matrix1[i])):
                    rs = matrix1[i][j] + matrix2[i][j]
                    matrix2[i][j] = rs
            else:
                cnt += 1
    else:
        cnt += 1
    if cnt == 0:
        return matrix2
    else:
        return "No of columns not same"

matrix1 = [[1,5,4],[-4,3,3]]
matrix2 = [[2,-1,-3],[4,-1,-4]]
result = matrx(matrix1, matrix2)
if type(result) == str:
    print("No of columns not same")
else:
    print("matrix_sum = ",result)