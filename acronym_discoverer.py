import re
from itertools import permutations, product

from tqdm import tqdm


class Acronym_Discoverer:

    def __init__(self, Keywords, dictionary=None):

        bases = {key: [key[0]] for key in Keywords}
        bases_unique = set(Keywords)
        __vowels = r'[aeiou]'

        # plus pairs if not both vowel/consonnant
        for key in Keywords:
            key_vowels = list(set(re.findall(__vowels, key.lower())))
            for letter in key_vowels:
                if key[0].lower() != letter and key[0] + letter not in bases_unique:
                    bases[key].append(key[0] + letter)
                    bases_unique.add(key[0] + letter)
            bases[key] = list(set(bases[key]))

        self.bases = bases
        self.dictionary = dictionary
        if dictionary is not None:
            self.__dictionary_condition = lambda x: x.lower() in self.dictionary
        else:
            self.__dictionary_condition = lambda x: True

    def get_bases(self):

        return self.bases

    def compute_acronyms(self, acronym_lengths=None, add_acro=None):
        # TODO: Introduce Phonetical Acronyms via substitution of combinations of letters with similar sounds.
        bases = self.bases
        if acronym_lengths is None:
            acronym_lengths = range(2, min(10, len(bases.keys())))
        acronyms = set()
        comb = list(set(product(*bases.values())))
        for c in tqdm(comb):
            if add_acro is not None:
                c += (add_acro,)
            perm = permutations(c)
            for p in perm:
                for acrolen in acronym_lengths:
                    acro_components = p[:acrolen]

                    w = ''.join(acro_components)
                    if w not in acronyms and self.__dictionary_condition(w):
                        acronyms.add(w)
        # sorted
        return list(sorted(acronyms))
