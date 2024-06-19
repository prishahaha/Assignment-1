'''
1.
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
print("Sum of two numbers=",num1+num2)



2.
num=int(input("Enter the number:"))
if(num%2==0):
    print("num is even")
else:
    print("num is odd")



3.
n=int(input("Enter the number:"))
fact = 1
i = 1
while i <= n:
    fact *= i
    i  += 1
    print("factorial:",fact)


4.
str = input("Enter your name:")
print("Hello,How are you doing?")


7.
str = input("Enter the str:")
print(len(str))


8.
str1 = "Hello"
str2 = "World"
result = str1 +" "+str2
print(result)


9.
str = "I'm writing a program in python"

if "program" in str1:
    print("Yes,it is a substring of str1 ")
else:
    print("not substring")



10.
str = "i'm writing a program in python"
print(str.upper())


11.
def fibonacci_numbers(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_numbers(num-2)+ fibonacci_numbers(num-1)
n = 7
for i in range(0,n):
    print(fibonacci_numbers(i),end = " ")



12.
num = input("Enter number:")
sum = 0
for i in num:
    sum = sum+int(i)
    print(sum)




13.
user_age = int(input("Enter your birth year:"))
current_yr = date.today().year
birth_year = (current_yr - user_age)
print("Hello","you were born in:",birth_year,".")


16.
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
        return dict
print(char_frequency('google.com'))


17.
str = "hello,this is my first assignment in python"
print(str.upper())


18.
def check(s1,s2):
    if(sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
s1 = "listen"
s2 = "silent"
check(s1,s2)


19.
punctuation = '''@#$%^&*(){}![]:'".,<>?/'''
my_str="Hello!!!,this is my,/ first: program>> in python<>"
no_punct=""
for char in my_str:
    if char not in punctuation:
        no_punct = no_punct + char
        print(no_punct)


20.
total = 0
list1 = [1,2,3,4,5,6]
for ele in range (0,len(list1)):
    total = total + list1[ele]
    print("sum of all elements in given list:",total)


21.
list = [1,2,3,3,4,5,6,7,7,8,3,4,3,9,3]
count =list.count(3)
print(count)


22.
list = [23,56,78,3,76,34,77,89,2,12,31]
x= min(list)
print("the minimum of the element in list:",x)
y= max(list)
print("the maximum of the element in list: ",y)



23.

celsius= int(input("Enter temperature in celsius:"))
Fahrenheit=(1.8*celsius)+32
print("Temperature in fahrenheit:",Fahrenheit)


27.
str = "Hello World"
x = list(str)
print(x)
'''














