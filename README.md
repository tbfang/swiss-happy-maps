# Evolution of happiness over time for different places in Switzerland

## Abstract
We try do an analysis of how happy each part of Switzerland is during different times of the year and across times of the day as well as gender. We describe our approach below.

## Data description and methodology
* **Twitter** - We will use the twitter dataset (goodcitylife) provided by Prof. Catasta. We are already given a sentiment for most of the tweets along with city level location. We have canton for some of the data. We get the canton information for all the data and visualize it using RStudio to see the average twitter sentiment across different cantons and with the option to filter by Gender, Time of day and tweet language.
* **Instagram** -  We will use the instagram data (goodcitylife) provided by Prof. Catasta in a similar way as the twitter data. But we first do a sentiment analysis on the Instagram dataset since we are not given the sentiments. We do a sentiment analysis on the hashtags for this purpose using FastText. Details are given in the readme in the machine_learning folder.

We provide the instagram sentiment we get to the other teams to be able to use them.

## Challenges faced
* Having no familiarity with using a cluster before, it took us some time and effort before we had our first simple script running on the cluster. We became quite comfortable with writing scripts in pyspark by the end of the project.
* In the Machine Learning part, trying to create an image classificator with the 1 million and a half pictures from the instagram data was very difficult because two main reasons: the labels (sentiments) we already had, made no sense with the pictures, and also, the amount of time that would take to download around 8 million and a half pictures  and to train a model and to predict all the labels that are missing. That's why we chose to perform text classification based on the instagram tags.
* Since we wanted to create an interactive map that could filter over several options (we found "folium" kind of limited thinking of the things we wanted to visualize), we chose to use the "shiny" library for R, this was very difficult at the beginning because none of the teammembers had previous knowledge of R. As we did in the cluster, we became more comfortable with the R and R Studio as we were working on the project.

## Deliverables
### Machine Learning
* A result of the sentiment analysis of instagram posts using text analysis of the hashtags along with a measure of how good our model is in doing sentiment analysis.

### Visualization
* Using the results of the sentiment analysis to make a map of Switzerland which shows how happy each part is. The dynamic map can be filtered by Month, Gender, Language and time of day to see the average sentiment for each Canton.

-------------------------------------------------------------------------------------------------------

## Repository Structure

* `Scripts`: Contains the scripts we ran on the cluster, usually to save the data as parquet so that we can do further analysis on it locally.
* `data_wrangling`: Contains the notebooks used to clean the twitter data downloaded through the scripts. It is finally made into a form more suitable for visualization.
* `Machine_Learning`: Gives the code and details for the Machine Learning part. The notebook is complete with learning curves, cross-validation, etc to get an idea of the how the model is as well as explanations on the details of the model.
* `leaflet-app`: Gives the data and corresponding code in R for creating the maps, as well as the code for the server and user for creating the shiny application in R that generates the interactive map.

Further details for each folder are given in the Readme of each folder.

