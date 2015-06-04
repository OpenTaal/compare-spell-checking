set -xe
unzip -u OpenTaal-210G-woordenlijsten.zip
./prepare.py OpenTaal-210G-basis-gekeurd.txt opentaal210g_gekeurd.txt
./prepare.py OpenTaal-210G-flexievormen.txt opentaal210g_flexies.txt
./prepare.py OpenTaal-210G-basis-ongekeurd.txt opentaal210g_ongekeurd.txt
./prepare.py OpenTaal-210G-verwarrend.txt opentaal210g_verwarrend.txt
