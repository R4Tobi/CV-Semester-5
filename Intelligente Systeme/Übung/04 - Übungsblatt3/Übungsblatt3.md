# Übungsblatt 1

## Aufgabe 1 - Netze von Schwellenwertelementen

### (1) Neuronales Netz

Wenn der Punkt im Dreieck liegt, gebe 1, ansonsten 0 zurück.

Idee: Lösen über Ungleichungen, die Prüfen, ob ein Punkt im Dreieck liegt

- Ein Punkt liegt genau dann im Dreieck, wenn x >= 1, y <= 1 und x + y <= 4 sind

Ungleichungen mit Gewichten kombinieren:

u = w1\*x + w2\*y + b

Daraus ergeben sich Schwellenwerte:

- w = (1,0), b = -1 (u = 1, wenn x >= 1; x - 1 >= 0)
- w = (0,1), b = -1
- w = (-1,-1), b = -4

Ausgabe Neuron (Kombination aus allen Gewichten)

- Alle Bedingungen sind erfüllt -> logisches UND
- 3 Fälle: 0, 1/2 und 3
- Neuron soll nur im Fall 3 aktiviert werden

n1 + n2 + n3 = 3 muss gelten für n1 + n2 + n - θ >= 0

### (2) nicht-konvexe Polygone

- Dreicke (konvexe Mengen) können durch die schnittmenge von halbräumen beschrieben werden, nicht-konvexe nicht
- Problem ist nicht-darstellbarkeit von unkonvexen polygonen

**Lösungsmöglichkeiten**:

- Zerlegung in konvexe Teilgebiete (Dreiecke) -> Innerhalb des Dreiecks AND und insgesamt alle Dreicke mit einem OR verknüpfen
- Mehrschichtiges Perzeptron

## Begriffe

### Perzeptron

- vereinfachtes künstliches neuronales Netz
- besteht aus einem künstlichen neuron
  - Gewichteungen und Schwellenwert anpassbar
- wandeln einen eingabevektor in einen ausgabevektor um

**Formeln und Formelzeichen**:

- Schwellenwert θ (Theta) [engl. threshold]
- Berechnung der Ausgabewerte: o<sub>j</sub> = { 1 Σ<sub>i</sub>(w<sub>ij</sub>x<sub>i</sub> + b) > 0 ; 0 sonst
