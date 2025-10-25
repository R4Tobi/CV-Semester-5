# Übungsblatt 2

## Aufgabe 1 Laufzeitvariabilität

### a) Definition

Fähigkeit eines Softwaresystems, sein Verhalten während der Ausführung dynamisch anzupassen, ohne dass derQuellcode neu kompiliert oder die anwendung neu gestartet werden muss

- dynamische Konfiguration, benutzergesteuert, Kontextabhängig, keine neukompilierung

### b) Reale Softwaresysteme mit Laufzeitvariabilität

- Webbrowser
  - Erweiterungen und Plugins
  - Feature-Flags
  - Rendering-Modi
  - Privacy-Modi
  - Themes
- Musikstreaming-Apps
  - Streaming Qualität
  - Offline-Modus
  - Crossfade
  - Datensparmodus
  - Equalizer

### c) Musik-Player-App Implementierung

#### Konfigurationsmöglichkeiten

- ´visualEqualizer´
- ´streamingQuality´
- ´theme´
- ´crossfade´

#### Methoden

- manuell:
  - Nutzer passt Konfiguration selbsständig an
- kontextbasiert
  - bestimmte features werden in bestimmtken kontexten aktiviert oder deaktiviert

#### Konflikte

**Resourcenkonflikt**:

- visualEqualizer: true, stramingQuality: high, theme: dark, crossfasde: 3s
- Akkuladung: 8%, Netzwerk 2G, CPU-Last: 85%

Visueller Equalizer + hohe Qualität führen zu:

- Schneller Akku-Entladung
- Buffering/Ruckeln
- App-Absturz möglich

**Feature-Abhängigkeiten**:

- visualEqualizer: true, stramingQuality: low, theme: dark, crossfasde: 5s

- Der Equalizer benötigt hochauflösende Audio-Daten 
für präzise Frequenzanalyse

#### Konflikterkennuung

- Präventiv:
  - Validierung der Eingaben
  - Modellieren von Prozessen unter Berücksichtigung aller Möglichkeiten
  - Deaktivierung/Aktivierung von Features
- Reaktiv:
  - Monitoring des Systemzustands
- Hybrid:
  - Validierung + kontinuierliches Monitoring
  - Benutzerbenachrichtigung bei Änderungen

### d) Vor und Nachtele Laufzeitvariabilität

| Vorteil          | Nachteil                         |
|------------------|----------------------------------|
| Flexibilität     | Performance-Overhead             |
| Personalisierung | Speicher-Overhead                |
| A/B-Testing      | Komplexität                      |
| Kontextanpassung | Aufwendiges Testen und Debugging |
|                  | Fehleranfälligkeit               |

## Aufgabe 2 Laufzeitvariabilität realisieren

### a) Variabiltät mit globalen Parametern

```java
public class GlobalConfig {
    public enum Mode { DRIVE, WALK, BIKE }
    public static Mode currentMode = Mode.DRIVE;
}

// Verwendung im Code:
if (GlobalConfig.currentMode == Mode.DRIVE) {
    // Routing, UI etc. für Drive-Modus
} else if (GlobalConfig.currentMode == Mode.WALK) {
    // Gehmodus-spezifisches Verhalten
} else {
    // Fahrradmodus
}
```

- Die Variable ist für alle Komponenten im System global zugänglich
- Ein Moduswechsel beeinflusst das Verhalten aller Teile der App direkt
- Modi können zur Laufzeit (z.B. durch den Nutzer) verändert werden

### b) Variabilität mit Methodenparametern

```java
public enum Mode { DRIVE, WALK, BIKE }

public class Navigation {
    public Route calculateRoute(Point from, Point to, Mode mode) {
        if (mode == Mode.DRIVE) {
            // Routing für Fahrmodus
        } else if (mode == Mode.WALK) {
            // Gehmodus
        } else {
            // Fahrradmodus
        }
        // ...
    }

    public void updateUI(Mode mode) {
        // UI für jeweiligen Modus anpassen
    }
}

// Aufruf:
Route route = navigation.calculateRoute(start, end, Mode.BIKE);
navigation.updateUI(Mode.BIKE);
```

