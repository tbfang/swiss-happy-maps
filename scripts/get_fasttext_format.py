import json
import subprocess
import fnmatch
from pyspark import SparkConf, SparkContext
import pyspark.sql
from pyspark.sql.types import *	
from pyspark.sql import SQLContext
from pyspark.sql.functions import lit
import pandas as pd

#This function looks for all the instagram posts which have a sentiment so that we can generate both a training data set
#(instagram posts with labels) and a test data set (instagram posts without labels), this function also prepares those data 
#sets to be in the specific format in order to be processed by FastText and could predict the labels for the test data set.

conf = SparkConf().setAppName("ADA-gcl")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


# Path definitions
base_path = 'hdfs://iccluster046.iccluster.epfl.ch:8020/datasets/goodcitylife/'
insta_files = '*/harvest3r_instagram_data*.json'
news_files = '*/harvest3r_news_data*.json'
twitter_files = '*/harvest3r_twitter_data*.json'
train_path = 'train.txt'
test_path = 'test.txt'
lbl = '__label__'

def hasColumn(df, column):
    try:
        df[column]
        return 1
    except:
        return 0

def label(sen):
    if(sen == 'NEUTRAL'): 
         return('0')
    elif(sen == 'POSITIVE'):
        return('1') 
    elif(sen == 'NEGATIVE'):
        return('-1')
    else:
        return('jhol')  	
    
# Restrict columns and change their names
def writeCols(df):
    with open(train_path, "a") as train_file, open(test_path, "a") as test_file:
        for row in df:
            try:
                row._source.sentiment       
                if(row._source.sentiment in ['POSITIVE', 'NEGATIVE', 'NEUTRAL']):
                    train_file.write(lbl+label(row._source.sentiment) + ' ' + ' '.join(row._source.tags) + '\n') 
                else:
                    test_file.write(row._id + "," + ' '.join(row._source.tags)  + '\n')
            except:
                test_file.write(row._id + "," + ' '.join(row._source.tags)  + '\n')

def get_paths(dir_path, recurse):
    t = []
    files = []
    if(recurse == True):
        cat = subprocess.Popen(["hadoop", "fs", "-ls", "-R", dir_path], stdout=subprocess.PIPE)
    else:
        cat = subprocess.Popen(["hadoop", "fs", "-ls", dir_path], stdout=subprocess.PIPE)
    for line in cat.stdout:
        t.append(line.decode())

    for l in t[1:]:
        files.append(l.split(' ')[-1].rstrip())
    return(files)

#First we are going to get all the paths of the json files in the cluster (news, twitter and instagram information)
all_paths = get_paths(base_path, True)

#Secondly, we are going to get just all the instagram files.
file_list = []
for path in all_paths:
    if(fnmatch.fnmatch(path, insta_files)):
        file_list.append(path)

#Finally, we are going to get the sentiment for the instagram post in order to generate both the train data set and the test data set
#this by reading each of the json files for instagram.
for f in file_list:
    df_temp = sqlContext.read.json(f).collect()
    writeCols(df_temp)


