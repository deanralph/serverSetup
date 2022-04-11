# Coloured Text Generator
# Dean Ralph
# 2022

HEADER = '\033[95m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def printHeader(textString):
    print(HEADER + textString + ENDC)

def printWarning(textString):
    print(WARNING + textString + ENDC)

def printFail(textString):
    print(FAIL + textString + ENDC)

def printOKGreen(textString):
    print(OKGREEN + textString + ENDC)