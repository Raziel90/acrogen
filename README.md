# Acrogen
Generate Acronyms from keywords

## How to use:
`python acrogen.py -i keywords.txt -d vocab.txt -o acros`

---
### Arguments:
- `-i` keyword file 
- `-d` dictionary file
- `-o` acronym file 
- `-v` verbose (True/False)
- `-M` max number of keyword elements in the acronym
- `-a` additional Acronym

---
### Default values:
- `keywords.txt` input file containing keywords to generate acronyms
- `vocab.txt` input file containing vocabulary file with words to match
- `acros` output file with acronyms