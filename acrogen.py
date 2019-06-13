# -*- coding: utf-8 -*-
"""
Spyder Editor

Find Cool Acronyms for the Team Name
"""
from itertools import combinations, permutations 

Keywords = ['Cognitive', 
            'Intelligent', 
            'Robot', 
            'Learning', 
            'Autonomous', 
            'Manipulation']
            
            
Initials = [key[0] for key in Keywords]
acronyms = []

for acrolen in range(2,len(Keywords)):
    
    comb = combinations(Initials, acrolen)
    
    for c in comb:
        perm = permutations(c)
        
        for p in perm:
            acronyms += [''.join(p)]
            
            
        
        
print(str(len(acronyms)) + ' Acronyms Found!')

with open('acros', 'w') as acrofile:
    acrofile.write('\n'.join(acronyms))
    