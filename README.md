# ERpyEditor
The game editor for (https://github.com/Elite-Redux/eliteredux/tree/master)[Elite Redux], a game made with pokeemerald from pret decompilation project.

## Install it
1. Python 3 is required
2. pywebview needs to have its dependencies fullfilled in function of your OS
check out https://pywebview.flowrl.com/3.7/guide/installation.html#dependencies
3. install python dependencies with the requirement.txt


## Run it
```sh
python3 main.py 
# or (depends on your installation)
python main.py 
```


## Project structure
- front/
    - Holds the web based GUI as static files
    - Written in JS/HTML/CSS + Jquery and small other libraries

- back/
    - Read/Write/Parse the games code
    - Written in Python3, uses (https://pywebview.flowrl.com/3.7/guide/)[PyWebView]
    
- build.py: a future build util not yet ready

- main.py: entrypoint of the program
    
## Notes on the project

- pywebvieww Examples: https://pywebview.flowrl.com/3.7/examples/

- We're using the serverless mode of it.

- Please don't use Maj for Files.naming, i hate it, Majs are for Structure or CONSTANTS.

- for the naming convention refers to https://github.com/naming-convention/naming-convention-guides/tree/master/python.

- PEP8 could be enforced in the future.
