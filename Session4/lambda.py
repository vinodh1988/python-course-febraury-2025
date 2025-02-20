def add(a: int,b: int):
    return a + b

print(add(1,3))
print(add("Raj","Kumar"))

sum=lambda a,b:a+b

print(sum(1,3))
print(sum("Raj","Kumar"))

greet=lambda name:"Hi"+name

print(greet("Raj"))