import pprint
import json
# from urllib.request import urlopen

with open("/Users/reza/Code/python_foundations/extension_challenges/02_json/program/test.json") as f:
    data = json.load(f)
#pprint.pprint(data)

# Filter the list based on a specific director.
the_director = 'Sidney Lumet'

# Filter the list for those films whose director matches.
filtered_list = [film for film in data if film['director']==the_director]
print(filtered_list)

# Now share the list of films from the dictionary structure.
# output_films = []

 # Extract film names
film_names = [film['name'] for film in filtered_list]
print(film_names)