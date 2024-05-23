passwords = [
    {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
    {'service': 'acebook', 'password': 'qwerty789', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
]

def is_acebook(password):
    return password['service'] == 'acebook'

# print(
#     next(
#         filter(
#             is_acebook, passwords
#             )
#         )
#       )

print("Passwords: :", passwords)

print("Filtered iterator : ")

print(
    list(
        filter(
            is_acebook, passwords
        )
    )
)



# {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'}
