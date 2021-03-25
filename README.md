# aquaPoney


repo pour le code auqaponique
pour l'instant utilise un raspberry pi
un capteur de temperature/humidité bme280 i2c
un relai pour l'activation de la pompe
le code est principalement du python
Fastapi pour le Back
Svelte pour le Front


# Pour lancer
installer docker & docker-compose sur votre machine docker fera le reste
`docker-compose build`
`docker-compose up`
on peu tres bien uitilsé just la partie non server dans le repetoire raspi
copier le fichier
.envexemple en .env
dans le root et dans le repertoire raspi


# postgres database creation
docker exec -it  2f2ab7fb351d psql -U admin postgres
CREATE DATABASE aqua;


# SCreen to keep the process workin

apt-get install screen
then screen
then lauch the script
then
`Ctrl+Shift+A` then `D`

# insall Docker
apt-get install docker.io
pip3 install docker-compose
python3 -m pip install pyserial


# I2C SENSOR

i2cdetect -y 1

arduio via cli
https://www.youtube.com/watch?v=J-qGn1eEidA&t=4s

# ZSH raspif

https://gist.github.com/anthonyray/08f805138c2b37c2554b777ea96513f2


arduino-cli sketch new cli-aqua
arduino-cli compile --fqbn arduino:avr:nano cli-aqua -v
arduino-cli upload -p /dev/ttyUSB0 --fqbn arduino:avr:nano cli-aqua -v