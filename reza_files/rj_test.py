password_list = []

# new_password= {}
# new_password['service_name'] = 'Google'
# new_password['password'] = 'helloworld1'
# print("password combo : ",new_password)
# print("specific password :", new_password.get('service_name'))     
# password_list.append(new_password)


new_password= {}
new_password['service_name'] = 'acebook'
new_password['password'] = '$12345678'
password_list.append(new_password)


new_password= {}
new_password['service_name'] = 'makersbnb'
new_password['password'] = '@12345678'
password_list.append(new_password)


new_password= {}
new_password['service_name'] = 'facebook'
new_password['password'] = 'mark1234566'
password_list.append(new_password)

print("PASSWORD list - : ", password_list)


service_list = []
for count, item in enumerate(password_list):
    service_list.append(item.get('service_name'))
    print("Item number : ", count)

print("SERVICE list - : ", service_list)
service_list.sort(reverse=True)
print("SERVICE list REVERSED - : ", service_list)

print("Try to pop an item- : ")
for count, item in enumerate(password_list):
        if item.get('service_name') == 'makersbnb':
        # We have a match so remove it.
            password_list.pop(count)

print("new PASSWORD list - : ", password_list)

