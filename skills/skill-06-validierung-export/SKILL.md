---
name: skill-06-validierung-export
description: Prüft alle Google-Ads-Elemente per Codeinterpreter auf Zeichenlimits, Anzahl, Dubletten, Pflichtwerte und URLs und gibt Vorschau-Tabellen sowie zwei kommagetrennte Import-Blöcke (Textfelder in doppelten geraden Anführungszeichen) für den Google Ads Editor aus (Kampagnen-Gesamtblock und Asset-Block). Verwenden als letzten Schritt vor jeder Ausgabe.
---

# SKILL_06 – Validierung & Export

## 1. Prüfen (immer mit dem Codeinterpreter, nie schätzen)
| Element | Max. Zeichen |
|---|---|
| RSA Headline | 30 |
| RSA Description | 90 |
| Path 1 / Path 2 | 15 |
| Sitelink Link text | 25 |
| Description Line 1 / Description Line 2 | 35 |
| Callout text | 25 |
| Snippet-Wert (einzeln) | 25 |
| Keyword | 80 (max. 10 Wörter) |

Weitere Prüfungen:
- Anzahl: 15 Headlines, 4 Descriptions, 15–30 Keywords, 4–8 Sitelinks, 4–8 Callouts, 1–2 Snippets mit je MINDESTENS 3 und max. 10 Werten.
- Keine Dubletten innerhalb eines Elementtyps (Vergleich klein geschrieben).
- Kampagnen- und Anzeigengruppenname in allen Zeilen identisch.
- Kampagnen-Zeile: EU political ads = no, Campaign status = Paused.
- Anzeigengruppen-Zeile: Max CPC gesetzt (Standard 1); in Keyword- und RSA-Zeilen ist Max CPC leer.
- RSA-Spalten heißen Description 1 bis Description 4 (nicht „Description“).
- Alle Keywords: Match Type = Phrase (außer der Nutzer wollte etwas anderes).
- Alle Asset-Zeilen: Campaign = <account-level>.
- Snippet-Zeilen: Language gefüllt (Standard de); Header exakt in ALLOWED_HEADERS, sonst Fehler und korrigieren:
  ALLOWED_HEADERS = {"Amenities","Brands","Courses","Degree programs","Destinations","Featured hotels","Insurance coverage","Models","Neighborhoods","Service catalog","Shows","Styles","Types"}
- Alle URLs beginnen mit https:// und gehören zur analysierten Domain.
- Keine verbotenen Floskeln, keine Ausrufezeichen in Headlines.
- Überschreitung gefunden → Text kürzen, erneut prüfen, erst dann ausgeben.

## 2. Vorschau in Markdown
Je Element eine Tabelle mit Spalte „Zeichen“ (gemessener Wert). Bei RSA zusätzlich Spalte „Limit“.

## 3. Import-Blöcke (genau zwei, je ein Codeblock, kommagetrennt)

Format für ALLE Blöcke (Kopfzeile und Datenzeilen):
- Trennzeichen: Komma.
- Jedes nicht-numerische Feld in doppelte gerade Anführungszeichen "…" setzen, auch in der Kopfzeile. Anführungszeichen im Text verdoppeln ("").
- Numerische Felder (z. B. Budget 20.00, Target CPA) ohne Anführungszeichen.
- Leere Felder bleiben ganz leer (Komma direkt nach Komma), kein "".

### Block 1: Kampagnen-Gesamtblock (Kampagne + Anzeigengruppe + Keywords + RSA)
Kopfzeile exakt so (37 Spalten):
"Campaign","Campaign status","Campaign type","Networks","Budget","Budget type","Bid strategy type","Language","Location","EU political ads","Ad group","Max CPC","Keyword","Match Type","Ad type","Headline 1","Headline 2","Headline 3","Headline 4","Headline 5","Headline 6","Headline 7","Headline 8","Headline 9","Headline 10","Headline 11","Headline 12","Headline 13","Headline 14","Headline 15","Description 1","Description 2","Description 3","Description 4","Path 1","Path 2","Final URL"

Optionale Spalten (Customer ID, Campaign start date, Target CPA) nur anhängen, wenn ein Wert vorliegt.

Zeilenfolge:
| Zeile | Gefüllte Spalten (Rest leer) |
|---|---|
| 1 Kampagne | Campaign bis EU political ads (SKILL_02) |
| 2 Anzeigengruppe | Campaign, Ad group, Max CPC (Standard 1) |
| 3 bis n Keywords | Campaign, Ad group, Keyword, Match Type |
| letzte Zeile RSA | Campaign, Ad group, Ad type, Headline 1 bis Final URL |

Jede Zeile hat EXAKT 37 Felder (= 36 Kommas), genau wie die Kopfzeile – auch Anzeigengruppen-, Keyword- und RSA-Zeilen. Deren Kampagnen-Spalten (Campaign status bis EU political ads, also auch Language) werden als LEERE Felder mitgegeben, nicht weggelassen. Leere Felder bleiben leer (kein „-“, kein „n/a“, kein Leerzeichen).

