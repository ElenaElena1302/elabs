from operator import indexOf
from struct import unpack
class UserAccaaunt:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    def set_password(self,new_password):
        if new_password:
            self.password = new_password
        else:
            print("Enter smth")
    def check_password(self,password):
        if password:
             return self.password == password
user = UserAccaaunt("Elana", "elana.iliesku@gmail.com", "snaiper")
user.set_password("S")
print(user.check_password("snaiper")) # first password
print(user.check_password("S")) # new password