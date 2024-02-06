# 1 .to print hello world 
print("hello world")

# 2. addition of two numbers
a = int(input("enter number 1"))
b = int(input("enter number 2"))
print("sum of the two numbers is ",a+b)

# 3.division of two real numbers
c = int(input("enter number"))
d = int(input("enter number"))
if ((type(c)==int or float)and (type(d)==int or float)):
    print("division of the two numbers ",a,"and",b,"is ",a/b)
else:
    print("invalid inputs")

# 4.dot product of two vectors
n = int(input("enter the length of the vectors"))
list1= []
list2 = []
print("enter elements of first vector")
for i in range(n):
    a = float(input("enter element {i} of first vector "))
    list1.append(a)
print("enter element of second vector")
for i in range(n):
    b = float(input("enter element {i} of second vector "))
    list2.append(b)

print("the dot product of the vectors is ",result = sum(x * y for x, y in zip(list1, list2)))

# 5.det of a matrix
n = int(input("Enter the size of the matrix: "))
matrix = []

for i in range(n):
    row = [float(x) for x in input(f"Enter elements of row {i + 1} separated by spaces: ").split()]
    matrix.append(row)

if n == 1:
    print(matrix[0][0])
elif n == 2:
    print(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
elif n == 3:
    det_3x3 = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
        matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
        matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )
    print(det_3x3)
else:
    print("Enter matrix size up to 3")