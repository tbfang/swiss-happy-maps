# Evolution of happiness over time for different places in Switzerland

## Abstract
Switzerland is always near the top when we see the list of happiest countries in the world. So what is it that makes Switzerland so happy? Is it the mountains? The lakes? The money? We try to do an analysis of how happy each part of Switzerland is during different times of the year and what is it that makes it happy by doing a sentiment analysis of geotagged social media posts. We describe our approach below.

## Data description and methodology
* **Twitter** - We will use the twitter dataset from 2012 provided by Prof. Catasta. We will use machine learning techniques on the text of the tweets as well as use hashtags and emoticons to do a sentiment analysis on the tweets. We will also look for a corpus on which we can train our model. [1] suggests several possible datasets we can use to train our model.
* **Instagram** -  We will use the instagram data provided by Prof. Catasta in a similar way as the twitter data to do a sentiment analysis. We can also analyze the image along with the text and hashtags.

Since the data for Twitter and Instagram is geolocated, doing a sentiment analysis will finally give us geolocated sentiments for different places in Switzerland. We will analyze this data to figure out which regions are happier during which time of the year. We can also additionally do a frequency analysis on the tweets to figure out what words come up most frequently at a particular time of the year over the year to figure out a reason for a change in general sentiment for each region.

And if there is still time after this ( which is unlikely ) we can restric ourselves to a particular city, and make a 'happy map' similar to [3]. We can use the same methodology as they use to get the shortest path which maximizes happiness. But since we have a happiness map that evolves over time, such a path will also change over time rather than remain fixed. Fox example some roads might me more beautiful in fall, etc.

## Feasibility and Risks
We describe the risks we face in doing this analysis as well as what we can do to counter those risks.
* We do not have a manually labelled dataset which says whether a particular tweet/instagram post is positive or negative. There are several datasets available to train english tweets, but it might be difficult to find training sets for French and German tweets. So we might need to do unsupervised learning. [2] suggests several ways in which unsupervised learning has been successfully applied for sentiment analysis so it should still be doable.
* Use of slang and incorrect spelling in the tweets might make the sentiment analysis more difficult.
* We might not have enough data if we wish to use neural networks to do unsupervised learning.
* If there is no significant change in sentiment over time, the results and visualization might not be so interesting. In this case we would restric ourselves to a particular genre of tweets and see if the results are more interesting. For example we can look at posts that only refer to the geography and climate ( lakes, mountains, skiing, etc ). Or any other genre, like politics, entertainment etc.

## Deliverables
### Machine Learning
* A result of the sentiment analysis of twitter and instagram posts along with a measure of how good our model is in doing sentiment analysis.
### Visualization
* Using the results of the sentiment analysis to make a map of Switzerland which shows how happy each part is. The map should eveolve over time.
* If we can also get the reason for change in the sentiment by doing the frequency analysis, we can use http://cesiumjs.org/ to have objects appear at places where we know the reason for the sentiment. For example along with showing that there is a positive sentiment in verbier in the winter, we show a picture of a ski there.

## Timeplan

|                       | 7-13 Nov  | 14-20 Nov | 21-27 Nov | 28 Nov-4 Dec | 5-11 Dec | 12-18 Dec | 19-25 Dec | 26 Dec-1 Jan | 2-8 Jan | 9-15 Jan | 15-22 Jan
|---------------------------|----------------|------------|-------------|-------------|----------------|------------|-------------|-------------|----------------|-----------|------------|
| Preparing and cleaning the data |        *        |     *       |              |             |                |            |             |             |                |           |            |
| Sentiment Analysis           |                |            |      *       |      *       |       *         |   *        |    *      |      *       |            |       |            |
| Result Visualization      |                |            |             |             |                |            |       *      |       *      |       *         |     *      |      *     |

