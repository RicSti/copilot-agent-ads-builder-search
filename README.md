# Ads-Builder Search – Copilot-Agent für Google-Ads-Suchkampagnen

Ein Agent für **Microsoft 365 Copilot**, der aus einer Webseiten-URL eine importfertige Google-Ads-Suchkampagne baut – inklusive Sitelinks, Callouts und Snippets auf Kontoebene. Ergebnis sind zwei CSV-Dateien, die du direkt in den **Google Ads Editor** importierst.

Du brauchst keine Programmierkenntnisse. Der Agent wird einmal in der Copilot-Oberfläche angelegt (ca. 15 Minuten) und steht dir danach dauerhaft zur Verfügung.

## Was du bekommst

Aus einer URL (Unterseite, optional plus Startseite) entstehen:

| Element | Umfang |
|---|---|
| Steckbrief | Marke, Angebot, Zielgruppe, Nutzen, USPs, Region, Du/Sie – zur Freigabe vor dem Bauen |
| Kampagne | 1 Suchkampagne, **pausiert**, Tagesbudget 20 €, „Maximize clicks“ (änderbar) |
| Anzeigengruppe | 1 Anzeigengruppe, Max. CPC 1 € |
| Keywords | 15–30 Keywords, Match Type Phrase |
| Responsive Search Ad | 15 Headlines (≤ 30 Z.), 4 Descriptions (≤ 90 Z., AIDA/PAS), 2 Pfade |
| Konto-Assets | 4–8 Sitelinks, 4–8 Callouts, 1–2 Structured Snippets |
| Export | `01_kampagne_komplett.csv` und `02_assets_konto.csv` (UTF-8) plus Import-Blöcke zum Einfügen |

Alle Zeichenlimits prüft der Agent per Code Interpreter (Python), nicht per Schätzung. Die CSV-Zeilen erzeugt ebenfalls ein Skript, damit keine Spalten verrutschen.

## So ist der Agent aufgebaut

```
Anweisung (Rolle, Ablauf, Schreibstil, Export-Vertrag)
 └─ Skills (Arbeitsschritte)
     ├─ skill-01-website-analyse          → Steckbrief
     ├─ skill-02-kampagne-anzeigengruppe  → Kampagne + Anzeigengruppe
     ├─ skill-03-keywords                 → 15–30 Keywords
     ├─ skill-04-rsa                      → Responsive Search Ad
     ├─ skill-05-konto-assets             → Sitelinks, Callouts, Snippets
     └─ skill-06-validierung-export       → Prüfung + CSV-Export
```

Die KI schreibt, ein Skript kontrolliert.

## Schnellstart

1. Oben rechts auf **Code → Download ZIP** klicken und entpacken.
2. Der [Anleitung](ANLEITUNG.md) folgen: Agent anlegen, Anweisung einfügen, Skills hochladen, Code Interpreter und Websuche aktivieren.
3. Im Agent einen der Starter-Prompts wählen und eine URL einsetzen.
4. CSV-Dateien im Google Ads Editor importieren, prüfen, posten.

## Inhalt des Repos

| Pfad | Inhalt |
|---|---|
| [`ANLEITUNG.md`](ANLEITUNG.md) | Schritt-für-Schritt-Anleitung zum Anlegen des Agents |
| [`agent/anweisungen.md`](agent/anweisungen.md) | Text für das Feld **Instructions** (7.584 von max. 8.000 Zeichen) |
| [`agent/beschreibung.txt`](agent/beschreibung.txt) | Text für das Feld **Description** |
| [`agent/starter-prompts.md`](agent/starter-prompts.md) | Vier Starter-Prompts |
| [`skills/`](skills/) | Die sechs Skills als lesbare `SKILL.md` |
| [`dist/`](dist/) | Dieselben Skills als fertige ZIP-Pakete zum Hochladen |
| [`icons/`](icons/) | Optionales Agent-Icon |
| [`tools/`](tools/) | Hilfsskripte für Pflege und Prüfung (nur für Anpassungen nötig) |

## Voraussetzungen

- Microsoft 365 Copilot-Lizenz (oder Copilot mit Pay-as-you-go) und Zugriff auf den Agent Builder
- In deinem Tenant erlaubt: Websuche in Copilot und Code Interpreter (ggf. IT fragen)
- Google Ads Editor für den Import

## Grenzen – bitte lesen

- Das Ergebnis ist ein **Startpunkt, kein fertiges Konto**: eine Anzeigengruppe, nur Phrase Match, keine Gebotsoptimierung.
- Die Kampagne wird immer **pausiert** angelegt. Vor dem Aktivieren alles prüfen.
- Inhalte stammen nur von der analysierten Website. Trotzdem kann eine KI Aussagen falsch übernehmen – jede Headline vor dem Posten lesen.
- Bei Gesundheits-, Finanz-, Glücksspiel- oder Rechtsthemen sowie bei Preisen und Garantien setzt der Agent den Hinweis „Bitte rechtlich prüfen lassen“. Das ersetzt keine Rechtsprüfung.
- Microsoft ändert die Copilot-Oberfläche regelmäßig. Weichen Bezeichnungen ab, gerne ein Issue anlegen.

## Lizenz

[MIT](LICENSE) – frei nutzbar und anpassbar, auch kommerziell. Ohne Gewähr.

Entwickelt von Richard Stinauer, [adtraffic](https://www.adtraffic.de). Vorgestellt beim PPC Camp Rosenheim 2026 („Vom Prompt zum Tool“).
