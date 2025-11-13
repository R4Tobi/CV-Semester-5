# Übungsblatt 5

## Aufgabe 1 Präprozessor-basierte Variabilität

### (a) Was ist ein Präprozessor und wie unterstützt er die Implementierung von Variabilität in Software-Produktlinien

- manipuliert den Quellcode vor der Kompilierung
- integrieren von header- oder inline-files
- definieren und erweitern von Makros
- Konditionelle Kompilierung (entfernen von Debug-Code für Release-Build)

### (b) Erkläre die Rolle des Präprozessors in diesem Code

1. Bedingte kompilierung
  1. Präzision, Temperatureinheit, Modus und Sensor könnnen mit wahr/falsch belegt werden -> Nur aktivierte Bereiche landen tatsächlich im Programm
2. Typ- und Genauigkeitswahl
  1. Präprozessor entscheidet, welcher datentyp und welche Genauigkeit verwendet wird -> `PRECISION_HIGH` verwendet double und kleiner Toleranz, normal wäre float und größere Toleranz
3. Einheitenumrechnung durch Makros
  1. Präprozessor definiert, wie sensordaten interpretiert werden -> `CONVERT(x) wird später im Code ersetzt`
4. Sensorkonfiguration
  1. Bestimmte Konstanten und Funktionen werden aktiviert (Anzahl der Sensoren)

### (c) Angenommen, PRECISION HIGH, UNIT KELVIN, MODE THERMAL und SENSOR ADVANCED sind definiert, w¨ahrend EPSILON, SENSOR COUNT, CONVERT und p t außerhalb des gegebenen Code-Snippets nicht vordefiniert sind. Gib den resultierenden Quellcode an, wie er nach dem Preprocessing erscheinen würde, mit allen expandierten Makros und aufgelöster bedingter Kompilierung

```cpp
// PRECISION_HIGH, UNIT_KELVIN, MODE_THERMAL, SENSOR_ADVANCED

void readSensor() {
    // MODE_THERMAL ist definiert → Schleife wird aktiviert
    // SENSOR_COUNT wurde zu 3 expandiert
    for (int i = 0; i < 3; ++i) {

        // p_t wurde durch double ersetzt (wegen PRECISION_HIGH)
        // READ_RAW(i) → (300 + (i) * 10) (wegen SENSOR_ADVANCED)
        // CONVERT(x) → ((x) * 0.1 + 273.15) (wegen UNIT_KELVIN)
        double value = ((300 + (i) * 10) * 0.1 + 273.15);

        // EPSILON wurde zu 0.000001 (wegen PRECISION_HIGH)
        if (value > 0.000001)
            printf("Sensor[%d] active: %.2f\n", i, value);
    }

    // Der else-Zweig ("Thermal mode disabled.") wurde entfernt, da MODE_THERMAL definiert ist.
}
```

### (d) Verschiedene Präprozesoren

| Präprozessor | Eigenschaften | Vorteile | Nachteile | Geeignet für |
|---------------|---------------|-----------|------------|---------------|
| **CPP (C Preprocessor)** | Ursprünglich für C/C++-Code entwickelt; arbeitet textbasiert; nutzt Direktiven wie `#define`, `#ifdef`, `#include`. | Weit verbreitet, einfach, direkt in viele Compiler integriert. | Keine Kenntnis der Zielsprache -> kann fehleranfällig bei Nicht-C-Code sein; schwierige Wartbarkeit bei großen Projekten. | C/C++-Projekte, eingebettete Systeme, Plattformabhängige Konfigurationen im Quellcode. |
| **Munge** | Speziell für Java und ähnliche Sprachen entwickelt; berücksichtigt Sprachsyntax und Kommentare. | Syntaxbewusst -> geringere Gefahr von Syntaxfehlern; besser lesbare Konfigurationen. | Weniger verbreitet; zusätzlicher Installations- und Integrationsaufwand. | Java-basierte Projekte, plattformübergreifende Builds, situationsabhängige Codeaktivierung in Java. |
| **Antenna** | Build-System-Erweiterung für mobile Java-Entwicklung; integriert in Ant-Builds. | Gute Integration in Ant; unterstützt Ressourcen-, Build- und Präprozess-Steuerung | auf mobile Entwicklung zugeschnitten; eingeschränkt außerhalb des Ant-Ökosystems. | Mobile/Embedded-Java-Projekte |

## Aufgabe 2

### (a) Rolle von KConfig, KBuild, CPP und MenuConfig

- KConfig: definiert, welche Optionen es gibt (Features, Treiber und Architekturen)
- MenuConfig: Benutzerschnittstelle, um diese Optionen komfortabel auszuwählen
- KBuild: sorgt technisch dafür, dass der richtige Code kompiliert wird
- CPP: steuert dann auf Quellcodeebene, welcher Code tatsächlich kompiliert wird

### (b) KBuild

#### (1)

