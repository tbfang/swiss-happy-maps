# server.R

# overall, never changes
# load libraries, read data sets

source("choropleth.R")
library(sp)
library(rgdal)
library(leaflet)
library(plyr)

# READING OUT DATA
cantons_kml <- read.csv("data/cantons_kml.csv", encoding="latin1", sep=",", dec=".")
cantons_kml$X <- NULL
twitter_full <- read.csv("data/twitter.csv", encoding="latin1", sep=",", dec=".")
canton_mapping <- read.csv("data/canton_code.csv", encoding="latin1", sep=",", dec=".")

# FILTERING FUNCTIONS
filter_df <- function(df, gender, min_month, max_month, language, time_period){
  gender <- switch(gender, "Both" = TRUE, "Female" = (df$gender == gender), "Male" = (df$gender == gender))
  language <- switch(language, "All" = TRUE, "English" = (df$language == language), "German" = (df$language == language), "French" = (df$language == language))
  time_period <- switch(time_period, "All" = TRUE, "Day" = (df$time_period == time_period), "Night" = (df$time_period == time_period))
  month <- ((min_month <= df$month) & (df$month <= max_month))
  
  filtered = df[(gender & language & time_period & month),]
  return(filtered)
}

group_df <- function(df) {
  df <- ddply(df,.(canton_code),summarise,
      sentiment = weighted.mean(sentiment, count, ,na.rm=TRUE))
  df <- merge(x = canton_mapping, y = df, by = "canton_code", all.x = TRUE) # adding canton_original
  # aggregate(sentiment ~ canton_code, df, mean)
  df <- join(cantons_kml, df, type = "left")
  # merge(x = cantons_kml, y = df, by = "canton_code", all.x = TRUE)
  df[is.na(df)] = 0
  return(df)
}

new_df <- function(df, gender = TRUE, min_month=1, max_month=10,language=TRUE,time_period=TRUE) {
  return(group_df(filter_df(df,gender,min_month,max_month,language, time_period)))
}


shinyServer(
  function(input, output) {
  	twitter_filtered <- reactive(new_df(twitter_full, gender = input$gender, min_month = input$range[1], max_month = input$range[2], language = input$language, time_period = input$time_period))
  	# typeof(twitter_filtered$sentiment)
    output$map <- renderLeaflet({
    	build_map(df = twitter_filtered())
    })
    
  }
)