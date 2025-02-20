# function with no parameters and no return type
def  simple():
    print("Simple function")
    
simple()

#fucntion with one parameter and no return type
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

#function with two parameters and a return value
def sum(a,b):
    return a + b

print(f"sum(3,4) = {sum(3,4)}")

result=sum(343,53)
result=sum(a=343,b=53)

print(f"sum(343,53) = {result}")	