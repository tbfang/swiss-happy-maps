# Swiss Happy Maps

Happiness of Swiss cantons based on social media sentiment.

## Summary of Work

We classified 6.5 million instagram post sentiments using fastText. Our [**notebook**](https://github.com/tbfang/swiss-happy-maps/blob/master/machine_learning/FastText_sentiment_classifier.ipynb) is complete with data preparation, feature analysis, word clouds, hyperparameter selection, learning curves, cross-validation, confusion matrix to explain the model and measure its performance.

We provide an interactive visualization of the happiness of Switzerland across gender, time of day, and time of year with the [**interactive web application**](https://github.com/tbfang/swiss-happy-maps/tree/master/interactive_visualization).

Our data was on the Hadoop cluster provided by [Prof. Catasta](https://people.epfl.ch/michele.catasta). Our data acquisition and processing was done with PySpark, and our PySpark applications are found in our [`scripts` repo](https://github.com/tbfang/swiss-happy-maps/tree/master/scripts). Extensive data wrangling done for the visualization can be found in our [`data_wrangling` repo](https://github.com/tbfang/swiss-happy-maps/tree/master/data_wrangling).

## Challenges Faced
1. None of our team members had any knowledge of distributing computing or experience running jobs on the Hadoop cluster. It took us time and effort before successfully submitting a simple Spark application on the cluster.

2. None of our team members had experience with building interactive visualization or web applciation. We learned to use the Leaflet package in R and learned to build out our first web application using Shiny in RStudio. 

## Tools 

* [Spark](http://spark.apache.org/) for distributed data processing
* [fastText](https://github.com/facebookresearch/fastText) for state-of-the-art word representation learning and text classification
* [Leaflet](https://github.com/rstudio/leaflet) for interactive choropleth
* [Shiny](http://shiny.rstudio.com/) for interactive web app

-------------------------------------------------------------------------------------------------------

## Repository Structure

* [**`scripts`**](https://github.com/tbfang/swiss-happy-maps/tree/master/scripts): Contains the scripts we ran on the cluster, usually to save the data as parquet so that we can do further analysis on it locally.
* [**`data_wrangling`**](https://github.com/tbfang/swiss-happy-maps/tree/master/data_wrangling): Contains the notebooks used to clean the twitter data downloaded through the scripts. It is finally made into a form more suitable for visualization.
* [**`machine_learning`**](https://github.com/tbfang/swiss-happy-maps/tree/master/machine_learning): Gives the code and details for the Machine Learning part. The notebook is complete with feature analysis, word clouds, learning curves, cross-validation, confusion matrix to explain the model and measure its performance.
* [**`interactive_visualization`**](https://github.com/tbfang/swiss-happy-maps/tree/master/interactive_visualization): Gives the data and corresponding code in R for creating the Leaflet map and code for creating the shiny application in R that generates the interactive web application.

Further details for each folder are given in the Readme of each folder.

## Acknowledgement

This repository was developed by [Kirtan Padh](https://github.com/kirtanp/), [Luis Medina](https://github.com/lemmmr), and [Tina Fang](https://github.com/tbfang/) from November 2016 to February 2017 for the course [Applied Data Analysis](http://ada.epfl.ch/) at EPFL, Switzerland.