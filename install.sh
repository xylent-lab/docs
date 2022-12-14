#!/bin/bash

apt install screen -y

wget https://github.com/nullmc/docs/raw/main/OVH-PPS
curl https://raw.githubusercontent.com/nullmc/docs/main/HEX.py -o HEX.py
wget https://github.com/nullmc/docs/raw/main/STD
wget https://github.com/nullmc/docs/raw/main/TCP-ACK
curl https://raw.githubusercontent.com/nullmc/docs/main/UDP-OVH.py -o UDP-OVH.py
curl https://raw.githubusercontent.com/nullmc/docs/main/UDP.pl -o UDP.pl

chmod +x OVH-PPS
chmod +x HEX.py
chmod +x STD
chmod +x TCP-ACK
chmod +x UDP-OVH.py
chmod +x UDP.pl

echo "Finish."
