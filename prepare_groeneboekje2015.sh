set -xe
cd groeneboekje2015
if [ -e Taalunie_groeneboekje2015_unieke_lemmas.txt ]
then
    ../prepare.py Taalunie_groeneboekje2015_unieke_lemmas.txt groeneboekje2015_lemmas.txt
else
    echo Missing word list Taalunie_groeneboekje2015_unieke_lemmas.txt
fi
if [ -e Taalunie_groeneboekje2015_flexies.txt ]
then
    ../prepare.py Taalunie_groeneboekje2015_flexies.txt groeneboekje2015_flexies.txt
else
    echo Missing word list Taalunie_groeneboekje2015_flexies.txt
fi
cd ..
