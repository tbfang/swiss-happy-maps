import json
import subprocess
import fnmatch
from pyspark import SparkConf, SparkContext
import pyspark.sql
from pyspark.sql.types import *	
from pyspark.sql import SQLContext
from pyspark.sql.functions import lit

conf = SparkConf().setAppName("ADA-gcl")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
# Path definitions

#If you try to run it for the whole dataset, it gives a out of memory error
base_path = 'hdfs://iccluster046.iccluster.epfl.ch:8020/datasets/goodcitylife/'
insta_files = '/harvest3r_instagram_data*.json'
news_files = '*/harvest3r_news_data*.json'
twitter_files = '*/harvest3r_twitter_data*.json'

# Check if 'column' exists in df
def hasColumn(df, column):
    try:
        df[column]
        return 1
    except:
        return 0
    

# Restrict columns and change their names
def getCols(df):
    if(hasColumn(df, '_source.sentiment')):	
        df_ = df.select(df._id.alias("id"), 
            df._source.sentiment.alias('sentiment'),
            df._source.image_src.alias('link'))
    else:
        df = df.withColumn('sentiment', lit('null'))
        df_ = df.select(df._id.alias("id"), 
            df.sentiment.alias('sentiment'),
            df._source.image_src.alias('link'))
    return(df_)

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

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october']
for m in months:
    file_list = []
    for path in all_paths:
        if(fnmatch.fnmatch(path,'*/' + m + insta_files)):
            file_list.append(path)

    # Define Schema so that we can define an empty df
    schema = StructType([StructField('id',StringType(),True),StructField('sentiment',StringType(),True),
                        StructField('link',StringType(),True)])

    # Empty df
    cleaned_df = sqlContext.createDataFrame(sc.emptyRDD(), schema)
    for f in file_list[:15]:
        df_temp = sqlContext.read.json(f)
        s_temp = getCols(df_temp)
        cleaned_df = cleaned_df.unionAll(s_temp)

    cleaned_df.write.parquet('file:///home/padh/insta_data' + '_' + m[:3]+'1.parquet')

    cleaned_df = sqlContext.createDataFrame(sc.emptyRDD(), schema)
    for f in file_list[15:]:
        df_temp = sqlContext.read.json(f)
        s_temp = getCols(df_temp)
        cleaned_df = cleaned_df.unionAll(s_temp)

    cleaned_df.write.parquet('file:///home/padh/insta_data' + '_' + m[:3]+'2.parquet')

