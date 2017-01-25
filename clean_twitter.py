import json
import subprocess
import fnmatch
from pyspark import SparkConf, SparkContext
import pyspark.sql
from pyspark.sql.types import *	
from pyspark.sql import SQLContext

conf = SparkConf().setAppName("ADA-gcl")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
sqlContext.setConf("spark.sql.parquet.compression.codec", "snappy")

# Path definitions
base_path = 'hdfs://iccluster046.iccluster.epfl.ch:8020/datasets/goodcitylife/october'
insta_files = '*/harvest3r_instagram_data*.json'
news_files = '*/harvest3r_news_data*.json'
twitter_files = '*/harvest3r_twitter_data*.json'

def getCols(df):
    df_ = df.select(df._id.alias("id"), 
                 df._source.lang.alias('language'),
                 df._source.sentiment.alias('sentiment'),
                 df._source.source_location.alias('location'),
                 df._source.main.alias('main'),
                 df._source.published.alias('date'))
    return(df_)


#Get all files under a particular directory
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

file_list = []
all_paths = get_paths(base_path, True)
for path in all_paths:
    if(fnmatch.fnmatch(path, twitter_files)):
        file_list.append(path)


schema = StructType([StructField('id',StringType(),True),StructField('language',StringType(),True),StructField('sentiment',StringType(),True),
                    StructField('location',StringType(),True),StructField('main',StringType(),True),StructField('date',StringType(),True)])

cleaned_df = sqlContext.createDataFrame(sc.emptyRDD(), schema)

for f in file_list[:15]:
    df_temp = sqlContext.read.json(f)
    s_temp = getCols(df_temp)
    cleaned_df = cleaned_df.unionAll(s_temp)

cleaned_df.write.parquet('file:///home/fang/twitter_gender.parquet')
