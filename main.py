# Server setup scripe v2 - Electric Boogaloo
# Dean Ralph
# 2022
#
# Imports

import os
from colouredText import *
import time
import subprocess
import re

# Global Varables

# Functions

def checkRoot():
    # return os.geteuid() == 0
    return True

def javaCheck():
    version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
    if "Oracle" in str(version):
        printOKGreen("Java Installed")
        return False
    else:
        printWarning("No Java install detected")
        return True

def installJava():
    print("""Please select one of the following Java versions to install:
    
    1: Oracle v8
    2: Oracle v11
    3: Open Java v8
    4: Open Java v11
    5: None
    
Please enter choice 1-5 - """)

def installOpenSSH():
    print("Installing OpenSSH Server")
    printOKGreen("Install Successful")

def SetSUDONoPassword():
    varPresent = False
    print("Check if user has Sudo no password permissions")
    with open("test.txt", 'r') as f:
        lines = f.read()
        if "test" in lines:
            varPresent = True
    if varPresent:
        printOKGreen("User aleady has permissions")
    else:
        printWarning("Adding user to sudoers")
        with open("test.txt", 'a') as f:
            f.write("\n")
            f.write("test")

# Main code base

if __name__ == "__main__":
    os.system('cls')
    printHeader("Server Setup Script v2 - Python Edition")
    if not checkRoot():
        printFail("User is not root - Exiting Script")
        exit()
    print()
    if javaCheck():
        installJava()
    print()
    installOpenSSH()
    print()
    SetSUDONoPassword()
    SetSUDONoPassword()