count=0 
while True: 
 print(count)
 count+=1
 if(count>30):
  break
  
''' using continue'''
for a in range(1,30):
 if(a%2==0):
   print(a)
 continue
       