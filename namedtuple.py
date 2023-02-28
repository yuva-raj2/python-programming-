from collections import namedtuple
a=namedtuple("course",'name,language')
s=a('datascience','python') 
print(s)