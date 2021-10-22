num_list = [20,10,50,40,70,30,100]
i = []
for x in num_list:
    if x<= 50:
          i.append(x)
        
    print(i)

rows = 8

for i in range (rows):
    for j in range(i):
        print(i,end=' ')
    print(' ')

rows= int(input("Enter number of rows : ")) 

for x in range(rows):
    for y in range(x):
        print(y,end=" ")
    print(" ")


rows = 8
b=0
for x in range(rows,0,-1):
    b += 1
    for y in range(1,x-1):
        print(b,end=' ')
    print('\r')


