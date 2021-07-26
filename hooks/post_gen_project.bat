@echo First commit
git add -A && git commit -m "Initial commit"

@echo Setting up python3 virtual environment (venv)...
python -m venv venv

@echo Installing the project and required packages in the activated virtual environment...
cmd /k "call venv\Scripts\activate.bat & python -m pip install -U pip setuptools wheel & python -m pip install -e "".[dev]"" & pre-commit install"
