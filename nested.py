#nested loop:The inner loop will finish all of its iteration before finishing one iteration of the outer loop
a=int(input("How many rows? "))
b=int(input("How many columns?"))
c=input("Enter the symbols to write ")
for i in range(a):
  for j in range(b):
	      print(c,end="")
  print()