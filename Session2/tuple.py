#tuple and list are one and same but tuple is immutable

tuple1=(34,53,56,334,37,23,41,56,100,500,43,53,535,345,3535)

#tuple1[0]=100 #error
for x in tuple1:
    print(f"{x} ",end="")

print()
#slicing
print(tuple1[:5])