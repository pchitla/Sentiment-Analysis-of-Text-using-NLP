# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import matplotlib.pyplot as plt

# To get data from a file
text = open('read.txt', encoding='utf-8').read()

# To convert the string into lowercase
lower_case = text.lower()

# To remove puntuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Tokenization means to split the sentence into words of list
tokenized_words = word_tokenize(cleaned_text, "english")

# Initialize a list of stop words that have no meaning/emotion to it


final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# NLP Emotion Algorithm

# Check if the word in final_words list is also present in the emotions.txt file

# Open the emotions.txt file

# Loop through each line and clear it
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_it = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_it.split(':')

        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)

w = Counter(emotion_list)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    negat = score['neg']
    posit = score['pos']
    if negat > posit:
        print('Negative Sentiment')
    elif posit > negat:
        print('Positive Sentiment')
    else:
        print('Neutral Sentiment')


sentiment_analyse(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
