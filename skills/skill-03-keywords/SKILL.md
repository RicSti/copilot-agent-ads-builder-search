---
name: skill-03-keywords
description: Erzeugt 15 bis 30 Google-Ads-Keywords aus dem Website-Steckbrief, standardmäßig im Match Type Phrase, und liefert sie als Keyword-Zeilen für den Kampagnen-Gesamtblock des Google Ads Editors. Verwenden, wenn Keywords für eine Anzeigengruppe gebraucht werden.
---

# SKILL_03 – Keywords

## Menge und Match Type
- 15–30 Keywords, ohne Dubletten (auch nicht als Plural/Singular-Paar).
- Match Type standardmäßig für ALLE Keywords: Phrase
- Exact oder Broad nur, wenn der Nutzer es ausdrücklich verlangt.

## Keyword-Cluster (aus dem Steckbrief ableiten)
1. Kern: Produkt/Leistung der Unterseite (z. B. wärmepumpe einbauen)
2. Varianten: Synonyme, Fachbegriff + Laienbegriff, Plural (z. B. luftwärmepumpe installation)
3. Problem: Suchanfragen zum Problem, das die Leistung löst (z. B. heizung austauschen)
4. Kaufabsicht: kosten, preis, angebot, anbieter, firma, beauftragen, kaufen, bestellen
5. Lokal: nur wenn die Website eine Region nennt (z. B. wärmepumpe münchen)
6. Marke: nur 1–2 Keywords mit Markenname, wenn die Marke bekannt genug ist

## Schreibweise
- Kleinschreibung, Umlaute ausschreiben (ä, ö, ü, ß), keine Satzzeichen.
- Kein Match-Type-Zeichen im Keyword (keine "" oder []) – der Match Type steht in der eigenen Spalte.
- Max. 80 Zeichen und max. 10 Wörter pro Keyword.
- Keine Keywords zu Leistungen, die die Website nicht anbietet.
- Keine Informations-Keywords ohne Kaufnähe (z. B. „was ist“, „definition“, „kostenlos“, „selber machen“) – diese stattdessen unter „Offene Punkte“ als mögliche negative Keywords nennen.

## Ausgabe: je Keyword eine Zeile im Kampagnen-Gesamtblock (SKILL_06)
| Spalte | Wert |
|---|---|
| Campaign | exakter Kampagnenname |
| Ad group | exakter Anzeigengruppenname |
| Keyword | Text ohne Match-Type-Zeichen |
| Match Type | Phrase |

Alle anderen Spalten der Keyword-Zeilen bleiben leer, auch Max CPC (der Wert gilt nur für die Anzeigengruppe).
