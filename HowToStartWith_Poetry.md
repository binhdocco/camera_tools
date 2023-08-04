# MANAGE PYTHON MULTIPLE VERSIONS #https://github.com/pyenv-win/pyenv-win
Go to Python folder (E:\Program Files\Python)
And run the PowerShell command: 
- Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
- set PATH in global env to bin folder: C:\Users\BrayLeinoSplash\.pyenv\pyenv-win\bin
- Run pyenv install -l to check a list of Python versions supported by pyenv-win
- Run pyenv install <version> to install the supported version
- Run pyenv global <version> to set a Python version as the global version
- pyenv versions #show installed versions in pyenv

pip install opencv-python
pip install cmake
pip install dlib
pip install face_recognition

Get Started With Python Poetry
#https://realpython.com/dependency-management-python-poetry/
#https://www.youtube.com/watch?v=Ib7fNOIGM7E
#https://www.youtube.com/watch?v=0f3moPe_bhk
#https://www.youtube.com/watch?v=547Jr26duHQ #Setup VS Code for Python with Pyenv and Poetry

Get Started With Python Poetry + Flask
https://flask.palletsprojects.com/en/1.1.x/patterns/packages/#simple-packages
https://stackoverflow.com/questions/67460836/how-do-i-get-the-flask-package-tutorial-work-with-poetry?answertab=createdasc#tab-top


# Face attendance + face recognition with Python | Computer vision tutorial
https://www.youtube.com/watch?v=z_dbnYHAQYg

# Face recognition in real-time | with Opencv and Python
https://www.youtube.com/watch?v=5yPeKQzCPdI

# Solved face recognition install error | dlib install error
https://www.youtube.com/watch?v=BkTFzjFKQQU
-> install dlib manually #https://github.com/datamagic2020/Install-dlib/blob/main/dlib-19.22.99-cp310-cp310-win_amd64.whl

+ INSTALL & CREATE

- python --version
- pip install poetry
- poetry -v

- poetry env info  # view info of env
- poetry env info -p # view info of env, show path only

- poetry config --list
#if virtualenvs.in-project = null, set to true
- poetry config virtualenvs.in-project true
- poetry config virtualenvs.prefer-active-python true

===== poetry + install (RECOMMENDED)
- poetry init -n
#set python version to: python = "^3.10" #pyproject.toml

- poetry install
- poetry shell
- poetry cmake
- poetry add "E:\Projects\Python\Camera_AI\dlib\dlib-19.22.99-cp310-cp310-win_amd64.whl" #dlib
- poetry add opencv-python
- poetry add face_recognition

- pytest # run a package
- poetry add package_name
- poetry remove package_name

===== poetry + django
#1 use poetry init -n
- poetry init -n
- poetry add django   #init virtual env
#create main.py
from django import VERSION
print(VERSION)

#1_1 RUN without env
- poetry run python main.py

#1_2 RUN with env
- poetry shell
- python main.py OR 
- python -i main.py   # run in interactive mode, ctr+z OR exit() to exit interactive mode

#1_3 EXIT the active env
- exit
- deactivate

#see installed packages
- poetry show OR
- poetry show --tree

#add a new package
- poetry add requests

#remove an installed package
- poetry remove django

-----
#2 use poetry new
- poetry new project_name


+ START
poetry shell
poetry install
poetry run main.py