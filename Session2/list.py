listx=[34,53,56,334,37,23,41,56]



# Accessing list elements
print(listx[0])
print(listx[1])
print(listx[3])
print(listx[-1]) # negative index
print(listx[-2]) # negative index

listx[0]=100

for x in listx:
    print(f"{x} ",end="")
print()
for i in range(len(listx)):
    print(f"{i} -> {listx[i]}",end=" ")
# List can have different types of data
# List has index starting from 0
# List is mutable
# List is ordered
# List can have duplicate values
# List can have nested list
# List can have empty values (None)