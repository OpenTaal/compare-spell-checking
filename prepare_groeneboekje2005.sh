set -xe
cd groeneboekje2005
if [ -e Taalunie_groeneboekje2005_unieke_lemmas.txt ]
then
    ../prepare.py Taalunie_groeneboekje2005_unieke_lemmas.txt groeneboekje2005_lemmas.txt
else
    echo Missing word list Groene Boekje
fi
cd ..
