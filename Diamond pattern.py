rowSize = int(input("enter the number of rows: "))
if rowSize%2==0:
    halfdiamrow = int(rowSize/2)
else:
    halfdiamrow = int(rowSize/2) +1
space = halfdiamrow-1
for i in range (1, halfdiamrow+1): 
    for j in range(1, space+1): 
        print(end=" ")
    space= space-1 
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num = num + 1
    print()
space = 1 
#Loop for lower part --->
for i in range (1, halfdiamrow+1): 
    for j in range(1, space+1): 
        print(end=" ")
    space= space+1 
    num = 1
    for j in range(1, 2*(halfdiamrow-i)):
        print(end=str(num))
        num = num + 1
    print()
space = 1 
