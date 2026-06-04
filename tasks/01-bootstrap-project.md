# Úkol 01: Vytvoření základního projektu Informator

## Cíl

Vytvoř minimální funkční prototyp elektronické učebnice informatiky pro střední školu.

Projekt se jmenuje Informator.

## Požadovaná struktura

Vytvoř tuto strukturu:

```text
informator/
├── AGENTS.md
├── README.md
├── .gitignore
├── .readthedocs.yaml
├── docs/
│   ├── AGENTS.md
│   ├── conf.py
│   ├── requirements.txt
│   ├── index.md
│   ├── _static/
│   │   ├── css/custom.css
│   │   ├── js/interactions.js
│   │   ├── images/
│   │   └── slides/
│   ├── _templates/
│   │   └── chapter-template.md
│   ├── metodika/
│   │   └── index.md
│   ├── 01-zaklady-informatiky/
│   │   ├── index.md
│   ├── 02-programy-a-data/
│   │   └── index.md
│   ├── 03-informacni-a-databazove-systemy/
│   │   └── index.md
│   ├── 04-rastrova-grafika-a-digitalni-fotografie/
│   │   └── index.md
│   ├── 05-vektorova-grafika/
│   │   └── index.md
│   ├── 06-zpracovani-textu-na-pocitaci/
│   │   └── index.md
│   ├── 07-tabulkove-procesory/
│   │   └── index.md
│   ├── 08-pocitacove-zpracovani-zvuku/
│   │   └── index.md
│   ├── 09-digitalni-video-a-multimedialni-prezentace/
│   │   └── index.md
│   ├── 10-relacni-databaze-a-SQL/
│   │   └── index.md
│   ├── 11-internet-a-www/
│   │   └── index.md
│   ├── 12-html-a-kaskadove-styly/
│   │   └── index.md
│   ├── 13-webove-technologie/
│   │   └── index.md
│   ├── 14-webove-aplikace/
│   │   └── index.md
│   ├── 15-kyberbezpecnost/
│   │   └── index.md
│   ├── 16-zaklady-programovani-a-algoritmizace/
│   │   └── index.md
│   │   └── algoritmus.md
│   ├── 17-vyvojarske-nastroje-a-verzovaci-systemy/
│   │   └── index.md
│   ├── 18-strukturovane-programovani/
│   │   └── index.md
│   ├── 19-objektove-orienatovane-programovani/
│   │   └── index.md
│   └── 20-datove-struktury-a-soubory/
│       └── index.md

└── notebooks/
    └── AGENTS.md
````

## Technologické požadavky

Použij:

* Sphinx,
* MyST Markdown,
* myst-nb,
* sphinx-design,
* sphinx-togglebutton,
* sphinx-copybutton,
* sphinxcontrib-mermaid,
* pydata-sphinx-theme.

## Konfigurace

Vytvoř `.readthedocs.yaml` pro build přes Read the Docs.

Vytvoř `docs/conf.py` pro Sphinx.

Vytvoř `docs/requirements.txt` se všemi potřebnými závislostmi.

## Obsah ukázkové kapitoly

Soubor `docs/16-zaklady-algoritmizace-a-programovani/algoritmus.md` musí obsahovat:

* název kapitoly,
* krátký úvod,
* výukové cíle,
* základní pojmy,
* výklad pojmu algoritmus,
* ukázku v Pythonu,
* jednoduchý Mermaid diagram,
* cvičení,
* rozbalovací nápovědu,
* rozbalovací řešení,
* shrnutí,
* kontrolní otázky.

## Navigace

Všechny vytvořené sekce zapoj do Sphinx navigace pomocí `toctree`.

## Ověření

Po dokončení spusť:

```bash
python -m pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

Pokud build selže, oprav chyby.

## Výstup

Na konci uveď:

* seznam vytvořených nebo změněných souborů,
* stručné shrnutí,
* výsledek buildu,
* případné známé problémy.

