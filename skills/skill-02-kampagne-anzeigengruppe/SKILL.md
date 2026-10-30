---
name: skill-02-kampagne-anzeigengruppe
description: Erstellt die Kampagnen-Zeile und die Anzeigengruppen-Zeile einer Google-Ads-Suchkampagne für den Kampagnen-Gesamtblock des Google Ads Editors, inklusive Namenskonvention, Standardwerten und der Pflichtspalte EU political ads. Verwenden nach der Website-Analyse.
---

# SKILL_02 – Kampagne & Anzeigengruppe

## Namenskonvention
- Kampagne: Search | [Marke] | [Thema] | [Land-Kürzel]   Beispiel: Search | Muster GmbH | Wärmepumpe | DE
- Anzeigengruppe: [Thema]   Beispiel: Wärmepumpe Einbau
- Namen in ALLEN Zeilen exakt identisch verwenden (Groß-/Kleinschreibung, Leerzeichen).
- Kein Tabulator, kein Zeilenumbruch im Namen.

## Ausgabe
Beide Zeilen gehören in den Kampagnen-Gesamtblock (Kopfzeile und Aufbau: SKILL_06). Zeile 1 = Kampagne, Zeile 2 = Anzeigengruppe. Alle hier nicht genannten Spalten bleiben in der jeweiligen Zeile leer.

## Zeile 1 – Kampagne
| Spalte | Wert |
|---|---|
| Campaign | Kampagnenname |
| Campaign status | Paused |
| Campaign type | Search |
| Networks | Google search |
| Budget | Zahl mit Punkt als Dezimaltrenner, z. B. 20.00 |
| Budget type | Daily |
| Bid strategy type | vom Nutzer; erlaubt u. a.: Maximize clicks; Maximize Conversions; Target CPA; Manual CPC |
| Language | de (mehrere mit Semikolon: de;en) |
| Location | z. B. Germany; Austria; Switzerland (englische Geo-Namen, z. B. Munich, Bavaria, Germany) |
| EU political ads | no (IMMER setzen, Pflichtspalte) |

Optionale Spalten, nur wenn ein Wert vorliegt (dann ans Ende der Kopfzeile anhängen): Customer ID (nur MCC), Campaign start date (JJJJ-MM-TT), Target CPA (nur bei Gebotsstrategie Target CPA).

Suchnetzwerk-Partner und Displaynetzwerk NICHT aktivieren, außer der Nutzer will es ausdrücklich.

## Zeile 2 – Anzeigengruppe
| Spalte | Wert |
|---|---|
| Campaign | exakter Kampagnenname |
| Ad group | exakter Anzeigengruppenname |
| Max CPC | 1 (Standard; Zahl ohne Anführungszeichen, Punkt als Dezimaltrenner, z. B. 1 oder 1.50) |

Die Anzeigengruppe ist standardmäßig aktiv; die Kampagne ist pausiert, es läuft also nichts aus.
Max CPC IMMER setzen (Standard 1, außer der Nutzer nennt einen anderen Wert). Bei automatischen Gebotsstrategien ignoriert Google den Wert, er schadet aber nicht.

## Regeln
- Pro Unterseite genau eine Kampagne mit einer Anzeigengruppe, außer der Nutzer will mehrere.
- Existiert die Kampagne laut Nutzer schon: Kampagnen-Zeile weglassen, nur Anzeigengruppe, Keywords und RSA in die bestehende Kampagne legen.
