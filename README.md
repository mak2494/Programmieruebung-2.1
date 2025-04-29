# Programmieruebung-2.1
    Gruppe: Hannah Kleutgens, Marie Köhl 
## Aufgabe 1 
### Vorrausetzungen
    Python 3.10
    Pdm 
### Vorgehen bestehendes pdm installieren 
    1.	Das Git Repository in VS Code clonen 
    2.	Mit dem Befehl pdm install im Bash, das bestehende pdm installieren
### Vorgehen pdm anlegen 
    1.	Mit dem Befehl pdm init ein pdm erstellen 
    2.	Die enstprechenden Daten, wie Name des Projekts oder der Autor*innen eingeben 
    3.	Wichtige Pakete, wie numpy oder matplotlib, die für den Code benötigt werden mit pdm add <paketname> zum pdm hinzufügen 
### Funktionsweise des bestehenden Codes
    1.	In load_data.py werden die Daten aus activity.csv importiert und die Leistungswerte herausgefiltert
    2.	Mit sort.py werden die Leistungsdaten mit Hilfe eines Bubble-Sort-Algorithmus sortiert 
    3.	In load_data.py werden die Daten in absteigende Reihenfolge gebracht 
    4.	In power_curve werden die Leistungsdaten über die Zeit in Sekunden visualisiert/geplottet und als Image gespeichert
        Der erstellte Plot ist hier sichtbar:  
        [Leistung über Zeit](https://github.com/mak2494/Programmieruebung-2.1/raw/main/figures/Power_Curve.png)