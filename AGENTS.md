# AGENTS.md

## Projekt

Tento repozitář se jmenuje Informator.

Cílem je vytvořit elektronickou učebnici informatiky pro střední školu publikovanou pomocí Sphinxu a Read the Docs.

Učebnice má obsahovat:
- výukové texty,
- grafické prezentační snímky,
- ukázky kódu,
- diagramy,
- cvičení,
- rozbalovací nápovědy a řešení,
- jednoduché klientské interaktivní prvky,
- Jupyter notebooky jako doplňkový výukový materiál.

## Technologický základ

Používej:
- Python 3.12,
- Sphinx,
- MyST Markdown,
- myst-nb,
- sphinx-design,
- sphinx-togglebutton,
- sphinx-copybutton,
- sphinxcontrib-mermaid,
- pydata-sphinx-theme.

Nepřecházej na MkDocs, Jupyter Book ani jiný framework, pokud to není výslovně zadáno.

## Pravidla práce

Pracuj v malých, kontrolovatelných změnách.

Před větší změnou nejprve urč:
1. které soubory budeš měnit,
2. proč je budeš měnit,
3. jak ověříš výsledek.

Neměň existující obsah bez důvodu. Nepřepisuj celé soubory, pokud stačí cílená úprava.

Po každé významné změně ověř build dokumentace:

```bash
sphinx-build -b html docs docs/_build/html
````

Pokud build selže, oprav chybu před dokončením úkolu.

## Jazyk a styl

Veškeré výukové texty piš česky.

Styl má být:

* jasný,
* přesný,
* středoškolsky srozumitelný,
* odborně korektní,
* bez infantilizace,
* bez marketingového tónu.

## Struktura kapitoly

Každá výuková kapitola má mít tuto strukturu:

1. Název kapitoly.
2. Krátký úvod: proč je téma důležité.
3. Výukové cíle.
4. Základní pojmy.
5. Výklad.
6. Ukázka nebo modelová situace.
7. Ukázka kódu, pokud je vhodná.
8. Grafické shrnutí nebo diagram.
9. Cvičení.
10. Rozbalovací nápověda.
11. Rozbalovací řešení.
12. Shrnutí.
13. Kontrolní otázky.

Nepřidávej dlouhé textové bloky bez členění.

## Interaktivita

Interaktivita musí být statická a bezpečná.

Povoleno:

* klientský JavaScript,
* vstupní pole,
* okamžitá zpětná vazba,
* localStorage,
* jednoduché simulace,
* odkazy do Colabu nebo Binderu,
* notebooky jako staticky vykreslený obsah.

Zakázáno bez výslovného zadání:

* serverový backend,
* ukládání osobních údajů studentů,
* sledování uživatelů,
* externí analytika,
* odesílání dat mimo školní systém,
* závislost na placené externí službě.

## Grafické snímky

Prezentační grafické snímky mají mít styl odborné technologické infografiky:

* poměr 16:9,
* jeden jasný podproblém na snímek,
* výrazný horní titulkový pruh,
* logické bloky a panely,
* krátký čitelný text,
* diagramy, ikony, schémata, fragmenty kódu,
* profesionální barevnost: tmavě modrá, bílá, světle šedá, akcenty zelená/oranžová/tyrkysová/fialová/červená,
* čistý akademický design.

Vyhýbej se:

* memům,
* clipartu,
* emoji,
* přeplněným tabulkám,
* agresivním gradientům,
* gamifikovanému vzhledu.

## Kontrola před dokončením úkolu

Před dokončením každého úkolu zkontroluj:

* Build Sphinxu proběhl bez chyby.
* Všechny nové soubory jsou zapojené do navigace.
* Kapitoly jsou v češtině.
* Kódové bloky mají uvedený jazyk.
* Interaktivní prvky nevyžadují backend.
* Nebyly zavedeny zbytečné závislosti.
* Nebyly odstraněny existující části bez důvodu.

## Výstup

Na konci úkolu vždy uveď:

* seznam změněných souborů,
* stručné shrnutí změn,
* příkazy použité k ověření,
* případné známé limity nebo nedodělky.

