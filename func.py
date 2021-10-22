def outer(x,y):
    def inner(x,y):
        return x + y
    z = inner(x,y)
    return z + " Developer"

result = outer("JP ","KP")
print(result)


def multi_or_sum(x,y):
    product = x*y
    if product <= 1000:
        return product
    else:
        return x+y
print(multi_or_sum(20,30))

print(multi_or_sum(50,60))

n=8 # convert from decimal to octal number
print('%o' %n)


# Exercise 5: Accept a list of 5 float numbers as an input from the user
# num=[]

# for i in range(0,5):
#     print("Enter num at location",i,':')
#     item = float(input())
#     num.append(item)
# print("user list", num)


# Exercise 6: Write all content of a given file into a new file by skipping line number 5

with open("test.txt",'r') as file:
    lines=file.readlines()

with open("new_test.txt","w") as file:
    count=0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            file.write(line)
            count += 1
