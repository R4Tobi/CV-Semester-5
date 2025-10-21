# Übung 1

## Aufgabe 1

### a) Unterschied maßgeschneiderter und massenproduziertem Rucksack

| Kriterium | Maßgeschneiderter Rucksack | Massenproduzierter Rucksack |
| --- | --- | --- |
| Individualität | Genaue Brücksichtigung von Kundenwünschen | Alle Rucksäcke sind nahezu identisch |
| Produktion | Einzelanfertigung, manuell und in kleinserie | serienanfertigung, hohe stückzalen |
| Kosten | Hoch, da viel Handabrbeit und indisidulle Planung | niedrig, durch skalierung und automation |
| Lieferzeit | eher lang | eher kurz, durch lagerung |

### b) Wäre Mass Customization sinnvoll für Rucksäcke?

**Vorteile**:

- Kundenorientierung
- Wirtschaftlichkeit

**Nachteile**:

- Komplexere Logistik und Produktion
- Initial größere Investition in Technologie

## Aufgabe 2

### a) Ablauf: Vom Zusammenstellen bis zum servieren

1. Kunde betritt die Domäne
  - Domäne in dem Fall: Fast Food + anpassbare Mahlzeiten
2. Kunde wählt Features aus
  - Brotort, Fleischsorte, Salat, Soße, Beilage, etc.
3. Kunde erstellt eine Konfiguration
  - Brioche, Rind, Eisberg, BBQ, Pommes
4. System prüft Abhängigkeit und Konflikte
  - z.B. veganer Patty + Kuhmilchkäse -> veganität geht verloren
5. Produkt wird produziert
  - Küche erhält die KOnfiguration und bereitet das Gericht zu
6. Produkt wird serviert
  - Endergebnis der Feature Kombination

### b) Menü mit 10 Features

- Basis (Hauptgericht): Burger, Wrap, Bowl
- Brotart: Sesam, Vollkorn, glutenfrei, Brioche
- Protein: Rind, Hähnchen, Falafel, Beyond Meat (vegan)
- Käse: Cheddar, Gouda, veganer Käse, kein Käse
- Soße: BBQ, Knoblauch, Chili, vegane Mayo, ohne Soße
- Toppings: Salat, Tomate, Gurke, Jalapeños, Zwiebeln
- Beilage: Pommes, Süßkartoffel-Pommes, Salat, Onion Rings
- Getränk: Cola, Wasser, Eistee, Smoothie
- Dessert: Brownie, Obstsalat, Eis, keiner
- Extras: Doppelt Fleisch, Extra Käse, Extra Soße
- Verpackung: Zum Mitnehmen, Vor Ort essen

### c) Abhängigkeiten und Konflikte

#### Abhängigkeiten

- veganer Patty verlangt vegane Soße und Käse
- glutenfreies Brot, vegane Pattys: verlangen separate zubereitung

#### Konflikte

- Doppelt Fleisch + Vegan (müsste doppet Patty sein)
- Wrap + extra brötchen

### d) Unterschied zwischen dem Verkauf von Fast Food (Hardware) und Software

| Aspekt | Fast Food / Hardware | Software |
|---------|----------------------|-----------|
| **Physisch / digital** | Physische Produkte, die Zutaten und Materialien benötigen. | Digitales Produkt, reine Information. |
| **Produktion** | Jedes Produkt muss physisch hergestellt werden. | Kann unendlich oft kopiert und verteilt werden. |
| **Kostenstruktur** | Variable Kosten pro Stück (Zutaten, Arbeitszeit). | Hohe Entwicklungskosten, aber niedrige Stückkosten. |
| **Anpassung** | Begrenzte Anzahl an Kombinationen, durch Zutaten beschränkt. | Theoretisch unbegrenzte Anpassbarkeit (durch Code). |
| **Lieferung** | Physisch – Kunde muss vor Ort sein oder Lieferung erhalten. | Digital – sofortiger Download oder Cloud-Nutzung. |
| **Änderungen / Updates** | Nachträglich kaum möglich („Burger kann man nicht updaten“). | Software kann leicht aktualisiert oder gepatcht werden. |

## Aufgabe 3

### a) Was versteht man unter einer Software-Produktlinie

- Grupper verwandter Softwareprodukte
- gemeinsame Architektur und Menge an Kernkomponenten
- Unterscheiden sich in bestimmten Merkmalen (Features)

### b) Wann und warum sollten Software-Produktlinien eingesetzt werden?

#### Wann

- wenn mehrer ähnliche Produkte entwickelt werden
- Produkte sich regelmäßig weiterzuentwickeln, aber viele Gemeinsamkeiten hbane
- wiederverwendung von software-komponenten sinnvoll ist

