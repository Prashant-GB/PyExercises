with open ("sample.txt","r") as file:
    data= file.read().replace('\n','      ')
    print(data)

with open ("sample.txt","r") as file:
    data1= file.read().replace('/n','      ')
    print(data1)