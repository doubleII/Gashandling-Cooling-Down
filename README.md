# Gashandling
Ablaufsteuerung zum Abkühlen und Aufwärmen eines Verdampfungskryostaten mit Heliumrückgewinnung.

#### Startparameter:
<br/>Abkühlen
<li>cooldown</li>
<br/>
Aufwärmen 
<li>warmup</li>

# Settings
Sieh die Konfigurationsdatei "config.yaml"

<br/>TODO:
# FSM Abkühlen 
Vorkühlen & Abkühlen 

<br/>Vorkühlen
<br/>Voraussetzungen
<br/>Der Druck muss größer 220 mbar anzeigen.  
Die Temperature muss größer 4 K sein. Wenn die beiden Vorasusetzungen erfüllt sind,
ändert die FSM den Zustand. Unter diese Bedingungen soll das benötigte Heilum in den Kreislauf
eingefügt werden.

<br/>Helium einfüllen lassen
<br/>Die Ventile 2,3,4,5,6,13,14 werden geöfnet und die Vorpumpe und die turbopumpe eingeschaltet.
Dies  wird  solange  durchgeführt,  bis  genügend  Gas  im System steckt. Die Menge wird dabei an der Veränderung des Tankdrucks festgemacht. 200 mbar soll die 
Differenz betragen. Dieser  Vorgang  wird  unterbrochen,  falls  der  Druck  zwischen  Vorpumpe  und  Kompressor 
(pOut) einen Wert von 1000 mbar übersteigt. Hier soll einem Reißen der Kompressormembran 
durch  einen  zu  hohen  Druck  vorgebeugt  werden.  Um  dies  zu  realisieren  wird  Ventil  13 
geschlossen. Da somit kein Gas nachströmt, der Kompressor aber weiterpumpt, sinkt der Druck 
wieder. Sobald pOut wieder unter 300 mbar abfällt, kann mit dem Füllen durch Öffnen des 
Ventils 13 fortgefahren werden.
<br/>...
<br/>Abkühlen
<br/>...
# FSM Temperature konstant halten 

# FSM Aufwärmen
