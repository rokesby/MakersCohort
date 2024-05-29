# Kata Session 1

passwords = [
    {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
    {'service': 'acebook', 'password': 'qwerty789', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
]

def is_acebook(password):
    return password['service'] == 'acebook'

# print("Passwords: :", passwords)
# print("Filtered iterator : ")

# print(
#     list(
#         filter(
#             is_acebook, passwords
#         )
#     )
# )

# Kata Session 2
# Code wars
# https://www.codewars.com/kata/585eaef9851516fcae00004d


def what_list_am_i_on(actions):

    naughty_count = 0
    nice_count = 0

    # Check the first character in each word.
    for word in actions:
        if (word[0] == 'b') or (word[0] == 'f') or (word[0] == 'k'):
            # This is naughty
            naughty_count +=1
        if (word[0] == 'g') or (word[0] == 's') or (word[0] == 'n'):
            # This is naughty
            nice_count +=1   

    if naughty_count >= nice_count:
        return 'naughty'
    else:
        return 'nice'

print ("Kata : " , what_list_am_i_on(['broke someone\'s window', 'fought over a toaster', 'killed a bug']))
print ("Kata : " , what_list_am_i_on(['got someone a new car', 'saved a man from drowning', 'never got into a fight']))
print ("Kata : " , what_list_am_i_on( ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']))
