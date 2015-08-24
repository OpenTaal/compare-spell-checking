set -xe
cd groeneboekje2015
SPELL_VERSION=`dpkg -l|grep libhunspell|grep -v dev|awk '{print $3}'`
DICT_VERSION=`dpkg -l|grep myspell-nl|awk '{print $3}'`
DESTINATION=hunspell\_$SPELL_VERSION\_nl\_$DICT_VERSION
if [ ! -e ../$DESTINATION ]
then
    mkdir ../$DESTINATION
fi
if [ -e groeneboekje2015_lemmas.txt ]
then
    ../check_hunspell.py verify ../$DESTINATION groeneboekje2015_lemmas.txt
else
    echo Missing word list groeneboekje2015_lemmas.txt
fi
if [ -e groeneboekje2015_lemmas.txt ]
then
    ../check_hunspell.py verify ../$DESTINATION groeneboekje2015_flexies.txt
else
    echo Missing word list groeneboekje2015_lemmas.txt
fi
cd ..
