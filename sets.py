#sets:collection of unordered lists and the sets can't be repeated 
sets={"hello","yuvi",4,102,"good",102}
print(sets)
sets.add("cutty")
print(sets)
sets.remove("good")
print(sets)
dishes={"tomatorice","friedrice","cookie","good"}
dish=dishes.update(sets)
print(dishes)
print(dishes.union(sets))
print(sets.intersection(dishes))
for x in dishes:
	print(x)

