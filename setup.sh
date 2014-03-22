#!/bin/sh
#type in terminal ---> bash setup.sh
echo "========================= > Starting Installation < ============================="
sleep 2
sudo apt-get install dialog
dialog --title "BitStream Installation" --yesno 'The following packages will be installed :
Youtube-dl
Ubuntu-restricted-extras( packages such as ffmpeg )
Python
Do you want to continue?' 15 80
if [ $? -eq "0" ]
then
	sudo apt-get install youtube-dl
	sudo apt-get install ubuntu-restricted-extras
	sudo apt-get install python
else
	echo "======================> Exiting "
	sleep 1
fi
chmod 777 run.sh
