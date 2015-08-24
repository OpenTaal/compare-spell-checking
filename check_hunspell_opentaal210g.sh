set -xe
cd opentaal210g
SPELL_VERSION=`dpkg -l|grep libhunspell|grep -v dev|awk '{print $3}'`
DICT_VERSION=`dpkg -l|grep myspell-nl|awk '{print $3}'`
DESTINATION=hunspell\_$SPELL_VERSION\_nl\_$DICT_VERSION
if [ ! -e ../$DESTINATION ]
then
    mkdir ../$DESTINATION
fi
../check_hunspell.py verify ../$DESTINATION opentaal210g_gekeurd.txt
../check_hunspell.py verify ../$DESTINATION opentaal210g_flexies.txt
../check_hunspell.py verify ../$DESTINATION opentaal210g_ongekeurd.txt
#../check_hunspell.py verify $DESTINATION opentaal210g_verwarrend.txt
