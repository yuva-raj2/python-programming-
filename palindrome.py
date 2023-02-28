a=input("Enter the string:")
#using slicing condition we can find the palindrome
reverse=a[::-1]
if(reverse==a):
 print("The reversed string s a palindrome")
else: 
 print("The reversed string is not a palindrome")