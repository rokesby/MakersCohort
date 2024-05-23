my_passwords = [
    {'service':'acebook',   'password':'password123',   'added_on': '22/03/22'},
    {'service':'makersbnb', 'password':'qwerty789',     'added_on': '22/03/22'},
    {'service':'linkedIn',  'password':'ßasdf7777',     'added_on': '21/03/22'},
]

# For loop method
def find_acebook(passwords):
    for password in passwords:
        if password['service'] == 'acebook':
            return password

print("For loop: ", find_acebook(my_passwords))
# __________________________________________________


def are_all_passwords_long_enough(passwords):
    for password in passwords:
        if len(password['password']) < 8:
            return False
    return True


print("Passwords long enough 1: ", are_all_passwords_long_enough(my_passwords))
# __________________________________________________

# Filter method.
def is_too_short(password):
    return len(password['password']) < 8

def are_all_passwords_long_enough_2(passwords):
    return len(
        list(
            filter(
                is_too_short,
                passwords
            )
        )
    ) == 0


print("Passwords long enough 2: ", are_all_passwords_long_enough_2(my_passwords))
# __________________________________________________


def are_all_passwords_long_enough_21(passwords):
    return list(
        filter(
            lambda password: len(password['password']) < 8,
            passwords
        )
    ) == []

print("Passwords long enough 2.1: ", are_all_passwords_long_enough_21(my_passwords))
# __________________________________________________


def are_all_passwords_long_enough_3(passwords):
    return len(
        [ 
            password
            for password
            in passwords
            if len(password['password']) < 8
        ]
    ) == 0
print("Passwords long enough 3: ", are_all_passwords_long_enough_3(my_passwords))
# __________________________________________________


# Exercise - check to see if any passwords were added on a specific date.
SELECTION_DATE = '21/03/22'

def is_added_on_date(passwords):
    return len(
        [
            password
            for password
            in passwords
            if password['added_on']==SELECTION_DATE
        ]
    ) !=0

print("Passwords added on this date: ", SELECTION_DATE, " - ", is_added_on_date(my_passwords))


# Exercise - Return a list of passwords which were added on a specific date.
def added_on_date(passwords):
    return filter (
        lambda password: password['added_on']==SELECTION_DATE,
        passwords    
    )


print("List of passwords added on this date: ", SELECTION_DATE, " - ")
my_list = list(added_on_date(my_passwords))
print(my_list)


# Map function
result = map(lambda number: number*2, [1,2,3,4])
print("Map function - ", list(result))

# As above but with list comprehensions.
print("List iterator - ", [number * 2 for number in [10,20,30,40]])

test_words = ['one', 'two', 'three', 'four']
for word in test_words:
    if word.startswith('t'):
        print ("Starts with match", word)