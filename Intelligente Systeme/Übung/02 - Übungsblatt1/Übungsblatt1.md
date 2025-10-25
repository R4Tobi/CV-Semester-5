# Übungsblatt 1

## Aufgabe 1 - das chinesische Zimmer

### a) WOrin besteht das Gedankenexperiment

- beschreit einen Menschen, der durch reine Symbolverarbeitung sinnvolle chinesische ANtworten produzieren kann
- er besitzt kein verständnis für die chinesische sprache
- er benutzt nur ein handbuch mit regeln, um zeichen zu verarbeiten und zu antworten
- Computer, der ein Programm ausführt

### b) Argument

- argument dagegen, dass computer die programme ausführen bewusstsein oder verständnis erlangen können
- Computer kann den Anschein von Verstehen erwecken (wie im Turing-Test)
- besitzt aber keine semantik oder intentionalität
- argument richtet sich gegen die gleichstellung der begriffe "intelligentem verhalten" und "geistigem zustand"

### c) Zusammenhang mit dem Turingtest

- prüft, ob eine Maschine im Gespräch mit Menschen nicht von einem Menschen unterschieden werden kann
- experiment zeigt, das turing-test kein ausreichendes Kriterium für intelligenz ist

## Aufgabe 2

### a) Parkplatzschranke

- Wahrnehmung: Sensoren
- Aktion: Schranke schließen/öffnen
- Ziele: keine Eigenen Ziele
- Umgebung: Parkplatzzufahrt

-> Reaktiver Agent

### b) Ameisennest

- Wahrnehmung: Chemosensoren, Tastsinn
- Aktion: Transportieren, Graben/Bauen, Kämpfen
- Ziele: Nahrung sammeln, Nest ausbauen und schützen
- Umgebung: Wald,bodennah

-> sozialer Agent

### c) RoboCup Fußballteam

- Wahrnehmung: Sensoren (Kameras, ENtfernungsmesser)
- Aktion: Bewegung, Ballinteraktion
- Ziele: Tore schißen, Spiel gewinnen
- Umgebung:Fußballfeld

-> situierter Aent

### d) AlphaFold

- Wahrnehmung: Sequenzdaten, Datenbankeinträge
- Aktion: Berechnung/Vorhersage Proteinstruktur
- Ziele: Maximal Genauigkeit
- Umgebung: Virtuelle Daten und Wissensumgebung

-> refletiver Agent

### e) ChatGPT

- Wahrnehmung: Nutzereingaben
- Aktion: Texterzeugung, Bilderzeugung
- Ziele: Problemlösung und Unterstützung
- Umgebung: Digitale Umgebung, Internet

-> autonomer Agent

## Aufgabe 3

### Was passiert ohne die Voraussetzung

- Agent bleibt in schmalen Durchgängen hängen
- Agent kann dem Umriss nicht vollständig abfahren
- Agent kann nicht erkennen, ob er eineUnterscheidung zwischen Objekt- und Raumumrissen oder SAckgassen braucht

### Kann ein Regelsystem helfen

erweiterte Regelmechanismen und zusätzliche Wahrnehmung: Speicherung von Sensorzuständen, Nutzung temporaler/räumlicher Information, Merkmalsvektoren -> Teilweise Lösung des Problems

- Eigener Bewegungsablauf kann analysiert werden
- temporäremarkierungen, um einen Rückweg zu finden
- Merkmalsvektoren und Umgebungsmodelle nutzen, um Engstellen zu identifizieren und gezielt zu verlassen

## Aufgabe 4

### Regelsystem für Umrissabfahren (keine engen Zwischenräume)

1. Wenn der rechte Sensor (s3) frei ist:
→ Drehe nach rechts, gehe vorwärts.

2. Sonst, wenn der vordere Sensor (s2) frei ist:
→ Gehe vorwärts.

3. Sonst:
→ Drehe nach links.

Der Agent prüft also zuerst (priorisiert) die Möglichkeit, nach rechts zu ziehen (dem Umriss folgen),
dann nach vorne (dem Umriss entlang gehen), und dreht andernfalls nach links, falls er vor einer Wand steht.
Mit diesem Regelsatz kann der Agent den äußeren oder inneren Umriss eines Objekts oder Raumes abfahren.

### Regelsystem mit engen Zwischenräumen

reiner Stimulus-Response-Agent (ohne Gedächtnis/Zustandsspeicherung) kann dieses Problem nicht sicher lösen (Deadlocks/Traps)

**Erweiterungen**:

- Zusatzmerkmale aus Sensordaten (Historie, Richtungswechsel) in Entscheidungsregeln einbauen
- Mit Speichern und Zuständen arbeiten (besuchte wände/orte markieren)
