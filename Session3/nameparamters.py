def greet(**kwargs): # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    print("---------------------------------------------")

greet(name="Alice")
greet(sno=1,name="Alice")
greet(sno=1,name="Alice",city="Bangalore")	