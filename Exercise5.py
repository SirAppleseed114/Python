

# Exercise 8-3
'''
def make_shirt(size, message):
    print(f'the shirt is a size {size} and says "{message}"')

make_shirt('Medium','this is a shirt')
make_shirt(size= 'Large', message='this is also a shirt')
'''
# Exercise 8-4
'''
def make_shirt(size='Large', message='I Love Python'):
    print(f'the shirt is a size {size} and says "{message}"')
make_shirt()
'''
# Exercise 8-5
'''
def describe_city(city, country='U.S.A'):
    print(f'{city} is in {country}')
describe_city('Atlanta')
describe_city('New York')
describe_city('England','UK')
'''
# Exercise 8-6
'''
def city_country(city, country):
    print(f'{city}, {country}')
city_country('SC', 'USA')
city_country('NC','USA')
city_country('NY', 'USA')
'''
# Exercise 8-7
'''
def make_album(name, artist, number_of_songs=None):
    album = {name: artist}
    if number_of_songs:
        album['num_of_songs'] = number_of_songs

    return album
VHI = make_album(name='Van Halen I',artist='Eddie Van Halen',number_of_songs=11)
print(VHI)
'''
# Exercise 8-8
'''
def make_album(name, artist, number_of_songs=None):
    album = {name: artist}
    if number_of_songs:
        album['num_of_songs'] = number_of_songs

    return album
print('Welcome to Album maker\n type "quit" to exit')
quit = False
while quit == False:

    artist = input('what is your artists name: ')
    if artist == 'quit':
        quit = True
        exit()
    album = input('what is your artists album: ')
    if album == 'quit':
        quit = True
        exit()
    num_songs = input('what is your albums number of songs: ')
    if num_songs == 'quit':
        quit = True
        exit()
    break
created_album = make_album(name=album, artist=artist, number_of_songs=num_songs)
print(created_album)
'''
# Exercise 8-9
'''
def show_messages():
    print(messages)

messages = ['this is a message', 'this massage got hacked bet you cant figure it out first try ->',
'aopz tlzzhnl pz pu jhlzhy jpwoly olol ohoh... ila fvb kpkua kljyfwa pa aovbno, doha h zohtl ☹️']
show_messages()
'''
# Exercise 8-10
'''
def send_messages():
    print(messages)
    sent_masseages.append(messages)
messages = ['this is a message', 'no hacked messages this time', 'zeej ...detpyrcne ton ees']
sent_masseages = []
'''
# Exercise 8-11
'''
def show_messages():
    print(messages)

messages = ['this is a message', 'this massage got hacked bet you cant figure it out first try ->',
'aopz tlzzhnl pz pu jhlzhy jpwoly olol ohoh... ila fvb kpkua kljyfwa pa aovbno, doha h zohtl ☹️']
show_messages()

def send_messages():
    print(messages)
    sent_masseages.append(messages)
messages = ['this is a message', 'no hacked messages this time', 'zeej ...detpyrcne ton ees']
sent_masseages = []
'''
# Exercise 8-12
'''
toppings = ('tomato', 'cheese', 'pickles', 'lettuce','no toppings')
sand_types = ('ham','roast beef','veggie', 'PB&J')
def make_sandwich():
    print('welcome to the sandwich shop\n')
    choice = input(f'choose a sandwich\n {sand_types}: ')
    top_choice = input(f'choose your toppings\n {toppings}: ')
    print(f'your sandwich is a {choice} with {top_choice} on it')

make_sandwich()
'''
# Exercise 8-13
'''
def build_profile(first, last, **user_info):
    user_info['first name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Zach', 'Seiter', Phone='8675309',address='your moms house', SSN='123456')

print(user_profile)
'''
# Exercise 8-14
'''
def car(manufacturer,model,**car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
car_description = car('suburu','outback',color='blue',tow_package=True)
print(car_description)
'''
# Exercise 8-15 is in printing_models.py
# Exercise 8-16
'''
from printing_models import print_an_int
print_an_int()
'''
# Exercise 8-17
"""
def build_profile(first, last, **user_info):
    '''Builds a profile for a user'''
    user_info['first name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Zach', 'Seiter', Phone='8675309',address='your moms house', SSN='123456')

def car(manufacturer,model,**car_info):
    '''builds a car by manufacturer and model'''
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
car_description = car('suburu','outback',color='blue',tow_package=True)


toppings = ('tomato', 'cheese', 'pickles', 'lettuce','no toppings')
sand_types = ('ham','roast beef','veggie', 'PB&J')
def make_sandwich():
    '''builds a sandwich based ona  list of toppings'''
    print('welcome to the sandwich shop\n')
    choice = input(f'choose a sandwich\n {sand_types}: ')
    top_choice = input(f'choose your toppings\n {toppings}: ')
    print(f'your sandwich is a {choice} with {top_choice} on it')
"""