- `obj-y += core/`: core/-Verzeichnis wird fest in den Kernel eingebut
  - `obj-y` enthält alle objekte, die in das kernel image integriert werden -> Basisfunktionalität
- `obj-m += net/`: net/-verzeichnis wird kompiliert, programme landen aber nicht im Kernel-Image
  - können später zur Laufzeit modular geladen werden
- `obj-$(CONFIG_USB_SUPPORT) += drivers/usb/`: USB Treiber wird nur dann in das Kernel-Image installiert, wenn `obj-y` oder `obj-m`
- `obj-$(CONFIG_DEBUG_MODE) += debug/`: gleiches Prinzip wie bei USB, baue Debug-Code nur, wenn Debugging aktiviert ist

#### (2)

- core wird fest in das Kernel-Image geladen
- net wird modular installiert
- USB-Treiber wird nicht installiert
- Debug Code wird in das Kernel-Image geladen

#### (3)

| Aspekt | Feature-Implementierung mit Build-Systemen | Clone-and-Own mit Build-Systemen |
|---------|------------------------------------------------------------|-----------------------------------|
| **Grundprinzip** | Eine gemeinsame Codebasis mit konfigurierbaren Features. | Separate Codekopien für jede Variante oder jedes Produkt. |
| **Variabilitätsmechanismus** | Nutzung von Konfigurationsoptionen (z. B. `CONFIG_*`) und bedingtem Kompilieren (`obj-$(...)`, `#ifdef`). | Unterschiedliche Projektverzeichnisse oder Branches, die unabhängig gebaut werden. |
| **Wartbarkeit** | Hohe Wartbarkeit, da alle Varianten dieselbe Codebasis teilen. | Geringe Wartbarkeit, da Änderungen mehrfach in verschiedenen Kopien vorgenommen werden müssen. |
| **Codewiederverwendung** | Sehr hoch – gemeinsame Nutzung von Modulen und Features. | Niedrig – Code wird oft dupliziert statt geteilt. |
| **Fehleranfälligkeit** | Geringer, da Änderungen zentral verwaltet werden. | Höher, da Divergenzen zwischen Kopien entstehen können. |
| **Build-Komplexität** | Komplexes Build-System (z. B. KBuild, CMake) notwendig, um Varianten zu steuern. | Einfachere Build-Skripte, da jede Variante eigenständig ist. |
| **Einsatzgebiet** | Geeignet für große, variantenreiche Systeme wie den Linux-Kernel oder SPLs. | Häufig bei kleinen Projekten oder schnellen Prototypen ohne Langzeitpflege. |
| **Beispiel** | Linux-Kernel: Features über `KConfig` und `KBuild` wählbar. | Kopieren eines bestehenden Projekts, um eine neue Produktversion zu erstellen. |

## Aufgabe 4

### (a) Feature Traceability – Erklärung und Herausforderungen

**Feature Traceability (Rückverfolgbarkeit)** bezeichnet die Fähigkeit,  
eine direkte Verbindung zwischen einem *Feature* (z. B. „High Precision“)  
und seiner **Implementierung im Code**, **Dokumentation** oder **Build-Konfiguration** herzustellen.  
Sie ermöglicht, Änderungen, Fehler und Verantwortlichkeiten klar einem Feature zuzuordnen.

#### Herausforderungen

1. **Tangling (Verflechtung):**  
   - Mehrere Features beeinflussen denselben Codeabschnitt.  
   - → Schwer zu erkennen, welches Feature welchen Effekt hat.  
   - *Im Beispiel:* `computePower()` enthält Code für `SENSOR_ADVANCED`, `APPLY_SCALING`, `DEBUG` und `APPLY_LOGGING` gleichzeitig.

2. **Scattering (Zerstreuung):**  
   - Ein einzelnes Feature ist über viele Code-Stellen verteilt.  
   - → Rückverfolgbarkeit wird erschwert, da Feature-Logik über mehrere Orte verstreut ist.  
   - *Im Beispiel:* Das Feature `APPLY_LOGGING` betrifft mehrere Codebereiche (z. B. Logging, Skalierung, Sensordaten).

3. **Replikation (Duplikation):**  
   - Ähnliche oder gleiche Codefragmente für verschiedene Feature-Kombinationen.  
   - → Erhöht Wartungsaufwand und Inkonsistenzrisiko.  
   - *Im Beispiel:* Sensorwerte werden in beiden Zweigen (`SENSOR_ADVANCED`, `SENSOR_BASIC`) ähnlich verarbeitet.

**Bewertung für das Beispiel**:

- **Tangling:** Hoch (mehrere Feature-Direktiven im selben Methodenblock).  
- **Scattering:** Mittel (z. B. Logging und Skalierung verteilt).  
- **Replikation:** Gering bis mittel (ähnliche Logik mehrfach implementiert).

### (b) Konsequenzen von Tangling, Scattering und Replikation

