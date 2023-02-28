class User:
 users=0
 def __init__(self,username,pwd): #internal variables and methods
    self.username=username
    self.pwd=pwd
    User.users+=1
 def register(self):
    print("Registering "+self.username)
 def login(self):
    print("Logging in "+ self.username)
    