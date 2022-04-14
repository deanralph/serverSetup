# Server setup scripe v2 - Electric Boogaloo
# Dean Ralph
# 2022
#
# Imports

import os
from colouredText import *
import subprocess
import telnetlib
import socket
import getpass

# Global Varables

# Functions

def checkRoot():
    return os.geteuid() == 0


def installJava():
    installJDK = input("Do you need java on this box? y/n: ")
    if installJDK == "y":
        os.system('apt install default-jdk -y')


def SetSUDONoPassword():

    varPresent = False
    print("Checking if user has SUDO no password permissions")

    with open("/etc/sudoers", 'r') as f:
        lines = f.read()
        if "dean ALL=(ALL) " in lines:
            varPresent = True

    if varPresent:
        printOKGreen("User aleady has permissions")
    else:
        printWarning("Adding user to sudoers")
        with open("/etc/sudoers", 'a') as f:
            f.write("\n")
            f.write("dean ALL=(ALL) NOPASSWD: ALL")
        with open("/etc/sudoers", 'r') as f:
            lines = f.read()
            if "dean ALL=(ALL) " in lines:
                printOKGreen("User Added Successfully")
            else:
                printFail("Failed to add user. Exiting script...")
                exit


def installSoftware():

    installString = "apt install"
    with open('installList.txt', 'r') as f:
        softlines = f.readlines()
        for x in softlines:
            if '#' not in x:
                installString += f" {x[:-1]}"
    installString += f" -y" 
    os.system(installString)


def DraytekCLI(octet):
    macAddr = ""
    trimmedHostname = socket.gethostname()[0:12]
    os.system('cat /sys/class/net/en*/address >> mac.txt')
    with open("mac.txt", 'r') as f:
        macAddr = f.readline()
    os.remove('mac.txt')
    draytekCLIString = f"ip bindmac add 10.0.0.{octet} {macAddr[:-1]} {trimmedHostname}"

    HOST = "10.0.0.1"
    user = "admin"
    password = getpass.getpass("Please enter router password: ")

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Account:")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(bytes(draytekCLIString, encoding='ascii') + b"\n")
    tn.write(b"exit\n")

    tn.close

    print(tn.read_all().decode('ascii'))


def addPatching(servername, ipaddress):
    os.system("pip3 install pymssql")
    import pymssql
    conn = pymssql.connect("10.0.0.53", "patching", "Patching123", "patching")
    cursor = conn.cursor(as_dict=True)

    cursor.execute(f"EXECUTE [dbo].[addserver] '{servername}', '10.0.0.{ipaddress}', 'dean', 0, 0")
    conn.commit()
    
    validate = cursor.execute(f"select * from [dbo].[servers] where servername = '{servername}'")

    if validate[servername] == servername:
        printOKGreen("Successfully added to patching db")
    else:
        printFail("Failed to add to patching db")


# Main code base

if __name__ == "__main__":
    os.system('clear')
    printHeader("Server Setup Script v2 - Python Edition")
    if not checkRoot():
        printFail("User is not root - Exiting Script")
        exit()
    print()
    SetSUDONoPassword()
    print()
    print("Runnin apt update")
    os.system('sudo apt update && sudo apt upgrade -y && sudo apt autoremove && sudo apt autoclean -y')
    installJava()
    print()
    printHeader("Installing software")
    installSoftware()
    print()
    printHeader("Setting up IP to mac-address bind")
    varIP = input("Please the 4th octet (10.0.0.***) you and for the IP of this server: ")
    print()
    DraytekCLI(varIP) 
    varPatching = input("do you want to add server to patching? y/n: ")
    if varPatching == 'y':
        addPatching(srt(socket.gethostname()), varIP)