#### Warum

- Effizienz: Gemeinsame Codebasis spart Entwicklungszeit
- Wiederverwendete, getestete komponenten verringern fehler
- schneller markteinführung für neue varianten
- bessere wartbarkeit, weil kernsysteme gleich
- bessere skalierbarkeit, weil produkte sich besser ableeiten lassen

### Sind die folgenden Systeme SPLs

| System            | SPL?      | Begründung |
|-------------------|-----------|------------|
| Linux             | ja        | sehr viele varianten, die auf demselben Kernel basieren, Produktlinie nur der Kernel (~20k Features), nicht Distributionen |
| VSCode            | teilweise | Basisprodukt mit Erweiterungen auf sehr vielen Plattformen (Web, Desktop, SAP Build Code), es bleibt aber die gleiche Anwendung |
| HP Printer Driver | ja        | Gemeinsame Basisoftware für viele Modelle, gerätespezifische Module unterscheiden sich |
| Microsoft Office  | ja        | Gemeinsame codebasis, gerade in der UI, klassische varianten word/excel/powerpoint |
| Spotify           | nein      | gibt verschiedene plattformen, es bleibt aber eine app |
| Minecraft         | teilweise | varianten java/bedrock/pe, wurden separat entwickelt, daher eher SPL, aber auch nicht wirklich. mögliches Argument: Mods-Ökosystem |

### weitere Beispiele

#### Software Produktlinien

- Android (basiert auf Linux, Xiaomi, Samsung, Pixel, etc nutzen aber abgewandelte versionen)
- SAP ERP, S/4HANA
- Adobe Creative Cloud

#### keine SPLs

- Instagram
- Steam
- Wikipedia

## Aufgabe 4 Vorteile von SPLs

- Maßgeschneiderte Produkte
  - gezielte Anpassung an Kunden oder Marksegmente
- Kostenreduktion
  - sparen von Entwicklungs und Wartungskosten durch gleiche Code-basis
- Qualitätssteigerung
  - widerverwendung getesteter und bewährter komponenten
  - einfachere Wartung über mehrere Produkte der Kernmodule
- schnellere Markteinführung
  - scnellere entwicklung neuer produktvarianten
- Nachhaltige Wartbarkeit und Skalierbarkeit
  - langfristige Evolution und Wachstum
  - änderung in kernkomponenten wirken sich auf alle Varianten aus

```plaintext
Effort
│____
│    |
│    |
│    |    ← Produktlinienentwicklung
│    \__________________________
│
│_______________________________→ Anzahl Produkte
      ↑
      Einzelsystem-Entwicklung
```

**Beispiel**: HP Druckertreiber

- Anfangsinvestition: Aufbau einer gemeinsamen Treiberplattform für alle Druckermodelle.
- Ergebnis: Neue Druckermodelle können durch Konfiguration der vorhandenen Features (Papierformate, Farbdruck, Netzwerkfunktionen) schnell und günstig integriert werden.
- Langfristiger Effekt:
  - geringere Entwicklungs- und Testkosten,
  - konsistente Benutzererfahrung über alle Geräte hinweg,
  - schnellere Produktupdates.

## Aufgabe 5 Herausforderungen von SPLs

### a) Kopierter Quellcode für neue Produktvariante

- **Herausforderung:** Software Clones  
- **Problem:** Code wird kopiert („Clone-and-Own“), was zu Inkonsistenzen und erhöhtem Wartungsaufwand führt.

### b) Schwierige Nachvollziehbarkeit von Features

- **Herausforderung:** Feature Traceability  
- **Problem:** Unklar, wo Features im Code umgesetzt sind → erschwert Wartung, Fehlersuche und Erweiterung.

### c) Probleme bei automatisierter Produktgenerierung

- **Herausforderung:** Automated Generation  
- **Problem:** Schwierigkeiten bei der automatischen Zusammensetzung von Features → fehlerhafte Builds und Varianten.

### d) Viele mögliche Produktvarianten

- **Herausforderung:** Combinatorial Explosion  
- **Problem:** Exponentielles Wachstum an Feature-Kombinationen → unmöglich, alle Varianten zu testen oder zu verwalten.

### e) Konflikte zwischen Features

- **Herausforderung:** Feature Interactions  
- **Problem:** Kombination bestimmter Features führt zu unvorhersehbarem Verhalten oder Funktionskonflikten.

### f) Langfristig wachsende Produktlinie

- **Herausforderung:** Continuing Change and Growth  
- **Problem:** Stetig steigende Komplexität durch neue Features → erschwerte Wartung und Qualitätsrückgang über Zeit.
