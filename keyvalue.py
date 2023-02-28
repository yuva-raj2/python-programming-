#dictionary_pair of key values
#key:value
user={'Name':'Yuvi','Age':'20','Gender':'Male','Dept':'CSE'}
print(user)
#add the dictionary
user['Place']='Valparai'
print(user)
#modify the dictionary
user["Age"]='21'
print(user)
#delete the dictionary
del user['Dept']
print(user)
#To sort the dictionary jn orderwise
for key,val in user.items():
    print('key:'+key)
    print('val:'+val)
for key in user.items():
    print(key)
for val in user.items():
    print(val)
for key in user.keys():
    print(key)
for key in sorted(user.keys()):
    print(user[key])