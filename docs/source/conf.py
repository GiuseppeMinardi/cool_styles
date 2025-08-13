import sys
import tomllib
from pathlib import Path

root_folder =  Path(__file__).parents[2]
sys.path.append(root_folder.joinpath("src"))

def parse_pyproject(root_path: Path):
    pyproject_path = root_path.joinpath("pyproject.toml")
    with pyproject_path.open("rb") as tml_file:
        toml_content = tomllib.load(tml_file)
    return toml_content.get("project")
    

pyproject_toml = parse_pyproject(root_folder)

project = pyproject_toml.get("name")
copyright = "2025, Giuseppe Minardi"
author = ", ".join(
    [
        author.get("name", "") for author in
        pyproject_toml.get("authors", [{}])
    ]
)
release = pyproject_toml.get("version")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
