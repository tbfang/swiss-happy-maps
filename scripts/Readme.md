## Scripts used on the cluster

This directory contains the scripts we ran on the cluster to do some analysis of the data and download the relevant data as parquet files. 

1. `get_twitter_*.py` files are used to get `tweet_id`, `location`, `sentiment`, `language`, `main`, `date`, `canton`, `gender`, `num_following`, `num_followers`, `mentions` from the Twitter JSON files on the cluster, and download them as parquet files.

2. `get_insta_*.py` is similar, and gets the `post_id` and `sentiment` from the Instagram JSON files on the cluster, and download them as parquet files.

3. `get_fasttext_format.py` looks for all the instagram posts which have a sentiment so that we can generate both a training data set (instagram posts with labels) and a test data set (instagram posts without labels). This script also prepares those data sets to be in the specific format in order to be processed by FastText and could predict the labels for the test data set.

4. `run_count_sent.py` is used to get the count of posts with or without sentiment.