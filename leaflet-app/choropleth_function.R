# Defines the shiny function with the parameters...

# BUILD THE MAP

build_map <- function(df) {
  swiss_cantons <- readOGR("data/ch-cantons.topojson.kml","cantons",encoding="utf-8")

#Defining the colors that are going to use for the scale of happiness (from -1 to 1)
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
  #Defining the map with leaflet
  mymap <- leaflet() %>%
    addProviderTiles("Esri.WorldGrayCanvas",options = tileOptions(minZoom=0, maxZoom=16)) %>%
    #Defining the polygon, which is going to be the layer for the sentiments of the tweets, this polygon will have the option of highlight
    #which will help us to display the label (Name of the canton along with its sentiment) whenever you past the mouse courser over a certain canton
    addPolygons(data = swiss_cantons, 
                fillColor = ~palette(df$sentiment), #Defining the color of the canton depending of its sentiment and based on the scale color that we already defined
                fillOpacity = 1,
                color = "grey",
                dashArray=c(5,5),
                weight = 2,
                label=~stringr::str_c(df$canton,' : ', format(round(df$sentiment, 3), nsmall = 3)),
                highlightOptions = highlightOptions(dashArray=c(1,1),color='#808080', opacity = 1, weight = 3.0, fillOpacity = 1,bringToFront = TRUE, sendToBack = TRUE),
                group="allcantons")%>%
    #These are some options in order to be able to use the highlight option we defined in the polygon
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
    
#Adding a legend, which, practically will be just a text box with the following text: "Twitter Sentiment Analysis, Hover over a Canton"
addLegend(position = 'topright',
              colors = NULL,
              labels = NULL,
              title = "<h8>Twitter Sentiment Analysis</h8><h6>Hover over a Canton</h6>")%>%

#Adding a legend with the color scale to be displayed along with the map, this color scale matches exactly with the palette we defined.
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
  
}
