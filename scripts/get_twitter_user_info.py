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
sqlContext.setConf("spark.sql.parquet.compression.codec", "snappy")

# Path definitions
base_path = 'hdfs://iccluster046.iccluster.epfl.ch:8020/datasets/goodcitylife/'
insta_files = '/harvest3r_instagram_data*.json'
news_files = '*/harvest3r_news_data*.json'
twitter_files = '*/harvest3r_twitter_data*.json'

def getCols(df):
    df_ = df.select(df._id.alias("id"), 
                 df._source.source_followers.alias('num_followers'),
                 df._source.source_following.alias('num_following'),
                 df._source.mentions.alias('mentions'))
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

all_paths = get_paths(base_path, True)
                    
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october']
for m in months:
    file_list = []
    for path in all_paths:
        if(fnmatch.fnmatch(path,'*/' + m + twitter_files)):
            file_list.append(path)

    # Define Schema so that we can define an empty df
    schema = StructType([StructField('id',StringType(),True),
                         StructField('num_followers',IntegerType(),True),
                         StructField('num_following',IntegerType(),True),
                         StructField('mentions',ArrayType(StringType(), True),True)])

    # Empty df
    cleaned_df = sqlContext.createDataFrame(sc.emptyRDD(), schema)
    for f in file_list[:]:
        df_temp = sqlContext.read.json(f)
        s_temp = getCols(df_temp)
        cleaned_df = cleaned_df.unionAll(s_temp)

    cleaned_df.write.parquet('file:///home/fang/twitter_user_info' + '_' + m[:3]+'.parquet')


                    
                    
                    
                    
# for path in all_paths:
#     if(fnmatch.fnmatch(path, twitter_files)):
#         file_list.append(path)


# schema = StructType([StructField('id',StringType(),True),StructField('gender',StringType(),True),StructField('canton',StringType(),True)])

# cleaned_df = sqlContext.createDataFrame(sc.emptyRDD(), schema)

# for f in file_list[:15]:
#     df_temp = sqlContext.read.json(f)
#     s_temp = getCols(df_temp)
#     cleaned_df = cleaned_df.unionAll(s_temp)

# cleaned_df.write.parquet('file:///home/fang/twitter_cleaned_oct2.parquet')