Beispiel Anzeigengruppen-Zeile (Kampagnenname, 9 leere Felder, Ad group, Max CPC, 25 leere Felder):
"Search | Muster GmbH | Wärmepumpe | DE",,,,,,,,,,"Wärmepumpe Einbau",1,,,,,,,,,,,,,,,,,,,,,,,,,

Beispiel Keyword-Zeile (Kampagnenname, 9 leere Felder, Ad group, leeres Max CPC, Keyword, Phrase, 23 leere Felder):
"Search | Muster GmbH | Wärmepumpe | DE",,,,,,,,,,"Wärmepumpe Einbau",,"wärmepumpe einbauen","Phrase",,,,,,,,,,,,,,,,,,,,,,,

Beispiel RSA-Zeile (Kampagnenname, 9 leere Felder, Ad group, 3 leere Felder für Max CPC/Keyword/Match Type, dann Ad type bis Final URL):
"Search | Muster GmbH | Wärmepumpe | DE",,,,,,,,,,"Wärmepumpe Einbau",,,,"Responsive search ad","Headline 1",…,"Final URL"

Fallback „Kampagne getrennt“: Sagt der Nutzer das oder meldet der Editor Spaltenfehler in Block 1, Block 1 in vier Blöcke aufteilen (Reihenfolge Kampagne → Anzeigengruppe → Keywords → RSA), jeweils nur mit diesen Kopfzeilen:
"Campaign","Campaign status","Campaign type","Networks","Budget","Budget type","Bid strategy type","Language","Location","EU political ads"
"Campaign","Ad group","Max CPC"
"Campaign","Ad group","Keyword","Match Type"
"Campaign","Ad group","Ad type","Headline 1","Headline 2","Headline 3","Headline 4","Headline 5","Headline 6","Headline 7","Headline 8","Headline 9","Headline 10","Headline 11","Headline 12","Headline 13","Headline 14","Headline 15","Description 1","Description 2","Description 3","Description 4","Path 1","Path 2","Final URL"

### Block 2: Asset-Block (Sitelinks + Callouts + Snippets)
Kopfzeile exakt so (9 Spalten, keine doppelt):
"Campaign","Link text","Final URL","Description Line 1","Description Line 2","Callout text","Language","Header","Snippet values"

Zeilenfolge:
| Zeilen | Gefüllte Spalten (Rest leer) |
|---|---|
| Sitelinks | Campaign, Link text, Final URL, Description Line 1, Description Line 2 |
| Callouts | Campaign, Callout text |
| Snippets | Campaign, Language, Header, Snippet values |

- Campaign ist in jeder Zeile <account-level>.
- Jede Zeile füllt nur die Spalten EINER Asset-Art.
- Snippet values: mindestens 3 Werte, durch echte Zeilenumbrüche getrennt, ganzes Feld in doppelten geraden Anführungszeichen "…".

Fallback „Assets getrennt“: Sagt der Nutzer das oder meldet der Editor Fehler beim Asset-Block, stattdessen drei Blöcke mit diesen Kopfzeilen ausgeben:
"Campaign","Link text","Final URL","Description Line 1","Description Line 2"
"Campaign","Callout text"
"Campaign","Language","Header","Snippet values"

## 4. Blöcke erzeugen (Codeinterpreter)
PFLICHT: Beide Blöcke ausschließlich mit dieser Funktion im Codeinterpreter erzeugen und die Ausgabe unverändert übernehmen. Blöcke NIE von Hand tippen oder nachträglich umformatieren – dabei gehen leere Felder verloren und die Spalten verschieben sich.
```python
import csv, io, re
NUM = re.compile(r"^-?\d+(\.\d+)?$")
def fmt(v):
    v = "" if v is None else str(v)
    if v == "":
        return ""                      # leer bleibt leer
    if NUM.match(v):
        return v                       # Zahl ohne Anführungszeichen
    return '"' + v.replace('"', '""') + '"'   # Text in "…"
def block(header, rows):
    lines = [",".join(fmt(h) for h in header)]
    for r in rows:
        lines.append(",".join(fmt(r.get(h, "")) for h in header))
    out = "\n".join(lines) + "\n"
    # Pflichtprüfung: jede Zeile hat exakt so viele Felder wie die Kopfzeile
    parsed = list(csv.reader(io.StringIO(out), delimiter=",", quotechar='"'))
    bad = [i for i, row in enumerate(parsed) if len(row) != len(header)]
    assert not bad, f"Spaltenzahl falsch in Zeilen {bad}"
    return out
# Snippet: {"Campaign": "<account-level>", "Language": "de", "Header": "Service catalog",
#           "Snippet values": "\n".join(werte)}  -> wird automatisch in "…" gesetzt
```
Zusätzlich dieselben Inhalte als UTF-8-Dateien anbieten: 01_kampagne_komplett.csv, 02_assets_konto.csv (gleiche Funktion, Komma als Trenner, UTF-8).

## 5. Import-Anleitung (am Ende der Ausgabe in 3 Zeilen)
Google Ads Editor → Konto herunterladen → Konto > Importieren > Text einfügen (Block einfügen) oder Aus Datei → Änderungen prüfen → Posten. Reihenfolge: Block 1, dann Block 2.
