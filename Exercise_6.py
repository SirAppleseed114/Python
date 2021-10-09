# Exercise 9-1,2
'''
class Resturant:
    """A simple attempt to model a dog."""

    def __init__(self, name, type):
        """Initialize name and age attributes."""
        self.name = name
        self.type = type

    def describe_resturant(self):
        """Simulate a dog sitting in response to a command."""
        print(f"Welcome to {self.name} we serve {self.type}.")

    def open_resturant(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is now open")
Bobs = Resturant('Bobs Pizza','Pizza')
joes = Resturant('Joes Subs','Sandwiches')
Bills = Resturant('Bills Candy Store','Candy')
Johns = Resturant('Johns Grill','Steak')
Camdens = Resturant('Camdens Seafood','Seafood')

print(Bobs.open_resturant())
resturants = [Bobs,Johns,joes,Bills,Camdens]
for resturant in resturants:
    print(resturant.describe_resturant())
'''
# Exercise 9-3
'''
class User:
    """creates a user profile"""
    def __init__(self,first_name,last_name,phone,address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address

    def describe_user(self):
        """prints user info"""
        print(f'User Info\n {self.first_name}\n{self.last_name}\n{self.phone}\n{self.address}')

billy = User('bob','billy','000-867-5309','your moms house')
print(billy.describe_user())
'''
# Exercise 9-4
'''
class Resturant:
    """A simple attempt to model a dog."""

    def __init__(self, name, type, number_served):
        """Initialize name and age attributes."""
        self.name = name
        self.type = type
        self.number_served = number_served

    def describe_resturant(self):
        """Simulate a dog sitting in response to a command."""
        print(f"Welcome to {self.name} we serve {self.type}.")

    def open_resturant(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is now open")

    def set_number_served(self,served):
        self.number_served += served
Bobs = Resturant('Bobs Pizza','Pizza',0)
print(Bobs.open_resturant())
print(Bobs.describe_resturant())
Bobs.set_number_served(100)
print(f'Bobs Pizza has served {Bobs.number_served} customers')
'''
# Exercise 9-5
'''
class User:
    """creates a user profile"""
    def __init__(self,first_name,last_name,phone,address,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.login_attempts = login_attempts

    def describe_user(self):
        """prints user info"""
        print(f'User Info\n{self.first_name}\n{self.last_name}\n{self.phone}\n{self.address}\n{self.login_attempts}')

    def set_login_attempts(self, logins):
        """increases login attempts"""
        self.login_attempts += logins
    def reset_logins(self):
        """resets logins to zero"""
        self.login_attempts = 0
billy = User('bob','billy','000-867-5309','your moms house',3)
print(billy.describe_user())
billy.reset_logins()
print(billy.describe_user())
'''
# Exercise 9-6
'''
class Resturant:
    """A simple attempt to model a dog."""

    def __init__(self, name, type, number_served):
        """Initialize name and age attributes."""
        self.name = name
        self.type = type
        self.number_served = number_served

    def describe_resturant(self):
        """Simulate a dog sitting in response to a command."""
        print(f"Welcome to {self.name} we serve {self.type}.")

    def open_resturant(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is now open")

    def set_number_served(self, served):
        self.number_served += served


class Icecreamstand(Resturant):

    def __init__(self, flavors):
        """Initialize name and age attributes."""
        self.flavors = flavors

    def print_flavors(self):
        """prints flavors"""
        print(self.flavors)


bobs_icecream = Icecreamstand(flavors=['vanilla', 'chocolate', 'cherry', 'strawberry'])
Icecreamstand.print_flavors(bobs_icecream)
'''
# Exercise 9-8
'''
class User:
    """creates a user profile"""
    def __init__(self,first_name,last_name,phone,address,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.login_attempts = login_attempts

    def describe_user(self):
        """prints user info"""
        print(f'User Info\n{self.first_name}\n{self.last_name}\n{self.phone}\n{self.address}\n{self.login_attempts}')

    def set_login_attempts(self, logins):
        """increases login attempts"""
        self.login_attempts += logins
    def reset_logins(self):
        """resets logins to zero"""
        self.login_attempts = 0
class Admin:
    def __init__(self,privelages):
        self.privleges = privelages

    def show_privelages(self):
        """prints privelages"""
        print(self.privleges)

billy = User('bob','billy','000-867-5309','your moms house',3)
print(billy.describe_user())
billy.reset_logins()
print(billy.describe_user())
bob = Admin(['can delete files','can create new users', 'can reboot system'])
bob.show_privelages()
'''
# Exercise 9-9
'''
class User:
    """creates a user profile"""
    def __init__(self,first_name,last_name,phone,address,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.login_attempts = login_attempts

    def describe_user(self):
        """prints user info"""
        print(f'User Info\n{self.first_name}\n{self.last_name}\n{self.phone}\n{self.address}\n{self.login_attempts}')

    def set_login_attempts(self, logins):
        """increases login attempts"""
        self.login_attempts += logins
    def reset_logins(self):
        """resets logins to zero"""
        self.login_attempts = 0
class Admin:
    def __init__(self,privelages):
        self.privleges = privelages

class Privleges:
    def __init__(self,privelages):
        self.privleges = privelages

    def show_privelages(self):
        """prints privelages"""
        print(self.privleges)

billy = User('bob','billy','000-867-5309','your moms house',3)
print(billy.describe_user())
billy.reset_logins()
print(billy.describe_user())
bob = Privleges(['can delete files','can create new users', 'can reboot system'])
bob.show_privelages()
'''
# Exercise 9-10
'''
from resturant_module import Icecreamstand
bobs_icecream = Icecreamstand(flavors=['vanilla', 'chocolate', 'cherry', 'strawberry'])
Icecreamstand.print_flavors(bobs_icecream)
'''
# Exercise 9-11
'''
from admin_module import Privleges,User
billy = User('bob','billy','000-867-5309','your moms house',3)
print(billy.describe_user())
billy.reset_logins()
print(billy.describe_user())
bob = Privleges(['can delete files','can create new users', 'can reboot system'])
bob.show_privelages()
'''
# Exercise 9-12
'''
from admin_module import Privleges,Admin
from user_module import User
billy = User('bob','billy','000-867-5309','your moms house',3)
print(billy.describe_user())
billy.reset_logins()
print(billy.describe_user())
bob = Privleges(['can delete files','can create new users', 'can reboot system'])
bob.show_privelages()
'''
# Exercise 9-13
'''
from random import *
class Die:
    def __init__(self,side=6):
        self.side = side
    def roll_die(self) :
        print(f'your rolled number is {randint(0,10)}')

die = Die()
die.roll_die()
'''
# Exercise 9-14
'''
from random import *
numbers = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
def lottery():
    print(f'the winning code is \n{choice(numbers),choice(numbers),choice(numbers),choice(numbers),choice(numbers)}')
lottery()
'''
# Exercise 9-15
'''
from random import *
numbers = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
def lottery():
    winning_num = f'{choice(numbers),choice(numbers),choice(numbers),choice(numbers),choice(numbers)}'
    stripped_num = winning_num.rstrip()
# stripped_num = ('1','2','3','4','5') <-- garuntees win... its very difficult to win chances are slim due to each num being random
    return stripped_num

ticket = ('1','2','3','4','5')

if ticket == lottery():
    print(f'congrats you won')
while ticket != lottery():
        lottery()
        print(lottery())
'''
# Exercise 9-16
'''
# runs a simple http server in local directory
import os
command = 'sudo python3 -m http.server'
os.system(command)
'''
# Exercise 10-1 - 5
'''
import os
name = input('you are the first guest what is your name: ')
os.system(f'echo -n {name} > guest.txt')
while True:
    new_guest = input('what is your name: ')
    os.system(f'echo {new_guest} >> guest.txt')
    while True:
        opinion = input('what do you like about programming: ')
        if opinion.txt:
            os.system(f'echo {opinion} >> opinions.txt')
        else:
            os.system(f'echo {opinion} > opinions.txt')
'''
#Exercise 10-6 - 7
'''
number1 = input('what is the first number to add: ')
number2 = input('what is the second number to add: ')
while True:
    try:
        answer = int(number2) + int(number1)
    except ValueError:
        print('only imput numbers please')
        break
    else:
        print(f'then answer is {answer}')
        break
'''













