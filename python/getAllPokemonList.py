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
all_pokemon_template = env.get_template('all_pokemon_template.j2')

# -------------------------
# GET All Pokemon 
# -------------------------
all_pokemon_results = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1200')
all_pokemon_results_json = all_pokemon_results.json()

print (all_pokemon_results.content)
# ---------------------------------------
# Template Results
# ---------------------------------------
output_from_parsed_all_pokemon_template = all_pokemon_template.render(results=all_pokemon_results_json['results'])

print(output_from_parsed_all_pokemon_template)