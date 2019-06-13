# -*- coding: utf-8 -*-
"""
Spyder Editor

Find Cool Acronyms for the Team Name
"""
from itertools import combinations, permutations, product

with open("en_words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

Keywords = ['Cognitive',
            'Intelligent',
            'Robot',
            'Learning',
            'Autonomous',
            'Manipulation']

def isVowel(key):
    return key.lower() in ['a','e','i','o','u']

def is_english_word(word):
    return word.lower() in english_words


# only initials
bases = {key:[key[0]] for key in Keywords}
# plus pairs if not both vowel/consonnant
for key in Keywords:
    for letter in key:
        if isVowel(key[0])!=isVowel(letter):
            bases[key].append(key[0]+letter)
    bases[key] = list(set(bases[key]))

print("bases are " + str(bases))

acronyms = []

comb = list(set(product(*bases.values())))

for c in comb:
    perm = permutations(c)
    for p in perm:
        for acrolen in range(2,6):
            w = ''.join(p[:acrolen])
            if len(w)>3 and is_english_word(w):
                print(w)
                acronyms += [w]

# unique vals sorted
acronyms = list(sorted((set(acronyms))))

print(str(len(acronyms)) + ' Acronyms Found!')

with open('acros', 'w') as acrofile:
    acrofile.write('\n'.join(acronyms))
