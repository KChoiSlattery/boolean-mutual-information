# boolean-mutual-information

Probably the worst way to make $100.

## Usage

### Set up to run notebooks or development

A Virtual Environment can be set up using either uv or venv. The venv module is
built into most Python installations, so should not require additional
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
- In the repository folder, run `pdoc ./boolean_mutual_information --math -o ./docs`
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
