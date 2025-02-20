listx=[34,53,56,334,37,23,41,56]
listx.append(500)
listx.insert(2,100)
listx.remove(56)
del listx[0]

listx.sort()

for x in listx:
    print(f"{x} ",end="")
print()
listx.sort(reverse=True)
for x in listx:
    print(f"{x} ",end="")