import string
import matplotlib.pyplot as plt
from collections import Counter

text = open("read.txt", encoding='utf-8').read()
text_lower = text.lower()
cleaned_text = text_lower.translate(str.maketrans('', '', string.punctuation))
tokenised_words = cleaned_text.split()
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

finalised_list = []
for words in tokenised_words:
    if (words not in stop_words):
        finalised_list.append(words)        #cleaning up the words that dont contribute to analysis using custom stop word list
print(finalised_list)

#catching sentiment carrying words
emotion_list = []
word = []
emotions = []
with open("emotions.txt", 'r') as file:
    for line in file:
        cleared_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = cleared_line.split(':')
        if word in finalised_list:
            emotion_list.append(emotion)
w = Counter(emotion_list)
print(w)


fig1 , ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig1.autofmt_xdate()
plt.savefig('graph.png')
plt.show()