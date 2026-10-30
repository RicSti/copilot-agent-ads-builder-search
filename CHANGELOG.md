# Changelog

## 1.0.0 – 2026-10-30

Erste öffentliche Version, basierend auf dem Agent-Stand 1.0.9 aus dem Microsoft 365 Copilot Agent Builder.

Bereinigungen gegenüber dem Export aus der Copilot-App:
- skill-02, -03, -04, -06: doppelter Frontmatter-Block entfernt (die neuere Fassung bleibt).
- skill-02: doppelte Zeilen zu „Max CPC“ entfernt.
- skill-05: Im Export enthielt die Datei versehentlich den Inhalt von skill-06; durch den Originaltext ersetzt.
- skill-01: Ausweich-Ablauf für nicht lesbare Seiten (gezielte Suche, Hauptseite getrennt, dann Seitentext in Teilen à max. 2.000 Zeichen mit Abschluss „fertig“); neue Steckbrief-Zeile „Quelle der Inhalte“. Anweisung verweist darauf.
- Skills zusätzlich als einzelne ZIP-Pakete in `dist/` (SKILL.md auf oberster Ebene).
