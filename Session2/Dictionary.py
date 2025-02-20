# Dictionary demo for employee object

# Creating an employee dictionary
employee = {
    'name': 'John Doe',
    'age': 30,
    'department': 'HR',
    'position': 'Manager',
    'salary': 60000
}

# Accessing dictionary values
print("Employee Name:", employee['name'])
print("Employee Age:", employee['age'])
print("Employee Department:", employee['department'])
print("Employee Position:", employee['position'])
print("Employee Salary:", employee['salary'])

# Adding a new key-value pair
employee['email'] = 'john.doe@example.com'
print("Employee Email:", employee['email'])

# Updating an existing key-value pair
employee['salary'] = 65000
print("Updated Employee Salary:", employee['salary'])

# Deleting a key-value pair
del employee['department']
print("Employee Dictionary after deleting department:", employee)

# Iterating through the dictionary
print("\nIterating through the employee dictionary:")
for key, value in employee.items():
    print(f"{key}: {value}")