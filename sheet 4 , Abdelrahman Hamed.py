#1)
import random
def generate_password(length, chars):
    password = ' '.join(random.choices(chars, k=length))
    return password
print(generate_password(8, "abcde"))

 
#2)
def comperehension():
    list1=[]
    for x in range(48,58):
        list1.append(chr(x))
    for x in range(65,91):
        list1.append(chr(x))
    for x in range(97,123):
        list1.append(chr(x))
    print(" ".join(list1))
comperehension()


#3)
family=["Abdelrhman","Hamed", "Mohalil", "Mohamed"]
l = {char for name in family for char in name}
print("letters are: ")
print(l)


#4)
def average(*numbers):
    x=0
    for i in numbers:
        x+=i
    return x/len(numbers)

list1=[1,2,3,4,5]
print(average(*list1))


#5)
def substitute(equation, **kwargs):
    for x, y in kwargs.items():
        equation = equation.replace(x, str(y))
    return equation
print(substitute("x * 2 + y * 3 - z * 4", x=5,y=6,z=7))