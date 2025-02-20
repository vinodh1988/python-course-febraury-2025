# Loop through a list of numbers
for x in range(1,11):
    print(f"Number: {x}")

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(f"Number: {number}")

print("\n")

# Loop through a list of strings
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

print("\n")

# Nested for loop to print a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")
    print("\n")