- Jede Methode entscheidet basierend auf ihrem Parameter, welches Verhalten auszuführen ist
- Der Modus muss explizit beim Methodenaufruf übergeben werden.
- Es gibt keinen zentralen globalen Zustand

### c) Vergleich: Wartbarkeit und Flexibilität

| Aspekte      | Globale Parameter | Methodenparameter |
|--------------|-------------------|-------------------|
| Wartbakeit   | weniger wartbar, Änderungen wirken sich auf das gesamte System aus, erschweren Nachvollziehen von Abhängigkeiten | Modus wirk lokal und explizit weitergegeben, Komponenten sind weniger gekoppelt und besser testbar |
| Flexibilität | Einfach zu implementieren, aber weniger flexibel | Leichter um weitere Modi, spezielle Routing-Methoden oder parallele Nutzer-Sessions zu ergänzen |
| Risiko       | Fehlerquellen durch unbeabsichtigte Zustandsänderungen und Nebenwirkungen | Methoden sind isolierter, Fehler lassen sich einfacher auf Methoden-Ebene nachvollziehen und einschränken |

**FAZIT**: Die Lösung mit Methodenparametern ist für komplexe oder skalierende Apps einfacher zu warten und besser testbar. Sie erlaubt mehr Flexibilität für zukünftige Updates, da Verhalten gezielt pro Methode und pro Aufruf konfiguriert werden kann, ohne dass ein globales Systemverhalten unbeabsichtigt beeinflusst wird

### d) Implementierung

```java
// Enum for travel modes
enum Mode { 
    DRIVING, 
    WALKING, 
    CYCLING 
}

class Navigator {
    Navigator() {
    }
    
    /**
     * Navigate using the specified mode
     * @param route The route to navigate
     * @param mode The travel mode to use
     */
    void navigate(Route route, Mode mode) {
        // Logic based on mode parameter
        if (mode == Mode.DRIVING) {
            System.out.println("Calculating driving route...");
            calculateDrivingRoute(route);
            applyDrivingUI();
        } else if (mode == Mode.WALKING) {
            System.out.println("Calculating walking route...");
            calculateWalkingRoute(route);
            applyWalkingUI();
        } else if (mode == Mode.CYCLING) {
            System.out.println("Calculating cycling route...");
            calculateCyclingRoute(route);
            applyCyclingUI();
        }
    }
    
    // Mode-specific route calculation methods
    private void calculateDrivingRoute(Route route) {
        System.out.println("Using highways and main roads");
        System.out.println("Avoiding pedestrian zones");
        System.out.println("Estimated speed: 50-130 km/h");
    }
    
    private void calculateWalkingRoute(Route route) {
        System.out.println("Using sidewalks and pedestrian paths");
        System.out.println("Including shortcuts through parks");
        System.out.println("Estimated speed: 5 km/h");
    }
    
    private void calculateCyclingRoute(Route route) {
        System.out.println("Preferring bike lanes");
        System.out.println("Avoiding steep hills when possible");
        System.out.println("Estimated speed: 15-25 km/h");
    }
    
    // Mode-specific UI adjustments
    private void applyDrivingUI() {
        System.out.println("UI: Large buttons, voice navigation");
    }
    
    private void applyWalkingUI() {
        System.out.println("UI: Detailed street view, POI markers");
    }
    
    private void applyCyclingUI() {
        System.out.println("UI: Elevation profile, bike shop locations");
    }
}

class Route {
    // Simple placeholder class for route data
    private String startLocation;
    private String endLocation;
    
    Route(String start, String end) {
        this.startLocation = start;
        this.endLocation = end;
    }
}

public class Main {
    public static void main(String[] args) {
        // Create routes
        Route route1 = new Route("Home", "Office");
        Route route2 = new Route("Park", "City Center");
        Route route3 = new Route("Station", "University");
        
        // Create navigator
        Navigator nav = new Navigator();
        
        // Navigate with different modes
        System.out.println("\n=== Commute to work ===");
        nav.navigate(route1, Mode.DRIVING);
        
        System.out.println("\n=== Morning exercise ===");
        nav.navigate(route2, Mode.WALKING);
        
        System.out.println("\n=== Eco-friendly travel ===");
        nav.navigate(route3, Mode.CYCLING);
        
        // same navigator, different modes
        System.out.println("\n=== Returning home (cycling) ===");
        nav.navigate(route1, Mode.CYCLING);
    }
}
```

