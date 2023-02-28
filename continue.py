#continue=continues till the next iterations
#Remove , string
str="A,R,U,N"
str1=" "
for i in str:
    if i==',':
        continue
    str1=str1+i
print(str1)