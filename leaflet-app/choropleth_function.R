# defines the shiny function with the parameters...
# adding male and female options...

# BUILD THE MAP

build_map <- function(df) {
  swiss_cantons <- readOGR("data/ch-cantons.topojson.kml","cantons",encoding="utf-8")
  # df = switch(gender, "female" = sentiment_female, "male" = sentiment_male)
  
palette <- colorBin(c('#a50026', 
                      '#d73027',
                      '#f46d43',
                      '#fdae61',
                      '#fee08b',
                      '#ffffbf',
                      '#d9ef8b',
                      '#a6d96a',
                      '#66bd63',
                      '#1a9850',
                      '#006837'), 
                     bins = c(-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4,0.6,0.8,1))
  
  # popup1 <- paste0("<span style='color: #7f0000'><strong>Canton: </strong></span>", df$canton_code,
  #                  "<br><span style='color: salmon;'><strong>Happiness: </strong></span>", 
  #                  df$sentiment)
  mymap <- leaflet() %>%
    addProviderTiles("Esri.WorldGrayCanvas",options = tileOptions(minZoom=0, maxZoom=16)) %>%
    addPolygons(data = swiss_cantons, 
                fillColor = ~palette(df$sentiment), 
                fillOpacity = 1,
                color = "grey",
                dashArray=c(5,5),
                weight = 2,
                #popup = popup1,
                label=~stringr::str_c(df$canton,' : ', format(round(df$sentiment, 3), nsmall = 3)),
                highlightOptions = highlightOptions(dashArray=c(1,1),color='#808080', opacity = 1, weight = 3.0, fillOpacity = 1,bringToFront = TRUE, sendToBack = TRUE),
                group="allcantons")%>%
    htmlwidgets::onRender("
      var myMap = this;
      var layers = myMap._layers;
      for(var i in layers) {
        var layer = layers[i];
        if(layer.label) {
          layer.on('mouseover',
            function(e) {
              this.setStyle(highlightStyle);
              this.bringToFront();
            });
          layer.on('mouseout',
            function(e) {
              this.setStyle(defaultStyle);
              this.bringToBack();
            });
        }
      }
    }") %>%
    
addLegend(position = 'topright',
              colors = NULL,
              labels = NULL,
              title = "<h8>Twitter Sentiment Analysis</h8><h6>Hover over a Canton</h6>")%>%

    addLegend(position = 'bottomright',
              colors = c('#a50026', 
                      '#d73027',
                      '#f46d43',
                      '#fdae61',
                      '#fee08b',
                      '#ffffbf',
                      '#d9ef8b',
                      '#a6d96a',
                      '#66bd63',
                      '#1a9850',
                      '#006837'), 
              labels = c(-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4,0.6,0.8,1), 
              opacity = 1, 
              title = "<black>Sentiment</black>")
  
  # print(mymap)  
}

# filtered_df <- new_df(df,gender="Female")


# build_map(filtered_df)
