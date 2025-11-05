# boolean-mutual-information

Template for initializing a pure Python project with several features.

## Core features

- Framework for local module that can be easily imported from another project
- Virtual environment
- Documentation generation
- Unit testing
- Extremely flat folder structure
- Jupyter notebooks get automatically cleaned (metadata removed) on commit

Everything below this line of the readme is intended to be included in the actual repository, with 'boolean-mutual-information' replaced with the actual name of the repository. In addition, 'boolean-mutual-information' should be changed to the new name in "pyproject.toml" and the name of the "python_template_repo" folder.

## API Documentation

Automatically-generated documentation is available at <https://github.gatech.edu/pages/kchoislattery3/boolean-mutual-information>.

## Usage

### Set up to run notebooks or development

A Virtual Environment can be set up using either uv or venv. The venv module is
built into most Python installations, so should require not additional
installations, but uv is generally faster to install packages and has some other
benefits.

#### Using venv

- Create the Python virtual environment (venv): `py -3.13 -m venv .venv`
- Activate the venv: varies by OS
  - Windows: `.venv\Scripts\activate.bat`
  - Linux and MacOS: `source .venv/bin/activate`
- Install requirements to the venv: `pip install -r requirements.txt`
- Set up the automatic notebook cleaning: `pre-commit install`

#### Using uv (optional)

- Create the virtual environment: `uv venv --python 3.13`
- Activate the virtual environment: `.venv\Scripts\activate`
- Install requirements: `uv pip sync requirements.txt`
- Set up the automatic notebook cleaning: `pre-commit install`

## Developer instructions

### Generating documentation

- Delete the "docs" folder
- In the repository folder, run `pdoc ./aerosol_inversion --math -o ./docs`
- Read generated documentation by starting a live server starting from "docs/index.html"
- When pushed, GitHub automatically updates the hosted documentation. This can be
  configured in "settings>Pages" on the GitHub website.

### Changing the virtual environment

- Make desired modifications to "requirements.in"
- With the venv still activated, compile "requirements.in":
  - uv: `uv pip compile requirements.in > requirements.txt`
  - pip-tools: `pip-compile requirements.in`
- Update the venv: `pip-sync requirements.txt`

### Other miscellaneous commands

- Run all tests (from the tests folder and from the docstrings): `pytest tests/ && xdoctest boolean_mutual_information`
- Clean notebooks (this is also done automatically when the repository is pushed): `nb-clean clean . --preserve-cell-outputs`

### Release checklist

- The requirements and active venv have been updated
- Docs have been made
- Tests have been run
- Notebooks have been run
