---
name: skill-04-rsa
description: Schreibt eine Responsive Search Ad mit 15 Headlines (max. 30 Zeichen), 4 Descriptions (max. 90 Zeichen, AIDA/PAS) und 2 Pfaden als RSA-Zeile für den Kampagnen-Gesamtblock des Google Ads Editors. Verwenden, wenn Anzeigentexte für Google-Suchkampagnen erstellt werden.
---

# SKILL_04 – Responsive Search Ad (RSA)

## Zeichenlimits (hart)
- Headline: max. 30 Zeichen (Leerzeichen zählen mit)
- Description: max. 90 Zeichen
- Path 1 / Path 2: je max. 15 Zeichen, keine Leerzeichen, Bindestrich erlaubt, keine Umlaute (ae/oe/ue)

## Headlines (15 Stück, alle unterschiedlich)
| Nr. | Funktion | Beispiel-Logik |
|---|---|---|
| 1–4 | Keyword-Headlines: Kern-Keyword wörtlich enthalten | „Wärmepumpe vom Fachbetrieb“ |
| 5–7 | Nutzen für den Kunden | „Bis zu 70 % Heizkosten sparen“ – nur wenn belegt |
| 8–10 | USP / Beleg | „Über 2.000 Anlagen installiert“ |
| 11–12 | Handlungsaufforderung | „Jetzt Angebot anfordern“ |
| 13 | Marke | „[Marke] – [Kurzclaim]“ |
| 14 | Region oder Angebot/Preis | „Einbau in ganz Bayern“ |
| 15 | Einwand-Entkräftung | „Förderantrag inklusive“ |

- Jede Headline muss allein und in jeder Kombination Sinn ergeben.
- Normale deutsche Rechtschreibung: echte Umlaute und ß (ä, ö, ü, ß – nie ae, oe, ue, ss als Ersatz) und Groß-/Kleinschreibung wie im Satz, nicht jedes Wort groß („Lernen von Praktikern“, nicht „Lernen Von Praktikern“). Nur Path 1/2 ohne Umlaute.
- Keine Ausrufezeichen, kein durchgehender Großbuchstabe, keine Telefonnummer, keine Wiederholung desselben Wortanfangs in mehr als 3 Headlines.
- Pinning: Standard ohne Pin. Nur wenn der Nutzer es will: Marken-Headline auf Position 1 oder 2 (Spalte „Headline 13 position“ = 1).

## Descriptions (4 Stück)
| Nr. | Framework | Inhalt |
|---|---|---|
| 1 | PAS | Problem benennen → Lösung des Anbieters → CTA |
| 2 | AIDA | Aufmerksamkeit → Interesse → Wunsch → Aktion |
| 3 | Nutzen + Beleg | konkreter Vorteil + Beweis von der Website |
| 4 | Ablauf / Sicherheit | „So einfach geht’s“ oder Garantie/Service + CTA |

- Jede Description endet mit Punkt. Kern-Keyword in mind. 2 Descriptions.

## Pfade
- Path 1 = Hauptkategorie (z. B. waermepumpe), Path 2 = Spezifizierung (z. B. einbau). Aus der URL-Struktur ableiten, wenn möglich.

## Ausgabe: eine RSA-Zeile im Kampagnen-Gesamtblock (SKILL_06), gefüllte Spalten
Campaign | Ad group | Ad type | Headline 1 … Headline 15 | Description 1 | Description 2 | Description 3 | Description 4 | Path 1 | Path 2 | Final URL

Achtung: Die erste Description-Spalte heißt „Description 1“, nicht „Description“. Pin-Spalten („Headline 1 position“ usw.) nur aufnehmen, wenn gepinnt wird.

## Werte
| Spalte | Wert |
|---|---|
| Campaign / Ad group | exakte Namen aus SKILL_02 |
| Ad type | Responsive search ad |
| Final URL | Unterseiten-URL vollständig mit https:// |
