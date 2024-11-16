# python
Contains Solutions for Python training Lessons.

## Virtual environment


```bash
# with pyenv
pyenv install 3.12.0
pyenv virtualenv 3.12.0 .env
pyenv activate .env
pyenv local .env

# with python venv
python3 -m venv .env
source .env/bin/activate

# deactivate
source deactivate
```

## pip commands

```bash
# Python version
pip3 -V

# Python libraries for the current project
pip3 freeze
pip3 freeze > requirements.txt

# Install packages
pip3 install matplotlib

```