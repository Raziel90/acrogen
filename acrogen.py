# -*- coding: utf-8 -*-
"""
Spyder Editor

Find Cool Acronyms for the Team Name
"""

import getopt
import re
import sys
from itertools import permutations, product

from tqdm import tqdm


def read_vocabulary(filename="vocab.txt"):
    with open(filename) as word_file:
        vocabulary = set(word.strip() for word in word_file.readlines())
    return vocabulary


def isVowel(key):
    return key.lower() in ['a', 'e', 'i', 'o', 'u']


def find_wowels(key: str):
    return list(set(re.findall(r'[aeiou]', key.lower())));


def is_in_vocab(vocabulary, word: str):
    return word.lower() in vocabulary


def find_bases(Keywords):
    # only initials
    bases = {key: [key[0]] for key in Keywords}
    bases_unique = set(Keywords)

    # plus pairs if not both vowel/consonnant
    for key in Keywords:
        key_vowels = find_wowels(key)
        for letter in key_vowels:
            if key[0].lower() != letter and key[0] + letter not in bases_unique:
                bases[key].append(key[0] + letter)
                bases_unique.add(key[0] + letter)
        bases[key] = list(set(bases[key]))

    return bases


def extract_acronyms(bases, vocabulary):
    acronyms = set()
    comb = list(set(product(*bases.values())))
    for c in tqdm(comb):
        perm = permutations(c)
        for p in perm:
            for acrolen in range(2, 6):
                w = ''.join(p[:acrolen])
                if len(w) > 3 and w not in acronyms and is_in_vocab(vocabulary, w):
                    acronyms.add(w)
    # sorted
    return list(sorted(acronyms))


def save_acronyms(acronyms, filename='acros'):
    with open(filename, 'w') as acrofile:
        acrofile.write('\n'.join(acronyms))


def main(argv):
    """
    Keywords = ['Cognitive',
                'Intelligent',
                'Robot',
                'Learning',
                'Autonomous',
                'Manipulation',
                'Smart']
    """
    opts = []
    keywordfile, dictionaryfile, outputfile = ('keywords.txt', 'vocab.txt', 'acros')
    verbose = False
    try:
        opts, args = getopt.getopt(argv, "i:d:v:o", ["input", "dictionary", "verbose", "output"])
    except getopt.GetoptError as err:
        print(str(err))
        exit(-1)

    for o, a in opts:

        if o in ('-i', '--input'):
            keywordfile = a
        elif o in ('-d', '--dictionary'):
            dictionaryfile = a
        elif o in ('-v', '--verbose'):
            verbose = a
        elif o in ('-o', '--output'):
            outputfile = a
        else:
            assert False, "unhandled option!"

    Keywords = read_vocabulary(keywordfile)
    vocabulary = read_vocabulary(dictionaryfile)
    bases = find_bases(Keywords)
    acronyms = extract_acronyms(bases, vocabulary)
    save_acronyms(acronyms, outputfile)

    if verbose:
        print("bases are " + str(bases))
        print(acronyms)
    print(str(len(acronyms)) + ' Acronyms Found!')


if __name__ == '__main__':
    main(sys.argv[1:])
