#!/bin/bash
# Server Setup Script

mkdir Setup
cd setup

wget https://raw.githubusercontent.com/deanralph/serverSetup/main/main.py
wget https://raw.githubusercontent.com/deanralph/serverSetup/main/colouredText.py
wget https://raw.githubusercontent.com/deanralph/serverSetup/main/installList.txt

sudo python3 main.py

sudo rm *