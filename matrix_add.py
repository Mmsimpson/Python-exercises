first_matrix= [[8, 9], [6 ,3]]
second_matrix= [[3, 10], [8, 4]]
sum_matrix= [[] , []]
for i in range(len(first_matrix)):
    for j in range(len(first_matrix[0])):
          sum_matrix[i].append(first_matrix[i][j] + second_matrix[i][j])
print sum_matrix
    


##

m1= {
    [2,3]
    [5,7]
}
m2= {
    [7,8]
    [6,2]
}
#r = [[0,0], [0,0]]
r= []
for row in m1:
    for col in row:
        wip = []
        for col in  row:
            wip.append(0)
        r.append(wip)


width = len(r[0])
height = len(r)

for i in range(height):
    for j in range(width):
        r[i][j] = m1[i][j] + m2[i][j]
print r 