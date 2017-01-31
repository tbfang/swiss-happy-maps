# ui.R

library(leaflet)
library(shiny)

shinyUI(fluidPage(
  titlePanel("Happiness of Switzerland"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Explore sentiment patterns in Switzerland, according to demographics"),
    
      selectInput("gender", # gender
        label = "Gender",
        choices = c("Female", "Male", "Both"),
        selected = "Both"),

      selectInput("language", # language
        label = "Language",
        choices = c("English", "German", "French", "All"),
        selected = "All"),

      selectInput("time_period", # language
        label = "Time of Day",
        choices = c("Day", "Night", "All"),
        selected = "All"),
    
      sliderInput("range", 
        label = "Months (from 2016)",
        min = 1, max = 10, value = c(1,10)),

      br(),
      br(),
      "Data source: Twitter", 
      img(src = "twitter.png", height = 48, width = 80)
      
    ),
  
    mainPanel(leafletOutput("map"))
  )
))