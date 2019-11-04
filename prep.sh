#! /bin/bash

sudo cp ./services/demo.service /mnt/acab/etc/systemd/system/demo.service
sudo cp ./services/iperf*.service /mnt/acab/etc/systemd/system/
sudo mkdir /mnt/acab/home/pi/Source
sudo mkdir /mnt/acab/home/pi/Source/ident_blink
sudo cp ./src/blink.py /mnt/acab/home/pi/Source/ident_blink/blink.py
sudo chmod +x /mnt/acab/home/pi/Source/ident_blink/blink.py
sudo cp ./src/ident.py /mnt/acab/home/pi/Source/ident_blink/ident.py
sudo chmod +x /mnt/acab/home/pi/Source/ident_blink/ident.py
