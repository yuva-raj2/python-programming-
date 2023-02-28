#operator in python I'm going to do some operator in python
#Logical Operator
#In And operator both true means true otherwise it returns false
#In Or operator both false means false otherwise it returns true
#Xor operation performs both true and both false means false otherwise it returns true

x=True;
y=False;
print("x and y=",x & y)
print("x or y=",x|y)
print('x xor y=',x^y)
print('not x=',not x)
print('not y=',not y)
num1=2; #010
num2=4; #100
#Bitwise operator
print("Bitwise operator of num1 and num2=",num1&num2)
print('Bitwise operator of num1 or num2=',num1|num2)
print('Bitwise operator of num1 xor num2=',num1^num2)
#Shift operator
#It will shift the operator from right shift to left shift Left shift will move the operator to move 1 or more bits based on the value.Right shift opertor will move rightwards.
print("Num1 right shift by 1",num1>>1)
print("Num2 left shift by 8",num2<<8)
#Data types 
#Immutable data types
#String
str1="Yuvaraj"
str2="Rajan"
#concatenation
print(str1+" "+str2)
#STRING SLICING
print(str2[4])
print(str1[-3])
print(str2[2:-2])
print(str1[0:4])
print(str2[:5])
print(str2[::4])
print(str1[0:2:6])
#String slicing using find(),replace(),split(),count()
str="P.y.d.r.o.i.d"
print(str1.find('a'))
print(str2.find('Raj'))
print(str1.replace('araj','i'))
print(str2.replace("n",''))
print(str.split("."))
print(str1.count('a',0,5))
#here it will print 0 because it is case sensitive
print(str2.count('r'))
print(str2.count('R'))
#Repetition
print(str1*2)
print(str2*8)
#Immutable data types
#Strings
#TYPE specific method
print(str1.upper())
print(str2.upper())
print(str1.lower())
print(str2.lower())
print(str1.isalpha())
print(str2.isalpha())
print(max(str1))
print(max(str2))
print(min(str1))
print(min(str2))

#Immutable data types 
#Tuples
#SEQUENCE OPERATIONS
#Concatenation
tuple=('Yuvi','Kanna','Sunil','Srivarshan','Narendar','Deepack','Veera','Vashid')
print(tuple)
print(tuple+('Vigneshwaran','Sandy'))
#Repetition
print(tuple*9)
#Slicing
print(tuple[0:7])
print(tuple[-3])
#Since it will print till end it is the condition for slicing
print(tuple[1:9])
#indexing
print(tuple[3])
#DATA TYPES
#IMMUTABLE Data types
#List
#Concatenation
list=['Apple','Orange','Grape','Mango']
print(list)
print(list+['Pomegranate'])
#Repetition
print(list*9)
#Slicing
print(list[0:3])
print(list[-2])
print(list[1:5])
#Indexing
print(list[3])
print(list[-2])
#Append append(values)
my_list=['a','c','d','e','g']
my_list.append('f')
print(my_list)
#Extend extend(list)
my_list.extend(['fruit',5])
print(my_list)
#pop pop()
my_list.pop()
print(my_list)
#insert insert(index,value)
my_list.insert(-1,'h')
my_list.insert(4,'yuvi')
print(my_list)
#Data types
#Immutable data types 
#Dictionary
#Dictionary with index key
my_dict={1:'apple',2:'orange'}
print(my_dict)
#dictionary with mixed keys
dictionary={'name':'yuvi',2:['mangoose','tiger']}
print(dictionary)
#from sequence having item as a pair
dict={(1,'first'),(3,'third')}
print(dict)
#accessing the dictionary
dic={1:'Lemon',2:'Pineapple',3:'Orange'}
print(dic[3])
#len 
print(len(dic))
#values
print(dic.values())

#compound operator
a=10
a+=1
print(a)
a-=2
print(a)
a*=13
print(a)
a%=21
print(a)
a/=2
print(a)
a==5
print(a)