#!/usr/bin/env python3

import hunspell
import aspell
import sys


if len(sys.argv) != 4:
    print(
        'This application {} will check spelling with Hunspell.'.format(sys.argv[0]))
    print('')
    print('Input file needs to be in UTF-8 with one lemma per line.')
    print('A lemma is allowed to contain spaces but this is not recommended')
    print('when comparing spell checking in documents.')
    print('Also check only base forms and flexions, no proper names.')
    print('Output files will report on:')
    print(
        '- words without spaces check correct with suggestions called _nospace_correct.tsv')
    print(
        '- words without spaces check incorrect with suggestions called _nospace_incorrect.tsv')
    print(
        '- words with spaces check correct with suggestions called _space_correct.tsv')
    print(
        '- words with spaces check incorrect with suggestions called _space_incorrect.tsv')
    print('- report called _report.tsv with:')
    print('  - name and version spell checker')
    print('  - name and version dictionary')
    print('  - name of input file')
    print('  - total number of checked words')
    print('  - total number of correct words')
    print('  - total number of incorrect words')
    print('  - percentage of correct words')
    print(
        '  - the latter four also reported separately for words with and without spaces')
    print('')
    print(
        'ERROR: Missing option [verify|correct|verifyaspell], path to destination directory, path to input file.')
    exit(1)

mode = sys.argv[1]
if mode not in ('verify', 'correct', 'verifyaspell', ):
    print(
        'ERROR: Missing option [verify|correct|verifyaspell], path to destination directory, path to input file.')

dest = sys.argv[2]
checker = dest.split('_')[0]
if '../' in checker:
    checker = checker.split('../')[1]
if '..\\' in checker:
    checker = checker.split('..\\')[1]
library = dest.split('_')[1]
language = dest.split('_')[2]
dictionary = dest.split('_')[3]
filename = sys.argv[3]
basename = filename[:-4]

aobj = None
hobj = None
if 'aspell' in mode:
    aobj = aspell.Speller(('lang', language), ('master', language), )
    encoding = aobj.ConfigKeys()['encoding'][1]
    if encoding != 'UTF-8':
        print('ERROR: Wrong encoding, {} should be UTF-8'.format(encoding))
        exit(1)
else:
    hobj = hunspell.HunSpell(
        '/usr/share/hunspell/{}.dic'.format(language), '/usr/share/hunspell/%s.aff' % language)
    encoding = hobj.get_dic_encoding()
    if encoding != 'UTF-8':
        print('ERROR: Wrong encoding, {} should be UTF-8'.format(encoding))
        exit(1)

report = open('{}/{}_report.tsv'.format(dest, basename), 'w')
report.write('checker\t{}\n'.format(checker))
report.write('library\t{}\n'.format(library))
report.write('language\t{}\n'.format(language))
report.write('dictionary\t{}\n'.format(dictionary))
report.write('wordlist\t{}\n'.format(filename))
report.write('\n')

total_correct_nospace = 0
total_correct_space = 0
total_incorrect_nospace = 0
total_incorrect_space = 0
correct_nospace = open('{}/{}_correct_nospace.tsv'.format(dest, basename), 'w')
correct_space = open('{}/{}_correct_space.tsv'.format(dest, basename), 'w')
incorrect_nospace = open(
    '{}/{}_incorrect_nospace.tsv'.format(dest, basename), 'w')
incorrect_space = open('{}/{}_incorrect_space.tsv'.format(dest, basename), 'w')

words = open(sys.argv[3], 'r').readlines()
for word in words:
    word = word[:-1]
    if word == '':
        continue
    if 'aspell' in mode:
        if (mode == 'verifyaspell' and aobj.check(word)) or (mode == 'correctaspell' and not aobj.check(word)):
            if ' ' in word:
                total_correct_space += 1
                correct_space.write(
                    '{}\t{}\n'.format(word, '\t'.join(aobj.suggest(word))))
            else:
                total_correct_nospace += 1
                correct_nospace.write(
                    '{}\t{}\n'.format(word, '\t'.join(aobj.suggest(word))))
        else:
            if ' ' in word:
                total_incorrect_space += 1
                incorrect_space.write(
                    '{}\t{}\n'.format(word, '\t'.join(aobj.suggest(word))))
            else:
                total_incorrect_nospace += 1
                incorrect_nospace.write(
                    '{}\t{}\n'.format(word, '\t'.join(aobj.suggest(word))))
    else:
        if (mode == 'verify' and hobj.spell(word)) or (mode == 'correct' and not hobj.spell(word)):
            if ' ' in word:
                total_correct_space += 1
                correct_space.write(
                    '{}\t{}\n'.format(word, '\t'.join(hobj.suggest(word))))
            else:
                total_correct_nospace += 1
                correct_nospace.write(
                    '{}\t{}\n'.format(word, '\t'.join(hobj.suggest(word))))
        else:
            if ' ' in word:
                total_incorrect_space += 1
                incorrect_space.write(
                    '{}\t{}\n'.format(word, '\t'.join(hobj.suggest(word))))
            else:
                total_incorrect_nospace += 1
                incorrect_nospace.write(
                    '{}\t{}\n'.format(word, '\t'.join(hobj.suggest(word))))

total_space = total_correct_space + total_incorrect_space
total_nospace = total_correct_nospace + total_incorrect_nospace
total_correct = total_correct_space + total_correct_nospace
total_incorrect = total_incorrect_space + total_incorrect_nospace
total = total_correct + total_incorrect

report.write('total\t{}\n'.format(total))
report.write('correct\t{}\n'.format(total_correct))
report.write('incorrect\t{}\n'.format(total_incorrect))
report.write('efficiency\t{:0.1f}%\n'.format(100.0 * total_correct / total))
report.write('\n')
report.write('total space\t{}\n'.format(total_space))
report.write('correct space\t{}\n'.format(total_correct_space))
report.write('incorrect space\t{}\n'.format(total_incorrect_space))
report.write('efficien. space\t{:0.1f}%\n'.format(
    100.0 * total_correct_space / total_space))
report.write('\n')
report.write('total nospace\t{}\n'.format(total_nospace))
report.write('correct nospace\t{}\n'.format(total_correct_nospace))
report.write('incorrect nospace\t{}\n'.format(total_incorrect_nospace))
report.write('efficiency nospace\t{:0.1f}%\n'.format(
    100.0 * total_correct_nospace / total_nospace))
