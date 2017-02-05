# Data Wrangling Task Descriptions

1. `twitter_cleaning.ipynb`: This notebook uses the parquest files downloaded by the scripts in the folder `scripts` 
that were used to download data for twitter (55.6GB). This notebook combines and cleans the parquet files based on some observations. The 
main purpose of cleaning is to make it ready for visualisation. In particular:
  * Combine all the downloaded parquet files into a single dataframe
  * Keep only the main languages (en, de and fr)
  * Remove tweets which do not have a sentiment
  * Map the location for each tweet to a canton and remove garbage locations and cantons (38% to 98% mapped)
  * Add month and time of day
  * GroupyBy columns that we want to add as filters in our visualisation and calculate average sentiment.
  * Finally return a CSV which can easily be read as a R dataframe for ease of visualisation.
  
2. `twitter_analysis.ipynb`: We do not look at the tweet itself while cleaning the twitter dataframe in 
  `twitter_cleaning.ipynb`. In this, we do the following:
   * Use the ungrouped cleaned dataframe to get a function which given a column of the data frame and a list 
   of strings as an input, returns the average sentiment for each tweet which has any of the words from the list 
   and grouped by column.
   * For example if we give `['india', 'inde']` and `month` as input, we get a dataframe which tells us the average sentiment 
   by month for each tweet which has either of the words 'india' or 'inde'.
   

