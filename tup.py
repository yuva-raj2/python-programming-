#tuple=inmmutable csnnot change but we can change tje entkre tuple
tuple=(3,4,7)
print(tuple)
print(tuple.index(7))
print(tuple.count(3))
for i in tuple:
    print(i)
if 3 in tuple:
     print("Yes")
else:
     print("No")
if tuple:
     print("Tuple is not empty")