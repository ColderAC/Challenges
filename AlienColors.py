# Practicing if statements

alien_color = 'green'
if alien_color == 'green':
    print("Player just eanred 5 points")
if alien_color == 'red':
    print("Nothing happens")



alien_color = 'yellow'
if alien_color == 'green':
    print("player earned 5 points")
if alien_color == 'yellow':
    print("Player eanred 10 points")

alien_color = 'red'
if alien_color == 'green':
    print("Player eanred 5 points")
else:
    print("Player earned 10 points")

alien_color = 'green'
if alien_color == 'green':
    print("Player earned 5 poins")
elif alien_color == 'yellow':
    print("Player earned 10 points")
else:
    print("Player earned 15 points")    

age = 20
if age < 2:
    print("This person is a baby")
elif age >= 2 and age < 4:
    print("This person is a toddler")
elif age >= 4 and age < 13:
    print("This person is a kid")
elif age >= 13 and age < 20:
    print("This person is a teenager")
elif age >= 20 and age < 65:
    print("This person is an adult")
else:
    print("This person is an elder")




favorite_fruits = ['grapes', 'cherries', 'orange']
if 'apples' in favorite_fruits:
    print("You like Apples")
if 'bananas' in favorite_fruits:
    print("You like bananas")
if 'blueberries' in favorite_fruits:
    print("You Like blueberries")
if 'rasberries' in favorite_fruits:
    print("You like raspberries")
if 'watermelon' in favorite_fruits:
    print("You like watermelon")       
if 'cherries' in favorite_fruits:
    print("You like cherries")


