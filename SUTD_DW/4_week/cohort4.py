def transpose_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        l=[]
        for j in matrix:
            l.append(j[i])
        new_matrix.append(l)
    return new_matrix