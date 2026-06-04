# Algoritmus

Algoritmy jsou zakladem informatiky, protoze umoznuji popsat reseni problemu jasnym a opakovatelnych postupem.

## Vyukove cile

- Vysvetlit pojem algoritmus vlastnimi slovy.
- Rozpoznat vlastnosti dobreho algoritmu.
- Vytvorit jednoduchy algoritmus a zapsat ho v Pythonu.

## Zakladni pojmy

- algoritmus
- krok
- vstup
- vystup
- podminka

## Vyklad

Algoritmus je konecna posloupnost kroku, ktera vede od zadaneho vstupu ke spravnemu vystupu. Dobry algoritmus je srozumitelny, jednoznacny a proveditelny. V praxi se algoritmy zapisuji slovne, pomoci vyvojovych diagramu nebo primo v programovacim jazyce.

## Ukazka v Pythonu

```python
def je_sude(cislo: int) -> bool:
    return cislo % 2 == 0

vstup = 14
if je_sude(vstup):
    print(f"Cislo {vstup} je sude.")
else:
    print(f"Cislo {vstup} je liche.")
```

## Jednoduchy diagram

```{mermaid}
flowchart TD
    A[Zadej cislo] --> B{cislo % 2 == 0?}
    B -- Ano --> C[Vypis: sude]
    B -- Ne --> D[Vypis: liche]
```

## Cviceni

1. Navrhni algoritmus pro zjisteni, zda je student plnolety.
2. Uprav ukazkovy program tak, aby fungoval pro seznam cisel.

## Rozbalovaci napoveda

```{toggle} Napoveda
Zamysli se nad tim, jaky vstup algoritmus dostane a jaky ma byt vystup.
```

## Rozbalovaci reseni

```{toggle} Reseni
Pro plnoletost staci podminka vek >= 18. U seznamu cisel projdi hodnoty cyklem a pro kazdou urci sudost.
```

## Shrnuti

Algoritmus je presny navod k reseni problemu. Musi mit jasne kroky, definovany vstup a vystup a musi skoncit.

## Kontrolni otazky

1. Jake vlastnosti by mel mit kvalitni algoritmus?
2. Proc je dulezita jednoznacnost jednotlivych kroku?
3. Jak poznas, ze algoritmus vzdy skonci?
