def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
    print("---------------------------------------------")

greet()
greet("Alice")	
greet("Alice", "Bob")
greet("Alice", "Bob", "Charlie")

def add(*numbers): # *numbers is a tuple
    total = 0
    for number in numbers:
        total += number
    return total

print(f"add(1,2):{add(1,2)}")
print(f"add(1,2,3,4,5,6,7,8,9,10):{add(1,2,3,4,5,6,7,8,9,10)}")
print(f"add(34,45,54):{add(34,45,54)}")
