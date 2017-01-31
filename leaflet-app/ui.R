# ui.R

library(leaflet)
library(shiny)

shinyUI(fluidPage(
  titlePanel("Happiness of Switzerland"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Explore sentiment patterns in Switzerland across dimensions."),
    
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

      "Built at",
      img(src = "Logo_EPFL.png", height = 30, width = 60), "with",
      br(),
      br(),
      img(src = "leaflet.png", height = 30, width = 100), "        ",
      img(src = "shiny.png", height = 25, width = 50), "           ",
      img(src = "spark.png", height = 25, width = 50),
      br(),
      br(),
      "by Luis Medina, Kirtan Padh, Tina Fang"
      
    ),
  
    mainPanel(leafletOutput("map", height="557px"))
  )
))