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
# GET Single Pokemon 
# -------------------------
single_pokemon_results = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')
single_pokemon_results_json = single_pokemon_results.json()

# ---------------------------------------
# Template Results
# ---------------------------------------
output_from_parsed_pokemon_info_template = pokemon_info_template.render(results=single_pokemon_results_json)

print(output_from_parsed_pokemon_info_template)