# Evolution of happiness over time for different places in Switzerland

## Abstract
We try do an analysis of how happy each part of Switzerland is during different times of the year and across times of the day as well as gender. We describe our approach below.

## Data description and methodology
* **Twitter** - We will use the twitter dataset from 2012 provided by Prof. Catasta. We are already given a sentiment for most of the tweets along with city level location. We have canton for some of the data. We get the canton information for all the data and visualize it using RStudio to see the average twitter sentiment across different cantons and with the option to filter by Gender, Time of day and tweet language.
* **Instagram** -  We will use the instagram data provided by Prof. Catasta in a similar way as the twitter data. But we first do a sentiment analysis on the Instagram dataset since we are not given the sentiments. We do a sentiment analysis on the hashtags for this purpose using FastText. Details are given in the readme in the machine_learning folder.

We provide the instagram sentiment we get to the other teams to be able to use them.

## Challenges faced
* Having no familiarity with using a cluster before, it took us some time and effort before we had our first simple script running on the cluster. We became quite comfortable with writing scripts in pyspark by the end of the project.
* **TODO** Challenges faced in machine learning
* **TODO** Challenges faced in Visualization.

## Deliverables
### Machine Learning
* A result of the sentiment analysis of instagram posts using text analysis of the hashtags along with a measure of how good our model is in doing sentiment analysis.

### Visualization
* Using the results of the sentiment analysis to make a map of Switzerland which shows how happy each part is. The dynamic map can be filtered by Month, Gender, Language and time of day to see the average sentiment for each Canton.

-------------------------------------------------------------------------------------------------------

## Repository Structure

* `Scripts`: Contains the scripts we ran on the cluster, usually to save the data as parquet so that we can do further analysis on it locally.
* `data_wrangling`: Contains the notebooks used to clean the twitter data downloaded through the scripts. It is finally made into a form more suitable for visualisation.
* `Machine_Learning`: Gives the code and details for the Machine Learning part. The notebook is complete with learning curves, cross-validation, etc to get an idea of the how the model is as well as explanations on the details of the model.
* `leaflet-app`: **TODO** Details to be added as seen fit.

Further details for each folder are given in the Readme of each folder.

