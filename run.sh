#!/bin/bash

port="8331"	
ip="127.0.0.1"
password=1111
stats=1

#trap "rm stats; exit" SIGHUP SIGINT SIGTERM
#dialog --title "BitStream" \
#	--inputbox "Enter Port to start Server" 8 60 2>stats
#port=`cat stats`

#exec 6<>/dev/tcp/127.0.0.1/$port && stats=0

#if [[ $stats -eq "0" ]] 
#then
#	trap "rm stats; exit" SIGHUP SIGINT SIGTERM
#	dialog --title "ERROR:Port already in use" \
#	--msgbox "Try again by giving another port" 8 60 
#	bash run.sh
#else
	dialog --title "======================> Starting Bit_Stream <=========================" \
       --msgbox "Running the server at "$ip":"$port".""
If you want to close the application,please execute the KILL COMMAND DISPLAYED as soon as this dialogbox closes or else the server will fail to start next time." 10 80
	python ./core/web2py.py -p $port -i $ip -a $password & 
	sleep 2
	firefox http://$ip:$port/downloader/download/main
#fi

