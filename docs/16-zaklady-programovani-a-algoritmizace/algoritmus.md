# Algoritmus

Algoritmy jsou základem informatiky, protože umožňují popsat řešení problému jasným a opakovatelným postupem. Díky algoritmům lze úlohu vysvětlit člověku, zkontrolovat její správnost a později ji převést do programu.

## Výukové cíle

- Vysvětlit pojem algoritmus vlastními slovy.
- Rozpoznat vlastnosti dobře navrženého algoritmu.
- Vytvořit jednoduchý algoritmus a zapsat ho v Pythonu.

## Základní pojmy

- algoritmus
- krok
- vstup
- výstup
- podmínka

## Výklad

Algoritmus je konečná posloupnost kroků, která vede od zadaného vstupu ke správnému výstupu. Dobrý algoritmus je srozumitelný, jednoznačný a proveditelný. Každý krok musí být popsán tak, aby bylo jasné, co se má udělat a kdy postup končí.

V praxi se algoritmy zapisují slovně, pomocí vývojových diagramů nebo přímo v programovacím jazyce. Program je potom konkrétní zápis algoritmu, který může provést počítač.

## Ukázka nebo modelová situace

Představ si, že chceš rozhodnout, zda je zadané celé číslo sudé. Vstupem je číslo, postup ověří zbytek po dělení dvěma a výstupem je odpověď, zda je číslo sudé, nebo liché.

## Ukázka kódu

```python
def je_sude(cislo: int) -> bool:
    return cislo % 2 == 0

vstup = 14
if je_sude(vstup):
    print(f"Číslo {vstup} je sudé.")
else:
    print(f"Číslo {vstup} je liché.")
```

## Grafické shrnutí nebo diagram

```{mermaid}
flowchart TD
    A[Zadej číslo] --> B{číslo % 2 == 0?}
    B -- Ano --> C[Vypiš: sudé]
    B -- Ne --> D[Vypiš: liché]
```

## Cvičení

1. Navrhni algoritmus pro zjištění, zda je student plnoletý.
2. Uprav ukázkový program tak, aby fungoval pro seznam čísel.

## Rozbalovací nápověda

```{toggle} Nápověda
Zamysli se nad tím, jaký vstup algoritmus dostane a jaký má být výstup. Potom urči podmínku, která rozhoduje mezi dvěma možnostmi.
```

## Rozbalovací řešení

```{toggle} Řešení
Pro plnoletost stačí podmínka `vek >= 18`. U seznamu čísel projdi hodnoty cyklem `for` a pro každou hodnotu zavolej funkci `je_sude`.
```

## Shrnutí

Algoritmus je přesný návod k řešení problému. Musí mít jasné kroky, definovaný vstup a výstup a musí skončit v konečném počtu kroků.

## Kontrolní otázky

1. Jaké vlastnosti by měl mít kvalitní algoritmus?
2. Proč je důležitá jednoznačnost jednotlivých kroků?
3. Jak poznáš, že algoritmus vždy skončí?
