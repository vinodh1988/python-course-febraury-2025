def greet(name="Guest"):
    print(f"Hello, {name}!")

def add(a=0, b=0):
    return a + b

def describe_pet(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

# Example usage
greet()
greet("Alice")

print(add())
print(add(5, 10))
print(add(5))
print(add(b=5)) # Keyword parameters

describe_pet("Buddy")
describe_pet("Whiskers", "cat")