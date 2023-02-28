#nested loop:if and another if condition is the nested loop we can combine the nested loop as a single form
#logical conditions:AND,OR,NOT using nested if else form
num=int(input("Enter the number:"))
print(str(num))
#we can write the nested loop in single form 
if num>99 and num>100:
    if num%2==0:
 #if num>99 and num>100 and num%2==0: or 99>num>100
        print(str(num) +" is a three digit even number")
else:
         print(str(num)+ " is not a three digit even number")
         
#using or condition 
name="Yuvi"
if name[1]=='U' or name[1]=='u':
    print("The letter has been used")
else:
    print("The letter has not usef")
