#Create a dictionary on a person

zach = {'f_name': 'zach', 'l_name': 'seiter', 'age': 20, 'hometown': 'simpsonville', 'current_city': 'simpsonville', 'username': 'siraples33d'}
print(zach)
print(zach.values())

print(f'This user\'s first name is {zach["f_name"]}, last name is {zach["l_name"]}, and their username is {zach["username"]}')
print(f'We will ask for users hometown, which is {zach["hometown"]}')

definitions = {'python': 'the language that ths program is written in',
               'variable': 'is a changeable value defined in programming',
               'list': 'a list of values that can be looped through',
               'method': 'a python method is a label that you can call on an object; it is a piece of code to execute on that object.',
               'if_statement': 'a block of code that executes based on somthing else',
               'dictionary': 'a list of keys associated with values',
               'function': 'a block of code that runs when called'}

print(f'python \n{definitions["python"]}')
print(f'variable \n{definitions["variable"]}')
print(f'list \n{definitions["list"]}')
print(f'method \n{definitions["method"]}')
print(f'If Statement \n{definitions["if_statement"]}')
print(f'dictionary \n{definitions["dictionary"]}')
print(f'function \n{definitions["function"]}\n')

for key, value in definitions.items():
    print(f'{key}: {value} \n')

counties = {'sumter': 'sumter', 'union': 'union', 'oconee': 'wallhalla', 'richland': 'columbia', 'marlboro': 'bennetsville', 'spartanburgh': 'spartanburgh'}

other_counties = ['sumter', 'union', 'oconee', 'richland', 'marlboro', 'marion', 'calhoun', 'colleton', 'dillion', 'darlington']

for county in other_counties:
    if county in counties:
        print(f'{county} is in our directory, the capital is {counties[county]}\n')
    else: print(f'{county} is not in our dictionary. We will add this county shortly. Thanks!\n')

spartanburgh = ['campobello', 'cowpens', 'woodruff', 'spartanburgh', 'chesnee', 'landrum']

for city in spartanburgh:
    if city not in counties.keys():
        print(f'{city} is not a capital of any South Carolina county\n')
    else: print(f'{city} is a capital of a South Carolina county\n')

sc_counties = {'charleston': ['awendaw', 'folly beach', 'hollywood'],
'richland': ['arcadia', 'blythwood', 'neeses'],
'orangeburgh': ['bowman', 'cordova', 'hollywood'],
'pickens': ['central', 'clemson', 'easley'],
'laurens': ['clinton', 'fountian inn', 'waterloo']}

for key, value in sc_counties.items():
    print(f'the three biggest cities in {key} are {value}')

name = input('what is your name?: ')
print(f'hello {name}, welcome to AU')

money = input('a little bird said you need a processor... how much dough you got: ')
i3 = 700
i5 = 1000
i7 = 1300
i9 = 2000

money_int = int(money)

if money_int < i3:
    print('you do not have enough dough come back when your a little mmmmmmmmmmmm richer')
elif i3 <= money_int < i5:
    print(f'you can buy an i3 processor... chump')
elif i5 <= money_int < i7:
    print(f'you can buy an i5 processor... nerd')
elif i7 <= money_int < i9:
    print(f'you can buy an i7 processor... freakazoid')
elif money_int >= i9:
    print(f'you can buy an i9 processor... dweeb')

integer = input('give me an integer or else...: ')

while integer != 'or else what':
    integer_num = int(integer)
    if integer_num % 2 == 0:
        print(f'the integer {integer_num} is even')
        integer = input('give me an integer or else...: ')

    else:
        print(f'the integer {integer_num} is odd')
        integer = input('give me an integer or else...: ')


fav_num = input('guess my favorite number: ')
fav_num = int(fav_num)

while fav_num in range(0, 9999999999999999999999999999):
    if fav_num == 14:
        print('you win')
        exit()
    else:
        print('wrong... you loose')
        fav_num = input('guess my favorite number: ')
        fav_num = int(fav_num)

responses = {}
choices = ['Kubuntu','Lubuntu','Ubuntu Budgie','Ubuntu Kylin','Ubuntu MATE','Ubuntu Studio','Xubuntu']
polling_active = True

while polling_active:
    name = input('what is your name: ')
    vote = input('what is you ubuntu flavor of choice: ')
    responses[name] = vote
    repeat = input('is there another user to vote y/n: ')
    if repeat == 'n':
        polling_active = False
print('poll results')
for name, response in responses.items():
    print(f'{name} uses {response}')