## Aufgabe 3 Design Patterns für Laufzeitvariabilität

### a) Design Patterns

Design Patterns (Entwurfsmuster) sind wiederverwendbare Lösungsschablonen für häufig auftretende Entwurfsprobleme in der Softwareentwicklung.
Sie bieten abstrakte, bewährte Strukturen und Kommunikationswege, um Code flexibler, wartbarer, erweiterbarer und verständlicher zu machen.

**Allgemeiner Zweck**:

- Erhöhen Wartbarkeit durch Entkopplung von Komponenten
- unterstützen flexibilität bei erweiterung
- erleichtern kommunikation im team
- fördern wiederverwendbarkeit

### b) Pattern für Kaffeemaschine

**Decorator**:

- Anzahl an Getränkevarianten wächst exponentiell mit jeder weiteren ZUtat
- Grundklasse kann zur Laufzeit beliebig erweitert werden
- man muss nicht alle kombinationen als klasse abbilden

### c) Pseudo Code

```java
interface Beverage {
    String getDescription();
    double getCost();
}

class Espresso implements Beverage {
    public String getDescription() { return "Espresso"; }
    public double getCost() { return 2.0; }
}

abstract class BeverageDecorator implements Beverage {
    protected Beverage beverage;
    public BeverageDecorator(Beverage beverage) { this.beverage = beverage; }
}

class MilkDecorator extends BeverageDecorator {
    public MilkDecorator(Beverage beverage) { super(beverage); }
    public String getDescription() { return beverage.getDescription() + ", mit Milch"; }
    public double getCost() { return beverage.getCost() + 0.4; }
}

class SugarDecorator extends BeverageDecorator {
    public SugarDecorator(Beverage beverage) { super(beverage); }
    public String getDescription() { return beverage.getDescription() + ", mit Zucker"; }
    public double getCost() { return beverage.getCost() + 0.2; }
}

// Verwendung:
Beverage b = new Espresso(); // Basisgetränk
b = new MilkDecorator(b);    // Milch hinzufügen
b = new SugarDecorator(b);   // Zucker hinzufügen

System.out.println(b.getDescription());
System.out.println(b.getCost());
```

### d) Laufzeit Konfigurationsänderung während der Zubereitung

**Was kannn schiefgehen?**:

- zutat wird abgewählt, während sie hinzugefügt wird (-> transaction lock)
- inkonsistente Ergebnisse: Getränk entspricht nicht mehr der aktuellen Konfiguration (-> Änderungen erst beim nächsten Auftrag zulassen, Nutzer Feedback geben)
- Fehlermeldungen, Hardwarekonflikte, stillstehende Maschine

### e) Implementierung ohne Design Pattern

- Implementierung auch ohne Design Pattern möglich

```java
if (type == ESPRESSO && milk && sugar) { /*...*/ }
```

- Kaum wartbar bei vielen Varianten, Erweiterung oft fehleranfällig
- redundante if-else/switch strukturen

## Aufgabe 4 Parameter oder Design Patterns

### a) Probleme der aktuellen Implementierung

- verletzung des open-closed-prinzips -> jeder neue Ausgabe typ erfordert änderung an der playsound methode
- globalekonfiguration ist starr gekoppelt -> schwer testbar und fehleranfällig
- kein dynamisches umschalten -> Änderungen an der Config erfordern möglicherweise neusart oder führen zu inkonsistenten zuständen
- hohe kopplung, keine abstraktion
