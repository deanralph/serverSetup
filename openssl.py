import os

os.system('mkdir /home/dean/ssl')

varFQDN = input("Please enter FQND: ")
varIP = input("Please enter IP address: ")
varFilename = input("Please enter filename: ")

varConfigText = f"""[req]
distinguished_name = req_distinguished_name
req_extensions = req_ext
prompt = no

[req_distinguished_name]
C   = GB
ST  = Yorkshire
L   = Bradford
O   = DeanRalphNet
OU  = Systems
CN  = {varFQDN}

[req_ext]
subjectAltName = @alt_names

[alt_names]
IP.1 = {varIP}
DNS.1 = {varFQDN}
DNS.2 = {varIP}"""

with open('san.cnf', 'w') as f:
    f.write(varConfigText)

os.system(f"openssl req -out {varFilename}.csr -newkey rsa:2048 -nodes -keyout {varFilename}.key -config san.cnf")