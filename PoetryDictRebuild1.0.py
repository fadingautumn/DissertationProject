text = """Буря мглою небо кроет,
Вихри снежные крутя;
То, как зверь, она завоет,
То заплачет, как дитя,
То по кровле обветшалой
Вдруг соломой зашумит,
То, как путник запоздалый,
К нам в окошко застучит."""

dictmeter = {
    '010101': 'Трёхстопный ямб',
    '01010101': 'Четырёхстопный ямб',
    '0101010101': 'Пятистопный ямб',
    '010101010101': 'Шестистопный ямб',
    '01010101010101': 'Семистопный ямб',
    '0101010101010101': 'Восьмистопный ямб',
    '101010': 'Трёхстопный хорей',
    '10101010': 'Четырёхстопный хорей',
    '11101010': 'Четырёхстопный хорей',
    '1010001': 'Четырёхстопный хорей',
    '1010101': 'Четырёхстопный хорей',
    '1010101010': 'Пятистопный хорей',
    '101010101010': 'Шестистопный хорей',
    '10101010101010': 'Семистопный хорей',
    '1010101010101010': 'Восьмистопный хорей',
    '100100100': 'Трёхстопный дактиль',
    '100100100100': 'Четырёхстопный дактиль',
    '100100100100100': 'Пятистопный дактиль',
    '100100100100100100': 'Шестистопный дактиль',
    '010010010': 'Трёхстопный амфибрахий',
    '010010010010': 'Четырёхстопный амфибрахий',
    '010010010010010': 'Пятистопный амфибрахий',
    '010010010010010010': 'Шестистопный амфибрахий',
    '001001001': 'Трёхстопный анапест',
    '001001001001': 'Четырёхстопный анапест',
    '001001001001001': 'Пятистопный анапест',
    '001001001001001001': 'Шестистопный анапест'
    
}

import nltk
import pymorphy2
import re
import difflib
import collections
from collections import Counter
from wiktionaryparser import WiktionaryParser
from nltk import word_tokenize
parser = WiktionaryParser()
parser.set_default_language('russian')
morph = pymorphy2.MorphAnalyzer()

def get_accent(unaccword):
    word = parser.fetch(unaccword)
    first_mean = word[0]
    definitive = first_mean.get('definitions')
    if len(definitive) > 0:
        for element in definitive:
            sign1 = element.get('text')
            sign1 = sign1[0]
            sign1 = sign1.split(' ')
            sign1 = sign1[0]
            return sign1
    elif len(definitive) == 0:
        parse = morph.parse(unaccword)[0]
        morphword = parse.normal_form
        word = parser.fetch(morphword)
        first_mean = word[0]
        definitive = first_mean.get('definitions')
        for element in definitive:
            sign1 = element.get('text')
            sign1 = sign1[0]
            sign1 = sign1.split(' ')
            sign1 = sign1[0]
            return sign1
    else:
        return "Что-то пошло не так"
    
def get_numbers (stressword):
    accent_word = get_accent(stressword)
    unaccent = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    substr = ''
    try:
        for i in accent_word:
            if i in unaccent:
                substr += '0'
            elif i == '́' or i == 'ё':
                substr += '1'
            else:
                continue
    except:
        print ('Что-то пошло не так')
        pass
    if len(substr) == 1:
        substr = '1'
    true_sub = substr.replace('01', '1')
    return true_sub

def get_verse_size(rawpoem):
    lines = text.split('\n')
    supersize = []
    for line in lines:
        cleantext = line.lower() 
        cleantext = re.sub('[^а-я]', ' ', cleantext)
        words = nltk.word_tokenize(cleantext)
        razmer = ''
        for word in words:
            razmer += get_numbers(word)
        supersize.append(razmer)
    return supersize

def best_verse_size(num_lines):
  line_size_list = []
  for i in get_verse_size(num_lines):
    temp = 0
    best_fit_size = ''
    for key in dictmeter:
      output = int(difflib.SequenceMatcher(None, i, key).ratio()*100)
      if temp < output and temp < 100:
        temp = output
        best_fit_size = dictmeter[key]
    line_size_list.append(best_fit_size)
  counter = Counter(line_size_list)
  max_count = counter.most_common(2)
  max_count1 = f'{max_count[0][0]} встречается в {max_count[0][1]} строках стихотворения, а значит, он наиболее вероятен. '
  max_count2 = f'Также программа выделила {max_count[1][0]}, который встречается в {max_count[1][1]} строках стихотворения.'
  return max_count1 + max_count2

best_verse_size(text)
