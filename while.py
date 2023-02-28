#while loop:A statement will execute its block of code as long as the condition remains true
name=""
while len(name)==0:
	name=input("Enter your name: ")
print("Hello "+name)
#both the condition will give the same output in while condition 
name=None
while not name:
	name=input("Enter your name:")
print("Hello "+name)