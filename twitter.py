import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('cannabis') \
        .setSince("2019-01-01") \
        .setUntil("2020-01-01") \
        .setMaxTweets(1000)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    text_tweets = []
    for tweet in tweets:
        text_tweets.append([tweet.text])

    return text_tweets

text = ""
text_tweets = get_tweets()
lenght = len(text_tweets)
for i in range(0, lenght):
    text = text_tweets[i][0] + " " + text

lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = word_tokenize(cleaned_text, "english")

final_words= []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

print(final_words)

emotion_list = []
with open('emotion.txt', 'r') as f:
    for line in f:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Vibe")

sentiment_analyze(cleaned_text)

plt.bar(w.keys(),w.values())
plt.xticks(rotation=90)
plt.savefig('graph.png')
plt.show()
