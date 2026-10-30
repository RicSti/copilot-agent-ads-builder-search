# Anleitung: Ads-Builder Search in Microsoft 365 Copilot anlegen

Dauer: ca. 15 Minuten. Du legst den Agent einmal an und kannst ihn danach in jedem Copilot-Chat nutzen.

> **Warum nicht einfach eine fertige Agent-Datei importieren?**
> Der Agent Builder kann komplette Agents nicht aus einer ZIP-Datei importieren. Ein App-Paket ginge nur über Entwickler-Werkzeuge (Microsoft 365 Agents Toolkit) und eine Freigabe durch die IT. Der Weg unten funktioniert ohne beides: Felder per Copy & Paste füllen, Skills als ZIP hochladen.

**Hinweis zu Bezeichnungen:** Microsoft benennt Schaltflächen je nach Sprache und Version leicht unterschiedlich. Unten steht die englische Bezeichnung aus der Microsoft-Doku, in Klammern die übliche deutsche.

---

## Schritt 0: Voraussetzungen prüfen

- [ ] Du hast eine **Microsoft 365 Copilot**-Lizenz (oder Copilot mit Pay-as-you-go). Ohne Lizenz fehlt der Agent Builder.
- [ ] Du arbeitest im Browser unter **[microsoft365.com/chat](https://microsoft365.com/chat)** (oder in Teams). Die Mobil-Apps können keine Agents anlegen.
- [ ] Deine IT hat Websuche und Code Interpreter in Copilot nicht gesperrt. Merkst du das erst in Schritt 4 oder 5, gib der IT diese Anleitung.
- [ ] Für den Import der Ergebnisse: [Google Ads Editor](https://ads.google.com/intl/de_de/home/tools/ads-editor/) installiert.

## Schritt 1: Dateien herunterladen

1. Auf der GitHub-Seite dieses Repos oben auf **Code** und dann **Download ZIP** klicken.
2. Die ZIP-Datei entpacken. Du brauchst daraus:
   - den Ordner `agent/` (Texte zum Einfügen)
   - den Ordner `dist/` (sechs Skill-Pakete zum Hochladen)

> Die Dateien in `dist/` **nicht entpacken**. Sie werden als ZIP hochgeladen.
>
> Auf dem Mac entpackt Safari heruntergeladene ZIP-Dateien manchmal automatisch. Dann liegen die Skill-ZIPs trotzdem unverändert im Ordner `dist/`.

## Schritt 2: Neuen Agent anlegen

1. [microsoft365.com/chat](https://microsoft365.com/chat) öffnen und anmelden.
2. In der linken Seitenleiste **Agents** (bzw. **Agents & Skills**) wählen, dann **New agent** (**Neuer Agent**).
3. Oben auf **Configure** (**Konfigurieren**) wechseln bzw. **Skip to configure** wählen. Den Chat im Reiter **Describe** (**Beschreiben**) brauchst du nicht.

## Schritt 3: Name, Beschreibung, Anweisungen

| Feld | Inhalt | Quelle |
|---|---|---|
| **Name** | `Ads-Builder Search` | – |
| **Icon** (optional) | `icons/color.png` | Stift-Symbol am Icon |
| **Description** (**Beschreibung**) | kompletten Text einfügen | [`agent/beschreibung.txt`](agent/beschreibung.txt) |
| **Instructions** (**Anweisungen**) | kompletten Text einfügen | [`agent/anweisungen.md`](agent/anweisungen.md) |

So kopierst du den Text am saubersten: Datei auf GitHub öffnen, oben rechts auf das Symbol **Copy raw file** (zwei Rechtecke) klicken, im Agent Builder einfügen.

> Die Anweisungen haben 7.584 Zeichen, erlaubt sind 8.000. Nichts ergänzen, sonst wird der Text abgeschnitten.
> Prüfe nach dem Einfügen, ob der Text mit `Ist der Codeinterpreter nicht verfügbar, sag das ausdrücklich.` endet.

## Schritt 4: Websuche aktivieren

Unter **Knowledge** (**Wissen**) den Schalter **Search all websites** bzw. **Web content** (**Webinhalte**) **einschalten**.

Ohne Websuche kann der Agent die URL nicht lesen. Weitere Wissensquellen (SharePoint, Dateien) sind nicht nötig.

## Schritt 5: Code Interpreter aktivieren

Unter **Capabilities** (**Funktionen**):

- **Code interpreter** (**Code-Interpreter**) – **einschalten (Pflicht)**. Damit zählt der Agent Zeichen exakt und schreibt die CSV-Dateien.
- **Image generator** (**Bildgenerator**) – nicht nötig, kann aus bleiben.

## Schritt 6: Skills hochladen

1. Im Reiter **Configure** den Bereich **Skills** aufklappen.
2. **Add** (**Hinzufügen**) wählen und die erste ZIP-Datei aus `dist/` hochladen.
3. Für alle sechs Dateien wiederholen:

| Nr. | Datei | Aufgabe |
|---|---|---|
| 1 | `skill-01-website-analyse.zip` | Steckbrief aus der Website |
| 2 | `skill-02-kampagne-anzeigengruppe.zip` | Kampagne + Anzeigengruppe |
| 3 | `skill-03-keywords.zip` | 15–30 Keywords |
| 4 | `skill-04-rsa.zip` | Responsive Search Ad |
| 5 | `skill-05-konto-assets.zip` | Sitelinks, Callouts, Snippets |
| 6 | `skill-06-validierung-export.zip` | Prüfung + CSV-Export |

Danach sollten sechs Skills in der Liste stehen (erlaubt sind maximal acht pro Agent). Die Reihenfolge spielt keine Rolle.

**Wenn der Bereich „Skills“ fehlt:** Skills sind noch nicht in allen Tenants freigeschaltet (z. B. nicht bei aktivierten Information Barriers). Dann die IT fragen. Notlösung ohne Skills gibt es nicht: Die Anweisungen verweisen auf die Skills, ohne sie fehlen dem Agent wichtige Regeln.

## Schritt 7: Starter-Prompts eintragen

Unter **Starter prompts** (**Einstiegsprompts**) die vier Einträge aus [`agent/starter-prompts.md`](agent/starter-prompts.md) übernehmen – je **Titel** und **Nachricht**.

Optional, aber praktisch: Du startest den Agent dann per Klick und ersetzt nur `url_der_seite`.

## Schritt 8: Speichern und testen

1. Oben rechts **Create** (**Erstellen**) bzw. **Save** (**Speichern**) klicken.
2. Rechts im Testbereich (**Try it**) oder später im Chat den Agent öffnen.
3. Testlauf mit einer eigenen Unterseite, z. B.:
   `Erstelle eine Google Ads Kampagne inkl. kontoübergreifender Assets für folgende URL: https://www.deine-domain.de/leistung`
4. Der Agent zeigt zuerst einen **Steckbrief** und fragt „Passt das?“. Mit „ja“ bestätigen.
5. Prüfen, ob am Ende zwei CSV-Dateien zum Download angeboten werden und unter den Blöcken eine Zeile wie
   `Feldprüfung: Block 1 = 22 Zeilen à 37 Felder ✓` steht. Fehlt diese Zeile, lief der Code Interpreter nicht (siehe Fehlerbehebung).

## Schritt 9: In den Google Ads Editor importieren

1. Google Ads Editor öffnen und das Konto herunterladen bzw. aktualisieren.
2. **Konto → Importieren → Aus Datei…** und zuerst `01_kampagne_komplett.csv` wählen.
3. Vorschau prüfen, **Importieren** bzw. **Änderungen übernehmen**.
4. Danach genauso `02_assets_konto.csv` importieren.
5. Kampagne prüfen (sie ist **pausiert**), dann **Posten**. Aktivieren erst nach deiner Freigabe.

Alternative ohne Datei: **Importieren → Text einfügen** und den jeweiligen Block aus dem Chat einfügen. Die CSV-Dateien sind der sicherere Weg.

---

## Varianten im Chat

| Du schreibst … | Ergebnis |
|---|---|
| nur URL + „Standard“ | Start ohne Rückfragen zu Budget, Gebotsstrategie usw. |
| „… ohne vorausgehende Rückfrage zum erstellten Steckbrief“ oder „direkt“ | kein Zwischenstopp nach dem Steckbrief |
| „Nur Assets …“ / „Nur Kampagne …“ | nur einer der beiden Blöcke |
| „Assets getrennt“ | Asset-Block als drei einzelne Blöcke (Sitelinks, Callouts, Snippets) |
| „Kampagne getrennt“ | Kampagnenblock als vier einzelne Blöcke |
| „Budget 50, Target CPA 30, Sie-Ansprache, Standort Bavaria, Germany“ | eigene Werte statt Standard |

Standardwerte: Tagesbudget 20 €, Gebotsstrategie „Maximize clicks“, Max. CPC 1 €, Standort Deutschland, Sprache Deutsch, Ansprache wie auf der Website, Konto-Assets ja.

## Fehlerbehebung

| Problem | Lösung |
|---|---|
| „Seite kann nicht gelesen werden“, obwohl sie im Browser funktioniert | Copilot liest Seiten über den Bing-Suchindex, nicht direkt. Neue Landingpages fehlen dort oft. Test: bei Bing `site:deine-domain.de` plus Wörter aus dem URL-Pfad suchen. Lösung im Chat: Der Agent bittet um den Seitentext. Pro Nachricht passen max. 2.000 Zeichen – längere Seiten in mehreren Nachrichten schicken und mit „fertig“ abschließen. Menü, Footer und Cookie-Hinweise weglassen. Dauerhaft: URL in den [Bing Webmaster Tools](https://www.bing.com/webmasters) einreichen. |
| Seite lädt Inhalte nur per JavaScript oder blockiert Bots | Wie oben: Seitentext in Teilen einfügen. |
| Keine CSV-Dateien, keine „Feldprüfung“-Zeile | Code Interpreter ist aus (Schritt 5) oder in deinem Tenant gesperrt. Schreib: „Erzeuge die Blöcke jetzt mit dem Codeinterpreter.“ |
| Agent schreibt „SKILL_06 nicht verfügbar“ | Skill-Upload prüfen (Schritt 6). Die Ausgabe folgt trotzdem dem Export-Vertrag, aber bitte genau kontrollieren. |
| Editor meldet Spaltenfehler beim Import | Im Chat „Kampagne getrennt“ bzw. „Assets getrennt“ schreiben und die Einzelblöcke nacheinander importieren. |
| Umlaute kaputt (z. B. „WÃ¤rmepumpe“) | Datei nicht vorher in Excel öffnen und speichern. Direkt im Editor importieren; die Dateien sind UTF-8. |
| Snippet-Header wird abgelehnt | Header muss exakt englisch sein, z. B. `Service catalog` oder `Types`. Agent zur Korrektur auffordern. |
| Skill-Upload wird abgelehnt | Die ZIP-Datei darf nicht entpackt und neu gepackt werden. Original aus `dist/` verwenden. |

## Agent anpassen

Willst du Regeln ändern (z. B. andere Standardwerte oder Namenskonvention):

1. Die passende `SKILL.md` in `skills/` bearbeiten.
2. Mit `python3 tools/build_skill_zips.py` neue ZIPs in `dist/` erzeugen.
3. Im Agent Builder den alten Skill entfernen und den neuen hochladen.

Für Änderungen an der Anweisung: `agent/anweisungen.md` bearbeiten, mit `python3 tools/check_anweisungen.py` die 8.000-Zeichen-Grenze prüfen und den Text neu einfügen.
