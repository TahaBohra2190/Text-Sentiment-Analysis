import string
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sent_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if(pos > neg):
        print("Generally positive")
    else:
        print("Generally Negative")


text = open("read.txt", encoding='utf-8').read()
text_lower = text.lower()
cleaned_text = text_lower.translate(str.maketrans('', '', string.punctuation))
tokenised_words = word_tokenize(cleaned_text,"English")


finalised_list = []
for words in tokenised_words:
    if words not in stopwords.words('english'):
        finalised_list.append(words)
print(finalised_list)

emotion_list = []
word = []
emotions = []
with open("emotions.txt", 'r') as file:
    for line in file:
        cleared_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = cleared_line.split(':')
        if word in finalised_list:
            emotion_list.append(emotion)

print(emotion_list)
w= Counter(emotion_list)
print(w)


fig1 , ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig1.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
sent_analyse(cleaned_text)