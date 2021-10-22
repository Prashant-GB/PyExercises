reverse_name = "My name is prashant" [::-1]
print(reverse_name)

def reverse_words(sentence):
    words = sentence.split(' ')

    new_re_words = [word[::-1] for word in words]

    rest_word = ' '.join(new_re_words)
    return rest_word

str1="some pepole are going to  somewhere"
print(reverse_words(str1))
str2="in between a queen"
print(reverse_words(str2))
num1= 1234567
print(reverse_words(num1))

