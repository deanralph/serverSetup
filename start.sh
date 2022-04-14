#!/bin/bash
# Server Setup Script

mkdir setup
cd setup

wget https://raw.githubusercontent.com/deanralph/serverSetup/main/main.py
wget https://raw.githubusercontent.com/deanralph/serverSetup/main/colouredText.py
wget https://raw.githubusercontent.com/deanralph/serverSetup/main/installList.txt

sudo python3 main.py

cd ../

sudo rm -r setup

clear