listx=[34,53,56,334,37,23,41,56,100,500,43,53,535,345,3535]

# Slicing the list to get the first 5 elements
first_five = listx[:5]
print("First five elements:", first_five)

# Slicing the list to get the last 5 elements
last_five = listx[-5:]
print("Last five elements:", last_five)

# Slicing the list to get elements from index 3 to 8
middle_slice = listx[3:9]
print("Elements from index 3 to 8:", middle_slice)

# Slicing the list to get every second element
every_second = listx[::2]
print("Every second element:", every_second)

# Slicing the list to get elements in reverse order
reversed_list = listx[::-1]
print("Reversed list:", reversed_list)

# Slicing the list to get every second element in reverse order
every_second_reversed = listx[10:1:-2]
print("Every second element in reverse order:", every_second_reversed)