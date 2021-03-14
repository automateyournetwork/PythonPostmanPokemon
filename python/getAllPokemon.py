# -------------------------
# Import required libraries
# -------------------------

import json
import requests
import pprint

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
all_pokemon_results = requests.post('https://pokeapi.co/api/v2/pokemon?limit=1200'

# ---------------------------------------
# Template Results
# ---------------------------------------
output_from_parsed_all_pokemon_template = all_pokemon_template.render(results=all_pokemon_results['results'])

pprint.pprint(output_from_parsed_all_pokemon_template)