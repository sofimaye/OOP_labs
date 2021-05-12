"""Масиви"""

def transpose(matrix):
    a = []
    for i in range(len(matrix[0])):
        b = []
        for row in matrix:
            b.append(row[i])
        a.append(b)
    return a

B = [[1.0,2.0,3.0],
    [4.0,5.0,6.0],
    [7.0,8.0,9.0]]

C = transpose(B)
print("C:", C)
print("B:", B)

def small(list): #list of float
    smallest = list[0] #НАЧИНАЕМ СНАЧАЛА
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

sum = 0
for row in C:
    sum += (small(row))
print("Сумма найменших елементів: ",(sum))




