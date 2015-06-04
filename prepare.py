#!/usr/bin/env python3

import sys


if len(sys.argv) != 3:
    print('This application prepares a file for spell check comparing.')
    print('')
    print('Input file needs to be in UTF-8 with one word per line.')
    print('A word is allowed to contain spaces.')
    print('')
    print('Output file will contain the unique words from the input file and')
    print('unique words (with a minimum length of two) that were extracted')
    print('from words which contain spaces.')
    print('')
    print('ERROR: Missing path to input file and/or output file.')
    exit(1)

words = {}
total = 0
spaces = 0
input_file = open(sys.argv[1], 'r').readlines()
for word in input_file:
    word = word[:-1]
    if word == '':
        continue
    if word not in words:
        total += 1
        words[word] = ''
        if ' ' in word:
            spaces += 1
            for part in word.split(' '):
                if len(part) > 1 and part not in words:
                    words[part] = ''
print('Expaned by {} from {} words of which {} contained spaces to {} total number of words.'.format(len(words) - total, total, spaces, len(words)))

output_file = open(sys.argv[2], 'w')
for word in sorted(words):
    output_file.write('{}\n'.format(word))
