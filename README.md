# PythonPostmanPokemon
Fun with the Python, Postman, and the PokeAPI

https://pokeapi.co/

Help your children learn programming with Pokemon, Postman, and Python!

## Tools:

Download VS Code to edit the files
https://code.visualstudio.com/download

Download Postman for a GUI-based API client and to install the Postman Collection
https://www.postman.com/downloads/

Download Python for Windows to run the Python code 
https://www.python.org/downloads/


### Instructions
Step 1. Create a Virtual Python Environment

Start -> Run -> cmd 

Change to the root of your C: 

```console
C:\Users\Username\

cd\

C:\ python -m venv pokemon

```

Step 2. Activate the environment

```console
.\pokemon\Scripts\activate
```

Your prompt should look like this now:

```console
(pokemon) C:\>
```

Step 3. Install the rquired libraries

```console
(pokemon) C:\>pip install requests
(pokemon) C:\>pip install jinja2
```

#### Have Fun ! 

To run the Python scripts:

Get All Pokemon List 

```console
(pokemon) C:\>{{ file location }}\python getAllPokemonList.py
```

Prints all Pokemon on the screen and creates a .txt file list (in the output folder)

Get Pokemon Info 

```console
(pokemon) C:\>{{ file location }}\python getPokemonInfo.py
Please type in the name of the Pokemon you are trying to catch: {{ type in your Pokemon's name }}
```

Prints an individual Pokemon's information to the screen and creates a .txt file of the data (in the output folder)

Create Pokemon Website

```console
(pokemon) C:\>{{ file location }}\python createPokemonWebsite.py
Please type in the name of the Pokemon you are trying to catch: {{ type in your Pokemon's name }}
```

Creates a website for the Pokemon! 



