#!/usr/bin/env python
# coding: utf-8

# In[67]:


txt = 'На вокза́ле Никола́евской желе́зной доро́ги встре́тились два́ прия́теля: оди́н то́лстый, друго́й то́нкий.'

def wordhandle (x):
    bad_chars = [';', ':', '!', '*', '.', ',']
    x = ''.join(i for i in x if not i in bad_chars)
    x = x.lower()
    words = x.split()
    wordset = set(words)
    return wordset

def process (i):
    simple_vowels = 'уеыаоэяию'
    stressed_vowels = 'а́е́и́о́у́ы́э́ю́я́'
    exch = {
        'а́': 'а',
        'е́': 'е',
        'и́': 'и',
        'о́': 'о',
        'у́': 'у',
        'ы́': 'ы',
        'э́': 'э',
        'ю́': 'ю',
        'я́': 'я'
    }
    wordlist = []
    wordlist.append(wordhandle(txt))
    for line in wordlist:
        for character in line:
            if character in exch:
                line = line.replace(character, exch[character])
            return (line)
        
process (txt)


# In[ ]:




