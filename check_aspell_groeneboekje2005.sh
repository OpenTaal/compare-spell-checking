set -xe
cd groeneboekje2005
SPELL_VERSION=`dpkg -l|grep libaspell|grep -v dev|awk '{print $3}'`
DICT_VERSION=`dpkg -l|grep aspell-nl|awk '{print $3}'`
DESTINATION=aspell\_$SPELL_VERSION\_nl\_$DICT_VERSION
if [ ! -e ../$DESTINATION ]
then
    mkdir ../$DESTINATION
fi
if [ -e groeneboekje2005_lemmas.txt ]
then
    ../check_hunspell.py verifyaspell ../$DESTINATION groeneboekje2005_lemmas.txt
else
    echo Missing word list groeneboekje2005_lemmas.txt
fi
#if [ -e groeneboekje2005_flexies.txt ]
#then
#   ../check_hunspell.py verifyaspell ../$DESTINATION groeneboekje2005_flexies.txt
#else
#    echo Missing word list groeneboekje2005_flexies.txt
#fi
cd ..
