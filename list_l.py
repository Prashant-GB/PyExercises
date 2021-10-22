# import collections

# list_m = [2,4,5,6,2,4,3,6]
# duplicates=[]
# exists=[]

# for item,count in collections.Counter(list_m).items():
#     if count > 1:
#         duplicates.append(item)
#     else:
#          exists.append(item)

# print(duplicates)
# print(exists)


# num_list = [20,10,50,40,70,30,100]
# i = []
# for x in num_list:
#     if x<= 50:
#           i.append(x)
        
# print(i)


# sample_list = [2,4,5,3,2,5,7,8,7] 

# exist=[]
# duplicates = []

# for i in sample_list:
#     if i not in exist:
#         exist.append(i)
#     else:
#         duplicates.append(i)

# print(exist)
# print(duplicates)


list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50,20]

list1[1][2][2][1] = 3500

print(list1[1]);
print(list1[1][2]);
print(list1[1][2][2]);
print(list1[1][2][2][1]);



print(list1)

# print(list1[1]) = [10, 15, [20, 25, [30, 400], 40], 45]
# print(list1[1][2]) = [20, 25, [30, 400], 40]
# print(list1[1][2][2]) = [30, 40]
# print(list1[1][2][2][1]) = 40

quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))


for l in 'Jhon':
   if l == 'o':
      pass
   print(l, end=", ")


x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)