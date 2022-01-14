import pymorphy2
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
morph = pymorphy2.MorphAnalyzer()

text = open("full.txt", encoding = 'utf8').read()

# Подготовка текста и токенизация
cleantext = text.lower()
cleantext = re.sub('[^а-яА-Я]', ' ', cleantext)
cleantext = re.sub(r'\s+', ' ', cleantext)
justtokens = word_tokenize(cleantext)

#Удаление стоп-слов

filtlm = []
SW = stopwords.words('russian')
for w in justtokens:
    if w not in SW:
        filtlm.append(w)

#Лемматизация
lemmtok = []
for word in filtlm:
    pas = morph.parse(word)[0]
    lemmtok.append(pas.normal_form)
