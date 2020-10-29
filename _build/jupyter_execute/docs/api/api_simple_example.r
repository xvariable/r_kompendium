# OPTIONAL! Benötigte Pakete vorab installieren
#install.packages("tidyverse")
#install.packages("janitor")

#Pakete laden
library(tidyverse)
library(httr)
library(jsonlite)
library(janitor)

# GET-Request mit httr
my_response <- GET("http://api.tvmaze.com/search/shows?q=sesame%20street")
print(my_response)

# Den Inhalt der Response ausgeben
my_content <- content(my_response, as = "text")
my_content

# Mit jsonlite in einen Tibble umwandeln
df <- fromJSON(my_content, flatten = TRUE) %>%
  as_tibble(.name_repair = janitor::make_clean_names) 

# Datensatz anzeigen
head(df)

# GET-Request mit httr
love_response <- GET(url = "http://api.tvmaze.com/",
                    path = "search/shows",
                    query = list(
                      q = "Love"
                    ))

# Mit jsonlite in einen Tibble umwandeln
df_love <- content(love_response, as = "text") %>%
      fromJSON(flatten = TRUE) %>%
      as_tibble(.name_repair = janitor::make_clean_names) 

# Ergebnisdatensatz anzeigen
head(df_love, 10)

# Ihr Code hier!
# GET-Request mit httr
response_sesame <- GET(url = "http://api.tvmaze.com/",
                    path = "shows/6544/episodes",
                    query = list(
                      all = 1
                    ))

# Mit jsonlite in einen Tibble umwandeln
df_sesame <- content(response_sesame, as = "text") %>%
      fromJSON(flatten = TRUE) %>%
      as_tibble(.name_repair = janitor::make_clean_names) 

# Anzahl der Fälle ausgeben
print(str_c("Der Datensatz hat ", nrow(df_sesame), " Einträge."))

# Ergebnisdatensatz anzeigen
head(df_sesame, 10)
