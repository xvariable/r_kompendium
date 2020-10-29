#!/usr/bin/env python
# coding: utf-8

# # Features von RStudio
#   
# RStudio ist eine umfangreiche IDE, die die Anwender:innen mit umfangreichen Funktionen unterstützt. Ein paar davon möchte ich an dieser Stelle explizit hervorheben.

# ## Autovervollständigen
# Während man in RStudio Text schreibt, macht die IDE Vorschläge, wie sich das bisher geschriebene sinnvoll vervollständigen lässt. Dieses Feature ist besonders hilfreich, wenn man von einem Befehl nur den Anfang kennt und nicht genau weiß, wie er geschrieben wird und welche Elemente er beinhaltet.
#   
# <img src="../../_static/img/screenshot_autocomplete.png" alt="Screenshot Autovervollständigen" style="width:500px;margin-bottom:25px;margin-right:10px" align="left">
#     
# Der Screenshot zeigt, wie nach Tippen der Buchstaben `prin` Funktionen angezeigt werden, die mit diesen Buchstaben beginnen. Aus den Vorschlägen kann man mit der Maus oder über die Pfeiltasten und Drücken der Entertaste den richtigen auswählen, ohne dass man den Befehl selbst zu Ende schreiben müsste. Das spart viel Zeit und ist außerdem gerade dann hilfreich, wenn man die Befehle noch nicht auswendig kennt. Neben dem Autocomplete wird außerdem in gelb ein Hinweis zur Syntax und der Beginn der entsprechenden Hilfe-Datei angezeigt. Zu beachten ist, dass über das Autocomplete nur Funktionen aus Paketen angezeigt werden, welche während der aktuellen Session bereits geladen wurden.

# ## Aufrufen der Hilfe-Funktion
# Der Tab "Help", der weiter oben bereits vorgestellt wurde ist bei RStudio direkt in die Entwicklungsumgebung integriert. 
# Dieser Umstand ist erwähnenswert, denn bei anderen IDEs öffnet sich bei Aufruf der Hilfefunktion häufig ein externer Browser. 
# Das die Hilfe bei RStudio direkt integriert ist nimmt zwar etwas Platz auf dem Bildschirm weg, ist jedoch auch sehr anwenderfreundlich, gerade für Programmiereinsteiger:innen.

# ## Automatisches Einrückungen
# Wenn Codes länger werden und über mehrere Zeilen gehen bietet es sich an, diesen durch Einrückungen übersichtlich zu formatieren. Es kann so leicht kenntlich gemacht werden welche Teile einer längeren Kette von Befehlen unmittelbar zusammengehören.
# Bei einigen Programmiersprachen gehören solche Einrückungen sogar unmittelbar zur Syntax dazu (z.B. bei Python). Aber selbst wenn sie nicht unmittelbar Bestandteil einer Sprache sind (wie bei R), sind Einrückungen für die menschliche Anwender:in nützlich, um den Überblick zu behalten.
# RStudio schlägt während des Programmierens selbst sinnvolle Einrückungen vor, so dass die Anwender:in damit meist keine Arbeit hat.

# ## Syntaxhighlighting
# Syntaxhighlighting bedeutet, dass unterschiedliche Bestandteile des Codes in unterschiedlichen Farben dargestellt werden. Der folgende Screenshot demonstriert dies:
#     
# <img src="../../_static/img/screenshot_syntax_highlighting.png" alt="Screenshot Autovervollständigen" style="margin-bottom:25px;margin-right:10px" align="left">
# Auch Syntaxhighlighting dient der Übersichtlichkeit für die menschlichen Anwenderin. 