| Problem | Konsequenzen |
|----------|---------------|
| **Tangling** | Schwer nachvollziehbare Feature-Interaktionen; höheres Fehlerrisiko bei Änderungen; schwieriger Test und Debugging. |
| **Scattering** | Erschwerte Wartung, da Feature-Änderungen an vielen Stellen erfolgen müssen; Gefahr von Inkonsistenzen. |
| **Replikation** | Redundanter Code; erhöhter Pflegeaufwand; Risiko widersprüchlicher Änderungen zwischen Varianten. |

### (c) Möglichkeiten zur Sicherstellung von Feature Traceability

| Ansatz | Beschreibung | Vorteile | Nachteile |
|---------|---------------|-----------|------------|
| **Naming-Konventionen & Kommentare** | Einheitliche Benennung (`// FEATURE: LOGGING`) oder Tags in Code-Kommentaren. | Einfach, keine Tools nötig, schnell umsetzbar. | Nicht formal überprüfbar, leicht inkonsistent. |
| **Feature-Modularisierung** | Saubere Trennung von Features in eigene Klassen, Pakete oder Module. | Gute Nachvollziehbarkeit, geringes Tangling. | Erfordert refactoring; höhere Komplexität bei Abhängigkeiten. |
| **Variability Management Tools** (z. B. FeatureIDE, pure::variants) | Verknüpfen Feature-Modelle mit Code-Artefakten. | Automatische Traceability, konsistente Variantenbildung. | Hoher Einführungsaufwand, Tool-Abhängigkeit. |
| **Build-System-Verknüpfung** | Nutzung von Build-Konfigurationen (z. B. `CONFIG_*`, Präprozessor-Makros). | Gute Integration in Entwicklungsprozess; automatisierbar. | Rückverfolgung nur über Build-Kontext, nicht direkt im Code sichtbar. |
| **Annotations / Meta-Informationen** | Verwendung von Attributen oder Annotationen zur Markierung von Feature-Code. | Maschinell auswertbar; unterstützt Analyse-Tools. | Nicht in allen Sprachen/Tools nativ unterstützt. |

## Aufgabe 5

| Aspekt | Features mit Präprozessoren | Features mit Build-Systemen |
|---------|------------------------------|------------------------------|
| **Grundidee** | Bedingte Kompilierung innerhalb des Quellcodes durch Direktiven (`#ifdef`, `#define`, etc.). | Steuerung der Feature-Einbindung über Build-Konfigurationen (z. B. KBuild, Makefiles, CMake). |
| **Variabilitätsebene** | Innerhalb des Codes (Quellcode-Ebene). | Auf Projektebene (Dateien, Module, Build-Regeln). |
| **Beispiel** | `#ifdef DEBUG` → bestimmte Codeblöcke werden nur bei Debug-Builds kompiliert. | `obj-$(CONFIG_USB_SUPPORT) += drivers/usb/` im Linux-Kernel-Buildsystem. |
| **Vorteile** | - Hohe Flexibilität, da Variabilität direkt im Code steuerbar ist.<br>- Geringer Overhead, kein externes Build-Tool nötig.<br>- Feingranulare Anpassung einzelner Codezeilen möglich. | - Saubere Trennung von Code und Variabilitätslogik.<br>- Bessere Wartbarkeit und Übersichtlichkeit.<br>- Automatisierte Variantenbildung und Modulerzeugung möglich. |
| **Nachteile** | - Code wird schnell unübersichtlich („#ifdef-Hölle“).<br>- Erhöhtes Risiko für Fehler (z. B. bei mehrfachen Makrodefinitionen).<br>- Erschwerte Rückverfolgbarkeit und Testbarkeit. | - Geringere Granularität (Variabilität meist auf Modul-/Dateiebene).<br>- Höherer Initialaufwand bei der Einrichtung des Build-Systems.<br>- Abhängigkeit von externen Tools. |
| **Wartbarkeit** | Niedrig bei wachsender Anzahl an Features (starke Verflechtung). | Hoch, da Features modular und konfigurierbar sind. |
| **Feature Traceability** | Schwierig – Feature-Logik ist über viele `#ifdef`-Blöcke verteilt (Tangling/Scattering). | Besser – klare Zuordnung über Build-Regeln und Konfigurationsdateien (`KConfig`, `Makefile`). |
| **Typische Anwendungsfälle** | - Embedded-Systeme oder C-basierte Software mit geringen Ressourcen.<br>- Kleine Projekte mit wenigen Varianten.<br>- Feingranulare Hardwareanpassung. | - Große Software-Produktlinien (z. B. Linux-Kernel, Android).<br>- Projekte mit klar getrennten Modulen oder konfigurierbaren Komponenten. |
| **Bezug zur Vorlesung** | Beispiel: Temperaturüberwachungssystem mit Präprozessor-Makros (`PRECISION_HIGH`, `MODE_THERMAL`). | Beispiel: Linux-Kernel mit `KConfig` und `KBuild` zur Feature-Auswahl und Modulsteuerung. |
