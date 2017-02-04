## Data description of cleaned data
We earlier had a lot of uncleaned data in parquet format which we removed from the repository. We have kept only the cleaned 
data and given descriptions only for that.

1. `final_twitter.parquet`: has the average sentiment grouped by `'canton', 'month', 'language', 'gender', 'time_of_day'` after 
cleaning the full dataframe. This is for ease of filtering by these columns for visualisation.

2. `twitter_forFreq.parquet`: has a row for each tweet with `'canton', 'month', 'language', 'gender', 'time_of_day'` as well as
the tokenized and stop-words removed tweet as a list. This is for ease of doing frequence analysis and filtering by keywords.

3. `small_dict.p`: Is a dictionary mapping the source_locations to cantons for the tweets for which we do not have a canton.

4. `location.p`: Is a dictionary which maps location o canton from using all the tweets which have both columns. This is 
appropriately filtered to make the `small_dict`.
