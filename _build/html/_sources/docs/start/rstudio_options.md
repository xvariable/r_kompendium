# RStudio anpassen

Über das Menü **Tools > Global Options** können Sie RStudio Ihren Vorlieben entsprechend anpassen. 

<img src="../../_static/img/screenshot_rstudio_options.png" alt="Screenshot RStudio Optionen"  style="width:400px;margin-right:550px;margin-bottom:25px;margin-top:25px">

An dieser Stelle kann ich nicht auf alle Möglichkeiten eingehen (ich kenne auch gar nicht alle), aber ich möchte auf ein paar sinnvolle Anpassungen hinweisen:

1. <img src="../../_static/img/screenshot_rstudio_options_workspace.png" alt="Screenshot RStudio Optionen für den Workspace"  style="float:right;margin-top:15;margin-left:15px;margin-bottom:5px">Im Bereich **General** unter **Workspace**: Entfernen Sie bitte das Häckchen bei *Restore .RData into workspace at startup* und stellen Sie die Option *Save workspace to .RData on exit* auf *Never*. Diese Optionen sorgen dafür, dass die Arbeitsumgebung von R bei jedem Schließen gespeichert wird und beim neuen Öffnen wieder geladen wird. Das betrifft zum Beispiel alle Objekte, die Sie in einer R-Session erstellt haben. Er hört sich zwar erstmal nach einer tollen und zeitsparenden Idee an, die ganzen Objekte nicht erneut erstellen zu müssen und direkt an der Stelle weitermachen zu können, an der man aufgehört hat. In der Praxis ist das aber eine ganz furchtbare Idee! Zwischen zwei R-Sessions hat man sehr wahrscheinlich vergessen, wo genau man aufgehört hat, welche Transformationen mit einem R-Objekt bereits durchgeführt wurden und welche noch folgen sollen. Das kann in totalem Chaos enden. Es ist daher besser mit einem frischen, leeren Workspace zu starten und ggf. das Skript -. welches man natürlich abspeichern sollte -- von oben nach unten erneut auszuführen. <br /><br />

2. Unter **Appearance** können Sie das Farbschema für das Syntaxhighlighting anpassen. Sie können zwischen sehr vielen unterschiedlichen Varianten wählen. Einige davon haben einen dunklen Hintergrund. So ein *Dark Mode* hilft beim Energiesparen und ist vielleicht auch angenehmer für die Augen. Probieren Sie es ruhig aus!
<img src="../../_static/img/screenshot_rstudio_options_appearance.png" alt="Screenshot RStudio Optionen Appearance" style="width:400px;margin-right:550px;margin-bottom:25px;margin-top:25px">

3. Ich habe über **Code > Display > General > Show margin** noch eine senkrechte Linie bei 80-Zeichen eingeblendet. Sie erinnert mich daran, nicht zu lange Codezeilen zu produzieren und lieber den Code an sinnvollen stellen zu umbrechen oder ihn ggf. umzuschreiben. Das dient der Übersichtlichkeit.