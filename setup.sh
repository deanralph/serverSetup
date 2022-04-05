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

echo "Is java required on this machine? y/n"

read varJava

if [ $varJava == "y" ]; then
    echo "Installing Java"
    echo 
    echo 
    apt install default-jre -y
fi

echo "Installing requirted apps"
echo 
echo 
apt update
apt install qemu-guest-agent openssh-server -y

echo 
echo 

echo "Do you want to add the server to the Mac-Address bind table? y/n"

read bindIP

if [ $bindIP == "y" ]; then

    echo
    echo "Please enter the 4th Octlet (10.0.0.***) of the IP address you and to set:"
    read varOctlet
    echo 
    echo "Confirmed IP will be 10.0.0.$varOctlet"
    varMac=$(</sys/class/net/en*/address)
    echo "Mac-Address found: $varMac"
    echo
    draytekCLI="ip bindmac add 10.0.0.$varOctlet $varMac ${HOSTNAME:0:12}"
    echo "Draytek CLI command generated: $draytekCLI"
    echo "please copy and past the above command"

    ssh -t -oKexAlgorithms=+diffie-hellman-group1-sha1 admin@10.0.0.1

fi

echo

echo "Do you want to add the server to the local DNS on pihole? y/n"
read addPihole
echo

echo "Please enter FQDN:"
read fqdn

echo
if [ $addPihole == "y" ]; then
    echo "Connecting to PiHole on 10.0.0.10"
    ssh dean@10.0.0.10 "sudo bash /home/dean/addDNS.sh 10.0.0.$varOctlet $fqdn"
    echo "DNS entry added"
fi
