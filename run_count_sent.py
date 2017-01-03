import json
import os
import glob

def count_sentiment(file):
    rdd = sc.wholeTextFiles(file).values()
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

#path = os.getcwd() +'/datasets'
path = '/datasets/goodcitylife/'
instagram_files='/harvest3r_instagram_data*.json'
news_files='/harvest3r_news_data*.json'
twitter_files='/harvest3r_twitter_data*.json'
count_wo_sentiment=0
count_w_sentiment=0
for folder in os.listdir(path):
    for file in glob.glob(os.path.join(path,folder + instagram_files)):
        print(file)
        no_sent,sent=count_sentiment(file)
        count_wo_sentiment+=no_sent
        count_w_sentiment+=sent
print('Posts w/o sentiment: %d' % count_wo_sentiment)
print('Posts with sentiment: %d' % count_w_sentiment)