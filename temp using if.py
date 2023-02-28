#logical operators (and,or,not): used to check if two or more conditions are true
temp=int(input("What is the temperature today? "))
print(temp)
#In and operator both the condition should be true
if temp>=0 and temp<=30:
	print("The temperature is Good")
	print("You can go outside")
#In or operator atleast one of the condition to be true otherwise false
elif  temp<=0 or temp>=30:
	print("The temperature is very bad")
	print("You should not go outside")
	
