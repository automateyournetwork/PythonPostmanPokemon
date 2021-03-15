# -------------------------
# Import required libraries
# -------------------------

import json
import requests

# -------------------------
# Jinja2
# -------------------------

from jinja2 import Environment, FileSystemLoader
template_dir = '../templates'
env = Environment(loader=FileSystemLoader(template_dir))

# ----------------
# Template sources
# ----------------
pokemon_info_template = env.get_template('pokemon_info_template.j2')

# -------------------------
# Prompt for Pokemon Name
# -------------------------
pokemon_name = input("Please type in the name of the Pokemon you are trying to catch:")
url_string =  'https://pokeapi.co/api/v2/pokemon/{0}'.format(pokemon_name)

print (url_string)
# -------------------------
# GET Single Pokemon 
# -------------------------
single_pokemon_results = requests.get(url_string)
if single_pokemon_results.ok:
    single_pokemon_results_json = single_pokemon_results.json()
else:
    print ('Please check the name of your Pokemon! Make sure you use lowercase letters')
    print (url_string)
    quit()

# ---------------------------------------
# Template Results
# ---------------------------------------
output_from_parsed_pokemon_info_template = pokemon_info_template.render(results=single_pokemon_results_json)

print(output_from_parsed_pokemon_info_template)

# ---------------------------------------
# Create Files
# ---------------------------------------
with open('../output/Text/{0}.txt'.format(pokemon_name), 'w') as fh:
    fh.write(output_from_parsed_pokemon_info_template)