from oop import User
username1=User("Yuvi","@2356")
username2=User("Kanna","@234")
username1.register()
print("Succesfully registered")
username1.register()
print("Successfully logged in")
print(username1.username)
print(username2.username)
print(User.users)
User.users=10
print(User.users)