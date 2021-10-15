import os

print("First commit")
os.system('git add -A && git commit -m "Initial commit"')

# print("Setting up conda virtual environment...")
# os.system("conda env create --prefix env --file environment.yml")

# print("Installing the project and required packages in the activated virtual environment...")
# os.system("bash -c 'conda activate ./env & python -m pip install -U pip setuptools wheel & python -m pip install -e "".[dev]"" & pre-commit install'")
