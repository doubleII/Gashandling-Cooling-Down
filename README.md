# Gashandling Abkühlen
Ablaufsteuerung zum Abkühlen und Aufwärmen eines Verdampfungskryostaten mit Heliumrückgewinnung.

#### Startparameter:
<br/>Abkühlen muss geändert werden 
<li>cooldown</li>
<br/>
Aufwärmen muss geändert werden 
<li>warmup</li>

## Settings
Sieh die Konfigurationsdatei "config.yaml"

<br/>TODO:
## FSM Abkühlen 
Vorkühlen & Abkühlen

## Zustände

### 1. Idle (beriet)
### 2. Initialize 
### 3. Vorkühlern (pre_cooling_down)
<br/>Voraussetzung:
<br/>Der Druck muss größer 220 mbar anzeigen. Das heißt, dass im Tank muss mindestens 220 miliiter Gas  
Die Temperature muss kleiner 4 Kelvin sein. Wenn die beiden Vorasusetzungen erfüllt sind,
ändert die FSM den Zustand. Unter diese Bedingungen soll das benötigte Heilum in den Kreislauf
eingefügt werden.
### 4. Helium einfühlen (fill_with_helium)
<br/>Helium einfüllen lassen
<br/>Die Ventile 2,3,4,5,6,13,14 werden geöfnet und die Vorpumpe und die turbopumpe eingeschaltet.
Dies  wird  solange  durchgeführt,  bis  genügend  Gas  im System steckt. Die Menge wird dabei an der Veränderung des Tankdrucks festgemacht. 200 mbar soll die 
Differenz betragen. Dieser  Vorgang  wird  unterbrochen,  falls  der  Druck  zwischen  Vorpumpe  und  Kompressor 
(pOut) einen Wert von 1000 mbar übersteigt. Hier soll einem Reißen der Kompressormembran 
durch  einen  zu  hohen  Druck  vorgebeugt  werden.  Um  dies  zu  realisieren  wird  Ventil  13 
geschlossen. Da somit kein Gas nachströmt, der Kompressor aber weiterpumpt, sinkt der Druck 
wieder. Sobald pOut wieder unter 300 mbar abfällt, kann mit dem Füllen durch Öffnen des 
Ventils 13 fortgefahren werden.
### 5. Kühlen (cooling)
### 6. Kühlen unter 1 Kelin 
### 7. Idle


<br/>[Dropbox link]: https://www.dropbox.com/sh/on9qoytrhnbr8m5/AAAsT7IvGPmPMGjfxRkduPOza?dl=0


