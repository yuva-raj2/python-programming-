#tuple:collection of data which is grouped together and it is unchangeable
variables=("Hello",43,"Jack")
print(variables)
print(type(variables))
print(variables.count(43))
print(variables.index("Jack"))
for x in variables:
	print(x)
if "Hello" in variables:
    print("Hi Yuvi")