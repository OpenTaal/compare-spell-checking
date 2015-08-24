# compare-spell-checking

Compare different spell checking software in a quantitative and qualitative way.


## Specificaties

Deze opsomming bevat specificaties voor de ontwikkeling van een programma om de Spell Check API van Microsoft (en om Hunspell) te testen:

1. Het programma moet zelf onder een MIT-licentie aan Stichting OpenTaal gedoneerd worden.

2. De originele auteur van het programma mag met volledige naam in het programma genoemd worden.

3. Het programma moet in broncode en als executable opgeleverd worden.

4. Het programma moet gedocumenteerd zijn met datum, versienummer, afhankelijkheden zoals versie van besturingssysteem en benodigde frameworks.

5. Het programma meldt zo volledig mogelijk wanneer er iets is misgegaan en wat er is misgegaan. Zo veel mogelijk wordt het woord waarop de fout optrad gemeld en zo veel mogelijk additionele technische details worden gegeven.

6. Het programma moet de Spell Check API van MSDN gebruiken.

7. Het programma mag geschreven zijn in een willekeurige programmeertaal.

9. Het programma mag vanaf de commandline opgestart worden. Een grafische gebruikersinterface mag maar is niet nodig.

10. Het programma heeft de volgende drie invoerparameters:

  1. switch die letterlijk `verify` of `correct` is (verify|correct)

  2. absoluut of relatief pad bestemmingdirectory (destination directory)

  3. absoluut of relatief pad invoerbestand met woordenlijst (input file)

11. Alle tekstbestanden met woordenlijsten moeten betreffende formaat voldoen aan de volgende eisen:

  * bestand is in UTF-8 BOM tekstdocument

  * elke regel bevat een woord, een woord mag een spatie bevatten

  * spaties zullen niet aan begin of einde van de regel staan

  * er zullen geen meerdere spaties na elkaar staan

  * elke regel, ook de laatste regel, eindigt op een line feed en geen carriage return

  * alle regels eindigt op enkel alleen een line feed en geen carriage return

  * bestand bevat geen lege regels

12. Indien de eerste invoerparameter `verify` is, wordt het invoerbestand gezien als een lijst correcte woorden. Als de eerste invoerparameter `correct` is, wordt het invoerbestand gezien als een lijst van incorrecte woorden. In dit tweede geval zal het input bestand, met een TAB-karakters gescheiden, ook de correcties (tenminste één correctie) van de fout moeten bevatten.

13. In de bestemmingdirectory zullen de volgende vijf bestanden worden weggeschreven die als basis dezelfde naam hebben als het invoerbestand:

  1. rapportagebestand in TSV-formaat met op einde van de bestandnaam `_report.tsv`

  2. bestand met corecte woorden die een spatie hebben met op einde van de bestandnaam `_correct_space.tsv`

  3. bestand met incorecte woorden die een spatie hebben met op einde van de bestandnaam `_incorrect_space.tsv`

  4. bestand met corecte woorden die geen spatie hebben met op einde van de bestandnaam `_correct_nospace.tsv`

  5. bestand met corecte woorden die geen spatie hebben met op einde van de bestandnaam `_incorrect_nospace.tsv`

14. De bestanden met incorrecte én correct woorden zullen met TAB-karakters gescheiden alle suggesties in de aangeboden volgorde ook tonen.

15. De inhoud van het rapportagebestand zijn totaalcijfers die gescheiden zijn met een TAB-karakter.

    checker	NAME_SPELL_CHECKER
    library	VERSION_SPELL_CHECKER
    language	nl
    dictionary	VERSION_DICTIONARY
    wordlist	FILENAME.txt

    total	TOTAL_NUMBER_OF_WORDS
    correct	TOTAL_NUMBER_OF_CORRECT_WORDS
    incorrect	TOTAL_NUMBER_OF_INCORRECT_WORDS
    efficiency	(100*TOTAL_NUMBER_OF_CORRECT_WORDS/TOTAL_NUMBER_OF_WORDS)%

    total space	TOTAL_NUMBER_OF_WORDS_WITH_SPACE
    correct space	TOTAL_NUMBER_OF_CORRECT_WORDS_WITH_SPACE
    incorrect space	TOTAL_NUMBER_OF_INCORRECT_WORDS_WITH_SPACE
    efficien. space	(100*TOTAL_NUMBER_OF_CORRECT_WORDS_WITH_SPACE/TOTAL_NUMBER_OF_WORDS_WITH_SPACE)%

    total nospace	TOTAL_NUMBER_OF_WORDS_WITHOUT_SPACE
    correct nospace	TOTAL_NUMBER_OF_CORRECT_WORDS_WITHOUT_SPACE
    incorrect nospace	TOTAL_NUMBER_OF_INCORRECT_WORDS_WITHOUT_SPACE
    efficiency nospace	(100*TOTAL_NUMBER_OF_CORRECT_WORDS_WITHOUT_SPACE/TOTAL_NUMBER_OF_WORDS_WITHOUT_SPACE)%

Een voorbeeld van rapportagebestand gemaakt door controle met Hunspell ziet er uit als:

    checker	hunspell
    library	1.3.3-3
    language	nl
    dictionary	1:2.10-3
    wordlist	opentaal210g_flexies.txt

    total	157311
    correct	157161
    incorrect	150
    efficiency	99.9%

    total space	151
    correct space	2
    incorrect space	149
    efficien. space	1.3%

    total nospace	157160
    correct nospace	157159
    incorrect nospace	1
    efficiency nospace	100.0%

Zie de implementatie in Python voor Hunspell [check_hunspell.py](check_hunspell.py) met gegenereerde bestanden in de diverse bestemmingdirectories als referentie.


## Hunspell requirements

In order to run the tests with Hunspell on Linux, make sure the following packages are installed:

    sudo apt-get install python-dev libhunspell-dev python3-hunspell myspell-nl

Make sure personal dictonaries are empty or non-existing!


## Aspell requirements

In order to run the tests with Aspell on Linux, make sure the following packages are installed:

    sudo apt-get install aspell-dev aspell-nl
    pip3 install aspell-python-py3

Make sure personal dictonaries ~/.aspell.nl.pws and ~/.aspell.nl.prepl are empty or non-existing!


## Voorbereidingen

Om woorden met een spatie op te splitsen in afzonderlijke delen zijn er voor de woordenlijsten shellscripts waarvan de naam begint met `prepare` en eindigt op `.sh`. Deze maken gebruikt van een algemeen Pythonscript genaamd [prepare.py](prepare.py).


## Bescherming woordenlijsten

Alle woordenlijsten die betrekking hebben op het Groene Boekje of woordenlijst.org zijn *niet* opgenomen in dit project. Alleen de totaalcijfers zijn opgenomen zodat de woordenlijsten van de Taalunie en het INL beschermd blijven.


## Runnen van de testen

Voor alle testen zijn er shellscipts eindigent op `.sh` of batchscripts eindigent op `.bat` die de daadwerkenlijken testen runnen. Let op, sommige scripts verwijzen naar een directorie hoger dan waar deze runt. Daardoor wordt er gebruikt gemaakt van relatieve paden met `..` erin.

