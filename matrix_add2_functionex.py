m1= {
    [2,3]
    [5,7]
}
m2= {
    [7,8]
    [6,2]
}

height = len(matrix1)
width= len(matrix1[0])


def create_empty_matrix(width, height):
    result=[]
    # initialize the resulting matrix
    for i in range(0, height):
    result.append([])
        for j in range(0, width):
        result[i].append(0)
    return result
height = len(matrix1)
width = len(matrix1[0])
matrix = create_empty_matrix(width, height)
matrix = create_empty_matrix(3, 3)

#fill in the matrix
def add_matrices(m1, m2):
    height = len(m1)
    width = len(matrix1[0])
    matrix = create_empty_matrix(width, height)
    
    for i in range(0, height):
        for j in range(0, width):
            cell1= m1[i][j]
            cell2= m2[i][j]

            matrix[i][j]= cell1 + cell2 
    return  matrix

m1= {
    [2,3]
    [5,7]
}
m2= {
    [7,8]
    [6,2]
}

result= add_matrices(matrix1, matrix2)
print result