#!/usr/bin/env python3
"""Prüft die Zeichenlimits des Agent Builders für Name, Beschreibung und Anweisungen."""
import pathlib
A = pathlib.Path(__file__).resolve().parent.parent / "agent"
checks = [("Name", "Ads-Builder Search", 30),
          ("Beschreibung", (A / "beschreibung.txt").read_text(encoding="utf-8").strip(), 1000),
          ("Anweisungen", (A / "anweisungen.md").read_text(encoding="utf-8").strip(), 8000)]
for label, text, limit in checks:
    print(f"{'OK ' if len(text) <= limit else 'ZU LANG'} {label}: {len(text)} / {limit} Zeichen")
