import json
import subprocess
import fnmatch
from pyspark import SparkConf, SparkContext
import pyspark.sql
from pyspark.sql.types import *	
from pyspark.sql import SQLContext
from pyspark.sql.functions import lit
import pandas as pd

conf = SparkConf().setAppName("ADA-gcl")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


# Path definitions
#If you try to run it for the whole dataset, it gives an out of memory error
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

all_paths = get_paths(base_path, True)

#months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october']
#for m in months:
file_list = []
for path in all_paths:
    if(fnmatch.fnmatch(path, insta_files)):
        file_list.append(path)


for f in file_list:
    df_temp = sqlContext.read.json(f).collect()
    writeCols(df_temp)


