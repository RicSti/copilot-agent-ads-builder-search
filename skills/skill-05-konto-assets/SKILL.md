---
name: skill-05-konto-assets
description: Erstellt kontoübergreifende Google-Ads-Assets aus der Hauptseite - 4 bis 8 Sitelinks, 4 bis 8 Callouts und 1 bis 2 Structured Snippets - als gemeinsamen Asset-Block für den Google Ads Editor mit Campaign = <account-level>. Verwenden, wenn Konto-Assets gewünscht sind.
---

# SKILL_05 – Konto-Assets

## Grundsatz
- Ebene: Konto. In JEDER Asset-Zeile steht in der Spalte Campaign exakt: <account-level>
- Inhalt allgemein halten (Unternehmen, nicht einzelnes Produkt), damit die Assets zu jeder Kampagne passen.
- Vor dem Erstellen fragen (einmal pro Konto): „Gibt es im Konto schon Sitelinks, Callouts oder Snippets auf Kontoebene?“ Wenn ja: nur ergänzen, keine Dubletten.
- Alle Assets kommen gemeinsam in den Asset-Block (SKILL_06, Block 2), nicht in den Kampagnen-Gesamtblock. Die Kopfzeilen unten gelten nur für den Fallback „Assets getrennt“.

## Sitelinks (4–8)
Limits: Link text max. 25 Zeichen, Description Line 1 und Description Line 2 je max. 35 Zeichen.
- Nur URLs, die im Steckbrief als echte Seiten der Domain stehen. Keine erfundenen Pfade.
- Jede Final URL unterschiedlich; nicht die Startseite und nicht die Unterseite der RSA.
- Bevorzugte Ziele: Kontakt, Angebot/Termin, Leistungen, Preise, Referenzen, Über uns, FAQ, Karriere (nur wenn passend).
- Link text = klare Aktion oder klares Ziel („Kostenloses Angebot“, „Unsere Referenzen“). Beschreibungen ergänzen den Nutzen, sie wiederholen nicht den Link text.
- Immer beide Beschreibungszeilen füllen.

Kopfzeile (kommagetrennt, exakt so):
"Campaign","Link text","Final URL","Description Line 1","Description Line 2"

Beispielzeile:
"<account-level>","Kostenloses Angebot","https://www.example.de/angebot","Antwort innerhalb von 24 Std.","Unverbindlich und kostenfrei"

## Callouts (4–8)
Limit: max. 25 Zeichen je Callout.
- Kurze, belegbare Vorteile ohne Satzzeichen am Ende: „Kostenlose Erstberatung“, „Meisterbetrieb seit 1998“, „Festpreisgarantie“.
- Keine Wiederholung von Headlines oder Sitelink-Texten.

Kopfzeile (kommagetrennt, exakt so):
"Campaign","Callout text"

Beispielzeile:
"<account-level>","Kostenlose Erstberatung"

## Snippets (1–2)
Limit: MINDESTENS 3 und max. 10 Werte je Snippet, jeder Wert max. 25 Zeichen.
- Harte Regel: Nie ein Snippet mit nur 1 oder 2 Werten ausgeben. Gibt die Website für einen Header keine 3 passenden Werte her, einen anderen Header wählen oder das Snippet weglassen und unter „Offene Punkte“ vermerken.
- Language: PFLICHT in jeder Snippet-Zeile. Wert = Sprache der Snippet-Werte als Sprachcode wie bei der Kampagne (Standard: de).
- Header: PFLICHT und EXAKT einer dieser 13 Werte (englisch, Schreibweise inkl. Groß-/Kleinschreibung genau so, auch bei deutschen Werten):
  - Amenities
  - Brands
  - Courses
  - Degree programs
  - Destinations
  - Featured hotels
  - Insurance coverage
  - Models
  - Neighborhoods
  - Service catalog
  - Shows
  - Styles
  - Types
- Keine anderen Header, keine Übersetzungen (nicht „Leistungen“, „Marken“, „Typen“), keine eigenen Varianten.
- Häufigste Wahl: „Service catalog“ (Leistungen), „Types“ (Arten/Varianten) oder „Brands“ (geführte Marken).
- Werte sind Substantive/Kategorien, keine Werbesätze.
- Snippet values: Werte durch einen ECHTEN Zeilenumbruch trennen (kein Semikolon, kein \n als Text) und das ganze Feld in doppelte gerade Anführungszeichen " setzen. Keine typografischen Anführungszeichen („ “).

Kopfzeile (kommagetrennt, exakt so):
"Campaign","Language","Header","Snippet values"

Beispielzeile (ein Datensatz über mehrere Textzeilen):
"<account-level>","de","Service catalog","Wärmepumpen
Solaranlagen
Heizungswartung
Förderberatung"
