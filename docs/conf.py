project = "Informator"
author = "Informator"
language = "cs"

extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "AGENTS.md"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_js_files = ["js/interactions.js"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
]

nb_execution_mode = "off"
