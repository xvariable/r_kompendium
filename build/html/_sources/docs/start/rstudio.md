# RStudio: IDE für R

R ist eine Programmiersprache und sie kommt auch mit einer kleinen Umgebung, in der man R direkt ausführen kann. Allerdings ist die Konsole sehr schlicht gehalten und das Arbeiten damit macht nicht wirklich Spaß. Stattdessen benutzen die meisten Entwickler einen Editor oder eine so genannte *IDE* (= Integrated Development Environment zu deutsch Entwicklungsumgebung), die eine grafische Oberfläche bietet und das Programmieren und das Datenmanagement erheblich erleichtert.

Die bekannteste und beliebteste IDE für R ist RStudio.
Wie der Name schon vermuten lässt wurde RStudio speziell für die Arbeit mit R entwickelt. Es ist genau auf die Bedürfnisse von R-Anwender:innen angepasst. Im folgenden Abschnitt stelle ich die Entwicklungsumgebung kurz vor, beschreibe einige Features und die Benutzeroberfläche.

<img src="https://upload.wikimedia.org/wikipedia/commons/d/d0/RStudio_logo_flat.svg" alt="Logo RStudio" width="150px" align="left" style="border-right:15px solid white"> 
Die IDE RStudio ist seit 2011 auf dem Markt und wird von RStudio PBC entwickelt und vertrieben. 
Das Programm ist sowohl für Desktop-Rechner als auch für Server verfügbar und wird sowohl kostenlos als auch in einer kommerziellen Pro-Version vertrieben. 
Die Pro-Versionen unterscheiden sich vor allem dadurch, dass den Anwendern ein Priority-Support geboten wird.
Seit Beginn 2020 firmiert RStudio als *Public Benefit Corporation* und hat sich damit dem Gemeinwohl verpflichtet.

Das Unternehmen RStudio ist Teil des *R Consotium*, eines Zusammenschlusses von Unternehmen, die R in großem Stil einsetzen oder für ihre Geschäftsmodelle nutzen (auch Microosoft, Google und Oracle gehören dazu). 
Gerade RStudio treibt sowohl die Verbreitung der Sprache R als auch ihre Weiterentwicklung und Standardisierung enorm voran und prägt damit ihre Ausgestaltung zusehens. 

<img src="https://www.tidyverse.org/images/tidyverse-default.png" alt="Logo tidyverse" width="200px" align="left" style="margin-right:15px;margin-top:5px"> Allen voran ist hier das *Tidyverse* zu nennen. Es handelt sich dabei um eine Gruppe von Paketen die von den RStudio-Programmierern um *Hadley Wickham* (Chief Scientist bei RStudio) entwickelt wurden und die dazu dienen R einheitlicher und verständlicher zu gestalten sowie die Sprache noch besser auf die Bedürfnisse moderner Datenanalyse anzupassen. Auch in diesem Buch wird weitestgehend auf die Pakete und Funktionen des Tidyverse zurückgegriffen.
Obwohl die Entwicklung der Vereinheitlichung von R mit dem Tidyverse viele Anhänger gefunden hat und enorm zur Popularität der Sprache beigetragen haben dürfte, sei dennoch erwähnt, dass es auch Stimmen gibt, die diese Entwicklung kritisch betrachten. {cite}`Matloff_2019` {cite}`McChesney_2020`


## RStudio-Cloud
Wie oben erwähnt, gibt es sowohl eine Server- als auch eine Desktopversion von RStudio. 
Für den Zweck der Statistik-Ausbildung arbeiten wir hier am IJK mit einer Serverversion, nämlich der RStudio-Cloud.
Dies hat die Vorteile, dass die Studierenden zunächst nichts auf ihren Rechnern installieren müssen und dass die Entwicklungsumgebung mit allen Übungsskripten bereits vorliegt. 
Sie können sich sehr leicht selbst eine eigene Version der Verwendeten Skripte erstellen und so an den Übungen teilnehmen.
Der/die Dozierende kann sich Ihre Versionen ansehen und so bei Fehlern und Fragen leicht helfen.


## Installation von RStudio
Obwohl die RStudio-Cloud im Rahmen der Statistikausbildung sehr praktisch sein wird, benötigen Sie (später) eine eigene Instanz von R und RStudio auf Ihrem persönlichen Rechner. Zum einen für den Zweck des Übens, zum Anderen weil Sie es später zur Arbeit an eigenen (Studien-)Projekten benötigen werden.
Die Anleitung zur Installation befindet weiter hinten in diesem Kapitel. 
Sie ist getrennt nach Windows und MacOS aufgeführt, da sich die Schritte die zur Installation nötig sind leicht unterscheiden.


## Weiterführende Links
- [RStudio](https://rstudio.com/)
- [RStudio Cloud](https://rstudio.cloud/)
- [R Consotium](https://www.r-consortium.org/)

## Literatur
```{bibliography} ../../_bibliography/references.bib
:filter: docname in docnames
:style: plain
```
