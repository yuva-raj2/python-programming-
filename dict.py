#dictionary:A changeable,unordered collection of unique key value pairs.Fast because they use hashing allow us to access a value quickly
capital={'USA':'Washington D.C','India':'NewDelhi','China':'Beiging','Russia':'Moscow'}
print(capital)
print(type(capital))
print(capital['Russia'])
print(capital.keys())
print(capital.values())
print(capital.items())
print(capital.get("Germany"))