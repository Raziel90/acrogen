# -*- coding: utf-8 -*-
"""
Spyder Editor

Find Cool Acronyms for the Team Name
"""

import getopt
import sys

from acronym_discoverer import Acronym_Discoverer


def read_vocabulary(filename="vocab.txt"):
    with open(filename) as word_file:
        vocabulary = set(word.strip() for word in word_file.readlines())
    return vocabulary

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
    max_len = 6
    verbose = False
    try:
        opts, args = getopt.getopt(argv, "i:d:v:o:M", ["input", "dictionary", "verbose", "output", "max_length"])
    except getopt.GetoptError as err:
        print(str(err))
        exit(-1)

    for o, a in opts:

        if o in ('-i', '--input'):
            keywordfile = a
        elif o in ('-d', '--dictionary'):
            dictionaryfile = a
        elif o in ('-v', '--verbose'):
            verbose = True
        elif o in ('-o', '--output'):
            outputfile = a
        elif o in ("-M", "--max_length"):
            max_len = a
        else:
            assert False, "unhandled option!"

    Keywords = read_vocabulary(keywordfile)
    vocabulary = read_vocabulary(dictionaryfile)

    generator = Acronym_Discoverer(Keywords, vocabulary)
    acronyms = generator.compute_acronyms(acronym_lengths=range(2, max_len))
    # bases = find_bases(Keywords)
    # acronyms = extract_acronyms(bases, vocabulary)

    save_acronyms(acronyms, outputfile)

    if verbose:
        print("bases are " + str(generator.bases))
        print(acronyms)
    print(str(len(acronyms)) + ' Acronyms Found!')


if __name__ == '__main__':
    main(sys.argv[1:])
