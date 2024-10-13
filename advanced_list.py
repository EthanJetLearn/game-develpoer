L1=[1,2,3,4,5,6,7,8,9]
L1.append(10)
for i in L1:
    print(i,end=" ")
#create a 2D list
print()
matrix=[[1,2,3,0],[4,5,6,0],[7,8,9,0]]
#to print number of rules
print(len(matrix))
#to print number of collums
print(len(matrix[0]))
#to access same values
print(matrix[2][0]) 
print(matrix[1][1])
#looping over a 2D a list
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end="")
    print("\n")
#take a input to create a 2D list/matrix
row=int(input("enter number of rows:"))
column=int(input("enter number of columns"))
matrix=[]
for i in range(row):
    temp=[]
    for j in range(column):
        x=int(input("enter a value:"))
        temp.append(x)
    matrix.append(temp)
print(matrix)        
