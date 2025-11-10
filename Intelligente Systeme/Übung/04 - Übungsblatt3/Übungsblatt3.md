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

## Aufgabe 2 - Darstellung Boolescher Funktionen

- boolesche Funktion in DNF überführen (einheiltliche FOrm, algorithmus wird leichter)
  - durch die disjunktion von junktionen nur 2 schichten notwendig

### Vorgehensweise

1. Funktion in DNF überführen
2. Jedes Konjunktionsglieg auswerten
  - Gewichte:
    - w<sub>i</sub> = { +1, falls Literal x<sub>i</sub>; -1 falls Literal ¬x<sub>i</sub> vorkommt
  - Bias und Threshold
    - Anzahl positiver Literale = n -> Threshold
    - b<sub>j</sub> = -((Anzahl aller Literale) - 0.5)
      - Bei 3 Literalen liegt die Schwelle halb zwischen "alle erfüllt", also k
      - nächst niedriger fall wäre "eine bedingung nicht erfüllt", also k - 1
      - insgesamt ergibt sich dann k-0.5 (halb zwischen k und k-1)
3. Jede Disjuktion auswerten
  - Ausgabeneuron feuert, wenn ein neuron aus dem vorherigen schritt feuert
  - Gewichte:
    - w<sub>i</sub> = { +1, falls ein oder mehr neuronen feuern; 0 sonst
  - Bias und Threshold
    - Schwellenwert zwischen 0 und 1 = 0.5
    - θ ((Summe Neuronen aus Schicht 2) - 0.5)

## Aufgabe 4

Nein, geht nicht

- Schwellenneutron realisiert eine lineare Halbebene
- endlich kombination kann nur n-eckige Polygone abdecken
  - Kreis hat unendlich viele ecken -> unendliche vile halbebenen -> unendlich viele neuronen
- keine exakte darstellung möglich

**Annäherung mit 7 Neuronen**:

- 6 Neuronen (Sechseck) + 1 Output Neuron
- 6-Eck liegt im Kreis (innere Aproximation) -> keine false-positives
- punkte zwuschen den halbebenen und dem einheitskres währen false-negatives

Eingabe: (x, y)
Geraden des Sechseck: h<sub>k</sub> = θ(w<sub>k</sub> * x + b<sub>k</sub>)
Ausgabe: 1, wenn alle h<sub>k</sub> = 1

```plaintext
(x1,x2)
   ↓
[ H1 H2 H3 H4 H5 H6 ]   ← lineare Halbebenen (6)
   ↓
[ O1 (AND)]        ← Ausgabe: 1 falls innerhalb des Sechsecks
```

## Begriffe

### Perzeptron

- vereinfachtes künstliches neuronales Netz
- besteht aus einem künstlichen neuron
  - Gewichteungen und Schwellenwert anpassbar
- wandeln einen eingabevektor in einen ausgabevektor um

**Formeln und Formelzeichen**:

- Schwellenwert θ (Theta) [engl. threshold]
- Berechnung der Ausgabewerte: o<sub>j</sub> = { 1 Σ<sub>i</sub>(w<sub>ij</sub>x<sub>i</sub> + b) > 0 ; 0 sonst
