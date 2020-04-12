import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

gambler = open('Gambler.txt', encoding='utf-8').read()
lower_case = gambler.lower()
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
print(w),

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
