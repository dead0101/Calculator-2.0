import math

print("Hello welcome to a simple python calculator")
print(" ")
print("version 2.0")
print("\n")
print("1.)multiply")
print(" ")
print("2.)divide")
print(" ")
print("3.)add")
print(" ")
print("4.)Subrtract")
print(" ")
print("5.)Exponent")
print(" ")
print("6.)Square root")
simple_1 = input("Please enter your option: ")
if simple_1 == "1":
    print("\n" * 100)
    def multiply(a, b):
        return (a * b)
    
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    
    print(f'{a} multiplied by {b} is {multiply(a, b)}')
    
if simple_1 == "2":
    print("\n" * 100)
    def divide(a, b):
        return (a / b)
    
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    
    print(f'{a} divided by {b} is {divide(a, b)}')
    
if simple_1 == "3":
    print("\n" * 100)
    def add(a, b):
        return (a + b)
    
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    
    print(f'Sum of {a} and {b} is {add(a, b)}')
    
if simple_1 == "4":
    print("\n" * 100)
    def Subrtract(a, b):
        return (a - b)
        
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    
    print(f'The difference of {a} and {b} is {Subrtract(a, b)}')

if simple_1 =="5": #multiplying exponets
    print("\n" * 100)
    def Exponent(a, b):
        return (a ** b)
    a = int(input('Enter 1st number(Base): '))
    b = int(input('Enter 2nd number(Exponent): '))
    
    print(f'{a} and {b} is {Exponent(a, b)}')
    
if simple_1 =="6": #Square root
    print("\n" * 100)
    def square(a):
        return(print(math. sqrt(a)))
    a = int(input('Enter number: '))
    
    print("\n" * 100)
    
    print(f'The square root of {a} is {print(math.sqrt(a))}')
#added suare root and Exponents
