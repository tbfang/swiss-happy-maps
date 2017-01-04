import json
import subprocess
import fnmatch
from pyspark import SparkConf, SparkContext

# Defining sc
conf = SparkConf().setAppName("ADA-GCL")
sc = SparkContext(conf=conf)

# Path definitions
base_path = 'hdfs://iccluster046.iccluster.epfl.ch:8020/datasets/goodcitylife'
insta_files='*/harvest3r_instagram_data*.json'
news_files='*/harvest3r_news_data*.json'
twitter_files='*/harvest3r_twitter_data*.json'

# Count number of files with and without sentiment at 'path'
def count_sentiment(path):
    rdd = sc.wholeTextFiles(path).values()
    parsed = rdd.map(json.loads)
    m=parsed.top(1)
    no_sentiment=0
    sentiment=0
    for i in range(len(m[0])):
        if 'sentiment' not in m[0][i]['_source'].keys():
            no_sentiment+=1
        else:
            sentiment+=1
    return no_sentiment, sentiment

# Get all files under a particular directory
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
	if(fnmatch.fnmatch(path, insta_files)):
		file_list.append(path)

count_wo_sentiment=0
count_w_sentiment=0

for f in file_list:
	no_sent,sent = count_sentiment(f)
	count_wo_sentiment += no_sent
	count_w_sentiment += sent
print('Posts w/o sentiment: %d' % count_wo_sentiment)
print('Posts with sentiment: %d' % count_w_sentiment)
