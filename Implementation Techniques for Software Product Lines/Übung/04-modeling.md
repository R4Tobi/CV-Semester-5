# Übungsblatt 4

## Aufgabe 1 Grundlagen zu Feature Modellen

### (a) Was ist ein Feature-Modell und wozu wird es verwendet?

- Ein **Feature-Modell** ist eine hierarchische Darstellung von Features (abstract & concrete) mit Baum- und Cross-Tree-Constraints. Es spezifiziert welche Kombinationen von Features in einer Produktlinie erlaubt sind (Validierungszweck, Kommunikation, Explizitmachung impliziten Wissens).
- Typische Zwecke: Definieren gültiger Konfigurationen/Produkte, Dokumentation von Abhängigkeiten, Basis für automatisierte Analysen (SAT/#SAT/AllSAT), Toolunterstützung für Konfiguratoren.

### (b) Erklärung des gegebenen Modells (Struktur & Constraints)

- **Struktur:** `MobileApp` als Root (immer erforderlich). `Login`, `Notifications`, `Payment`, `Analytics` sind Unterfeatures; `Login`, `Notifications`, `Payment` besitzen wiederum konkrete Login-/Payment-Optionen (Email/Google/Facebook, Push/InApp, CreditCard/PayPal/Voucher). (Semantik: Parent → Child, optionale vs. mandatory Markierung nicht explizit gegeben — Annahme: Kinder sind optional/konkret verständlich gemäß Diagrammnotation der Vorlesung.)
- **Constraints:**  
  - `Push -> Google` (wenn Push gewählt ist, muss Google Login gewählt sein).  
  - `Analytics -> CreditCard` (Analytics erfordert CreditCard Payment).  
  - `PayPal -> InApp` (PayPal erfordert InApp-Notifications / oder: InApp als Voraussetzung für PayPal).
  Diese Cross-Tree-Constraints sind propositional zu lesen (Implikation).

**Beispielkonfigurationen**:

- **Gültig (z. B. MobileApp mit Google-Login, Push, CreditCard, Analytics):**  
  `S = {MobileApp, Login, Google, Notifications, Push, Payment, CreditCard, Analytics}`  
  Begründung: `Push -> Google` erfüllt (Google ist gewählt). `Analytics -> CreditCard` erfüllt (CreditCard gewählt). `PayPal -> InApp` irrelevant (PayPal nicht gewählt). Somit ist die Konfiguration mit den Constraints konsistent.

- **Ungültig (Beispiel):**  
  `S = {MobileApp, Login, Email, Notifications, Push, Payment, Voucher}`  
  Begründung: `Push -> Google` wird verletzt, weil `Push` gewählt ist, aber `Google` nicht. Also ungültig.

## Aufgabe 2 Feature Modell Analyse

### (a) Ist das Feature-Modell inkonsistent?

**Antwort:** **Nein, konsistent.**  
Begründung (nach Vorlesungssemantik): `¬FLAC` ist eine Cross-Tree-Constraint, die FLAC in allen gültigen Produkten ausschließt (FLAC ist niemals wählbar), das allein führt nicht zu einem Widerspruch. Die übrigen Implikationen (`WiFi -> InternalMemory`, `Bluetooth -> InternalMemory`, `WiFi -> ¬SDCard`) erzwingen lediglich Abhängigkeiten, erzeugen aber keinen offensichtlichen Zyklus oder direkte Kontradiktion (z. B. keine Forderung `InternalMemory` = false). Daher existieren Konfigurationen (z. B. nur MP3, keine Connectivity, SDCard optional), also ist das Modell **nicht** void. (Definitionen und SAT-Begriffe siehe Vorlesung). :contentReference[oaicite:8]{index=8}

### (b) Welche Features sind *core* (immer ausgewählt) und welche *tot* (nie auswählbar)?

- **Core (nicht abwählbar):** Mindestens die Root `MusicPlayer` ist core (Root ist per Semantik immer erforderlich). Weitere core-Features können nur entstehen, wenn Constraints sie in allen gültigen Konfigurationen erzwingen — das ist hier **nicht** der Fall. Daher: **Nur `MusicPlayer` ist core.**
- **Tot (dead):** `FLAC` ist *tot*, da `¬FLAC` es in allen gültigen Konfigurationen verbietet. Andere Features sind potentiell wählbar abhängig von Entscheidungen (z. B. `InternalMemory` ist wählbar, wenn WiFi/Bluetooth gewählt werden). :contentReference[oaicite:10]{index=10}

### (c) Schlage eine neue Bedingung vor, die `Bluetooth` zu einem toten Feature macht

- Verwende ein Constraint, das `Bluetooth` zwingt, ein Feature zu haben, das aufgrund vorhandener Constraints verboten ist. Beispiel:  
  **Vorschlag:** `Bluetooth -> FLAC`  
  Da bereits `¬FLAC` gilt, würde `Bluetooth -> FLAC` bedeuten: wenn `Bluetooth` gewählt ist, muss `FLAC` gewählt sein - aber `FLAC` ist durch `¬FLAC` verboten. Somit wäre `Bluetooth` unkonfigurierbar (dead). Dieses Vorgehen folgt dem in der Vorlesung beschriebenen Prinzip (Cross-Tree-Constraint + bestehende Negation erzeugen Dead-Features).

### (d) Wie kann ein SAT-Solver angewendet werden, um (a) und (b) durchzuführen?

- **(a) Konsistenz prüfen (void/consistent):** FM → propositional formula Φ(FM) (siehe Vorlesung: Baum-Constraints + Cross-Tree → konjunktive Formel). Dann SAT(Φ(FM)) prüfen: Existiert eine erfüllende Belegung? Wenn `SAT` = wahr, Modell ist konsistent.
- **(b) Core/Dead bestimmen:**  
  - *Dead feature F:* Prüfe SAT(Φ(FM) ∧ F). Wenn unbefriedigbar (⊥), ist F dead.  
  - *Core feature F:* Prüfe SAT(Φ(FM) ∧ ¬F). Wenn unbefriedigbar, ist F core.  

## Aufgabe 3 Feature Modell Transformation

### (a) Wie viele Produkte beschreibt das Modell? (unter obiger Annahme)

- `Edges`: 2 Möglichkeiten — {Directed} **oder** {Undirected} (genau eins).
- `Algorithms` (OR-Gruppe): mögliche Nicht-leeren Teilmengen von {DFS, CycleDetector} → {DFS}, {CycleDetector}, {DFS, CycleDetector} (3 Möglichkeiten).  
  Aber `CycleDetector` ist nur zulässig, wenn `Directed` gewählt ist (Constraint `CycleDetector -> Directed`).
- **Fall1:** `Edges = Directed` → `Algorithms` kann sein: DFS, CycleDetector, oder beide → 3 Produkte.
- **Fall2:** `Edges = Undirected` → `CycleDetector` nicht erlaubt → only {DFS} möglich → 1 Produkt.
- **Gesamt:** `3 + 1 = 4` gültige Produkte (unter den getroffenen Annahmen).  
  (Explizite Produkte auflisten siehe Teil (c) unten.) :contentReference[oaicite:15]{index=15}

### (b) Allgemeines Vorgehen beim Bestimmen der Anzahl (und Schwierigkeit)

- Allgemeines Vorgehen (Vorlesung): Modell → formale Formel Φ(FM) (Propositionalformel) -> **#SAT** (Zählsolver) ausführen, um die Anzahl erfüllender Belegungen zu erhalten. Alternativ: AllSAT zur Aufzählung, falls sinnvoll.
- Schwierigkeit: #SAT/AllSAT skaliert schlecht bei vielen Features (kombinatorische Explosion). Gruppen und viele Cross-Tree-Constraints erschweren die Umwandlung und das Zählen; AllSAT kann unpraktikabel werden, weil Ergebnisgröße enorm ist. (Siehe Diskussion zu #SAT/AllSAT / Skalierbarkeit in der Vorlesung.)

### (c) (1) Aussagenlogische Formel (unter obiger Annahme)

Bezeichne Features als Variablen: `Graph`, `Edges`, `Directed`, `Undirected`, `Algorithms`, `DFS`, `CycleDetector`.

Φ(FM) = Graph ∧ (Edges -> Graph) ∧ (Edges <-> (Directed ∨ Undirected)) ∧ ¬(Directed ∧ Undirected) ∧ (Algorithms -> Graph) ∧ (Algorithms <-> (DFS ∨ CycleDetector)) ∧ (CycleDetector -> Directed)

### (c) (2) Menge aller gültigen Konfigurationen (unter Annahmen)

Auflistung der 4 gültigen Produkte (nur ausgewählte Features neben Root):

1. `{Graph, Edges, Directed, Algorithms, DFS}`  
2. `{Graph, Edges, Directed, Algorithms, CycleDetector}`  
3. `{Graph, Edges, Directed, Algorithms, DFS, CycleDetector}`  
4. `{Graph, Edges, Undirected, Algorithms, DFS}`

(Die Varianten unterscheiden sich darin, ob Directed/Undirected und welche Algorithmus-Kombinationen gewählt sind; `CycleDetector` erscheint nur in Fällen mit `Directed`.) :contentReference[oaicite:19]{index=19}

### (c) Vor- und Nachteile der Darstellungen / andere Sprachen

- **Diagramm (Feature Tree):** gut für Menschen, übersichtlich; aber semantische Details (z. B. komplexe Cross-Tree Constraints) nicht immer klar/formal.
- **Aussagenlogische Formel (Φ):** formal, für Solver geeignet; verliert teilweise hierarchische Struktur/Lesbarkeit.
- **Menge aller Konfigurationen (Produkt-Map):** präzise, aber bei vielen Features unhandlich (explodiert).
- **Andere Sprachen / Formate (Vorlesung nennt):** UVL (Universal Variability Language), DIMACS (für CNF / SAT solver). Vorteile: Textuell, maschinenlesbar; Nachteile: Transformationsaufwand, möglicher Strukturverlust.

## Aufgabe 4 — Feature-Modelle aus Anforderungen ableiten

### (a) Smart-Home-Steuergerät — Anforderungsliste

- Sprachsteuerung erfordert Mikrofon und Lautsprecher.
- Fernsteuerung über Smartphone erfordert WLAN.
- Benutzeroberfläche erfordert Touchscreen.
- Bewegungserkennung erfordert Infrarotsensor.
- Außeninstallation erfordert Wetterfestigkeit.

**Vorschlag für ein Feature-Modell (textuelle Beschreibung)**:

```plaintext
SmartHomeDevice
├─ Control {abstract}
│ ├─ VoiceControl (optional)
│ │ ├─ Microphone (mandatory if VoiceControl)
│ │ └─ Speaker (mandatory if VoiceControl)
│ └─ RemoteControl (optional)
│ └─ WiFi (required if RemoteControl)
├─ UI (optional)
│ └─ Touchscreen (required if UI)
├─ Sensors (optional)
│ └─ MotionDetection (optional)
│ └─ InfraredSensor (required if MotionDetection)
└─ Installation (optional)
├─ Indoor
└─ Outdoor (optional)
└─ WeatherProof (required if Outdoor)
```

- **Kommentare:** Jede Anforderung wurde als Parent→Child oder als Cross-Tree constraint modelliert (z. B. VoiceControl → Microphone ∧ Speaker). Diese Vorgehensweise entspricht den in der Vorlesung beschriebenen Patterns: Baumstruktur + Cross-Tree Constraints für komplexere Abhängigkeiten. :contentReference[oaicite:24]{index=24}

(Fehlende Abhängigkeiten / Hinweise: Man könnte z. B. angeben, ob `WiFi` allein genügt oder zusätzlich `RemoteControl` mandatory etc. — Domain-Scoping bleibt offen, was in der Vorlesung als Herausforderung genannt wird.) :contentReference[oaicite:25]{index=25}

### (b) Smartphone-Produktlinie — aus Beispielprodukten

**Beobachtungen aus den Beispielprodukten**:

- Variierende Display-Größen: 5.0", 5.5", 6.1", 6.5" → sinnvoll als *alternative* Gruppe (genau eine Displaygröße pro Produkt).
- Kameras: Frontkamera erscheint in allen Beispiele → evtl. core? (wenn wirklich in allen Produkten vorhanden), Rückkamera nur in einige → optional.
- Fingerabdrucksensor, NFC, WLAN, 5G: variieren → optionale Features.
  
**Vorsichtiges Feature-Modell (vereinfachte Textform):**

```plaintext
Smartphone
├─ Display (alternative) {5.0, 5.5, 6.1, 6.5}
├─ FrontCamera (maybe core, falls in allen Produkten vorhanden)
├─ RearCamera (optional)
├─ FingerprintSensor (optional)
├─ NFC (optional)
├─ WiFi (optional)
└─ Cellular (optional)
└─ 5G (optional; appears only in some products)
```

**Schwierigkeiten beim Ableiten aus wenigen Produkten**:

- **Unvollständigkeit:** Ein kleines Beispielset zeigt nur beobachtete Kombinationen — es sagt nichts über mögliche, aber nicht gezeigte Kombinationen oder notwendige Constraints aus. (Vorlesung: Domain scoping, Feature-interactions, fehlende Abhängigkeiten sind Probleme.)
- **Fehleranfälligkeit:** Man könnte fälschlich ein Feature als core markieren, obwohl es nur in der betrachteten Stichprobe auftaucht. Ebenso können Cross-Tree-Constraints verborgen bleiben.

## Aufgabe 5 — Wie viele Sandwiches gibt es bei Subway?

### (a) Versuch einer Näherung / Methode

**Wichtig:** Diese Aufgabe **kann nicht allein aus der Vorlesungspräsentation** beantwortet werden — sie benötigt das tatsächliche Bestellformular (Aufzählung von Brotsorten, Belägen, Saucen, Extras etc.). Ich habe deshalb ergänzende externe Informationen verwendet (Web-Archiv mit dem Bestellformular, wie im Aufgabenblatt verlinkt). **Diese Stelle ist explizit mit externen Quellen beantwortet.** (Quelle: Wayback Machine Kopie des Bestellformulars).

**Vorgehensweise (Näherungsansatz)**:

1. **Formular analysieren:** Zähle die Entscheidungen und deren Ausprägungen (z. B. Brotarten B, Belagarten L, Käsesorten K, Saucen S, Extras E, Toast/Toasting ja/nein).  
2. **Modellieren als Feature-Modell / Kombinatorik:** Für jede unabhängige Auswahl multipliziere die Anzahl der Optionen (sofern Optionen unabhängig sind). Bei optionalen Mehrfachauswahlen (z. B. Wähle beliebige 0..n Beläge) nutze Potenzmengen mit Einschränkungen (Anzahl erlaubter Beläge).  
3. **Berücksichtige Ausschlüsse / Abhängigkeiten:** Manche Kombinationen sind untersagt (z. B. Sauce nur, wenn Belag vorhanden), das reduziert die Gesamtzahl.  
4. **Näherung:** Wenn Formular sehr viele Mehrfachauswahl-Felder hat, wird die exakte Anzahl astronomisch groß; daher eine Näherung durch Produkt der (vereinfachten) Wahlräume oder Sampling.

**Ergebnis (qualitativ):** Bereits eine grobe Multiplikation typischer Felder (z. B. 6 Brotsorten × ~30 Beläge (Wahl beliebig) × 6 Käsesorten × 10 Saucen × 5 Extras × 2 Größen × 2 Toast-Optionen …) führt zu sehr großen Zahlen (Millionen bis viele Milliarden), besonders wenn mehrere Beläge in Kombination erlaubt sind (Kombinatorik der Potenzmenge). Eine genaue Zahl erfordert das konkrete Formular und ein zählendes Programm oder exakte Modellierung (AllSAT/#SAT) — dies wurde hier **nicht** komplett durchgerechnet. **(Externe Quelle: Wayback Machine Kopie des Formulars wurde konsultiert.)**

### (b) Kritik am Bestellformular (aus Product-Line-Ingenieur-Sicht)

- **Mehrfachauswahlfelder** (beliebig viele Beläge) führen zur Kombinatorikexplosion; erschweren exakte Zählungen. (Vorlesung: AllSAT skaliert schlecht; ähnliche Probleme hier.)
- **Intransparente Abhängigkeiten / Constraints:** Manche Kombinationen sind systemseitig oder logistisch ausgeschlossen; wenn diese nicht im Formular explizit ersichtlich sind, erschwert das genaue Modellieren. (Vorlesung: Konfiguratoren in der Wildnis zeigen oft fehlende Erklärungen/Fehler)
- **Fehlende Struktur:** Das Formular ist nicht als Feature-Modell formalisiert — dadurch fehlt maschinenlesbare Semantik, was die Analyse (Zählen, Prüfen) stark erschwert. (Vorlesung: Excel / Produktmap problematisch, besser formale Repräsentation wie UVL/DIMACS).
