#!/bin/bash
# Server Setup Script

clear

echo "###################################################"
echo -e "\033[1;33m                   DEANRALPH.NET"
echo "             SERVER SETUP SCRIPT V1.0"
echo -e "\033[0m###################################################"
echo 
echo 

# Check script is being run as root user
if [ "$EUID" -ne 0 ]
  then echo -e "\033[0;31mPlease run as root"
  exit
fi

#checks if user is sudo no password
echo -e "\033[0mChecking if user is sudo no password..."
if grep -q "dean ALL=(ALL) NOPASSWD: ALL" /etc/sudoers; then
    echo "User already in sudoers"
else
    echo "Setting sudo without password..."
    echo "Taking backup of etc/sudoers"
    cp /etc/sudoers /etc/sudoers.backup
    if test -f "/etc/sudoers.backup"; then
        echo "backup successfull."
    fi
    echo "dean ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
    if grep -q "dean ALL" /etc/sudoers; then
        echo "Added to sudoers successfully"
    else
        echo -e "\033[0;31mFailed to set up are you running as root?"
        exit
    fi
fi

apt update

echo "Is java required on this machine? y/n"

read varJava

if [ $varJava == "y" ]; then
    echo "Installing Java"
    echo 
    echo 
    apt install openjdk-17-jdk openjdk-17-jre
fi

echo 
echo 
echo "Installing requirted apps"
echo 
echo 
apt install qemu-guest-agent openssh-server -y
