set -xe
cd groeneboekje2015
SPELL_VERSION=`dpkg -l|grep libaspell|grep -v dev|awk '{print $3}'`
DICT_VERSION=`dpkg -l|grep aspell-nl|awk '{print $3}'`
DESTINATION=aspell\_$SPELL_VERSION\_nl\_$DICT_VERSION
if [ ! -e ../$DESTINATION ]
then
    mkdir ../$DESTINATION
fi
../check_hunspell.py verifyaspell ../$DESTINATION groeneboekje2015_lemmas.txt
../check_hunspell.py verifyaspell ../$DESTINATION groeneboekje2015_flexies.txt
cd ..
