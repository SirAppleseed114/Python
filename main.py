# This is a program to store new vehicle inventory and assist with monthly payments

# Create variable of your favorite car brand

brand='Lamborghini'

# Create list of 5 of their models from cheapest to most expensive

models = ['Hurrican','Aventador','Diablo','Urus','Sian']

# Append a 6th model to the list

models.append('Veneno')

# Create list of 5 standard colors for all models

colors = ['Red','Green','Blue','Orange','Yellow']

# Replace your last color with a different color
colors[4] = 'blue'

# Create variable of the current new year models
newmodels = ['COUNTACH LPI 800-4', 'SIÁN ROADSTER', 'SIÁN FKP 37']

# Create MSRP constant number (not string) of each of the models

NEWMSRP = [2_600_000, 3_700_000, 3_700_000]

# Create a constant number (not string) for total months in 4yr, 5yr, and 6yr loans

YEARLOANS = [4,5,6]

# Create a variable for the guest's name. Be courteous in your upcoming messages :)

guest = 'billybobjoe'

#Create message variable (with f-string) welcoming customer to your new car store

message = f'welcome {guest} to Atlanta Georgias Lamborghini dealership'

# Create awesome banner with your brand/name/dealership, however you want to welcome customers

banner = '''


$$\                              $$\                                     $$\       $$\           $$\        $$$$$$\ $$$$$$$$\ $$\       
$$ |                             $$ |                                    $$ |      \__|          \__|      $$  __$$\\__$$  __|$$ |      
$$ |      $$$$$$\  $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\  $$\ $$$$$$$\  $$\       $$ /  $$ |  $$ |   $$ |      
$$ |      \____$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ |$$  __$$\ $$ |      $$$$$$$$ |  $$ |   $$ |      
$$ |      $$$$$$$ |$$ / $$ / $$ |$$ |  $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |      $$  __$$ |  $$ |   $$ |      
$$ |     $$  __$$ |$$ | $$ | $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |      $$ |  $$ |  $$ |   $$ |      
$$$$$$$$\\\$$$$$$$ |$$ | $$ | $$ |$$$$$$$  |\$$$$$$  |$$ |      \$$$$$$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |      $$ |  $$ |  $$ |   $$$$$$$$\ 
\________|\_______|\__| \__| \__|\_______/  \______/ \__|       \____$$ |\__|  \__|\__|\__|  \__|\__|      \__|  \__|  \__|   \________|
                                                               $$\   $$ |                                                               
                                                               \$$$$$$  |                                                               
                                                                \______/                                                                

                              _.-="_-         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [w] : /        \ : |========================|    : /        \ :  [w] :
V___________:|          |: |========================|    :|          |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"


'''
# Print awesome banner and welcome message

print(banner)
print(message)

# Using title methods, print the number vehicles in alphabetical order, with the year and available colors.
models.sort()
colors.sort()
print(models)
print(colors)

# Create a variable that calculates a monthly payment (no interest) for 5yr/60months for the first vehicle
import math

loanyears = YEARLOANS[1]
monthlypayment = NEWMSRP[0] / loanyears * 12

# and print that in a nice, kind message. Don't be rude/pushy to the customer :)

print(f'Your monthly payment is {monthlypayment.__ceil__()} every month for {loanyears} years.')

# Do the same thing, but give them 4yr and 6yr options for the same vehicle

#4 year loan
loanyears = YEARLOANS[0]
monthlypayment =NEWMSRP[0] / loanyears * 12
print(f'Alternativly, a {loanyears} year loan would be {monthlypayment.__ceil__()} every month for {loanyears} years.')

#6 year loan
loanyears = YEARLOANS[2]
monthlypayment = NEWMSRP[0] / loanyears * 12
print(f'Lastly a {loanyears} year loan would cost {monthlypayment.__ceil__()}.')

# Lastly, give them a 5yr option for each of the other vehicles, just to see if they are interested

#Both the Roadster and FKP have the same price

#Roadster
loanyears = YEARLOANS[1]
monthlypayment = NEWMSRP[1] / loanyears * 12
print(f'Your monthly payment is {monthlypayment.__ceil__()} every month for {loanyears} years.')
#FKP
loanyears = YEARLOANS[1]
monthlypayment = NEWMSRP[2] / loanyears * 12
print(f'Your monthly payment is {monthlypayment.__ceil__()} every month for {loanyears} years.')

