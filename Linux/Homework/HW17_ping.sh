#!/bin/bash
#set -e

read -p "Enter IP or domain to ping: "  ADRESS
#ADRESS=192.0.2.1	#for test ERR

#fail_counter
COUNT=0

while true; 
do

	#Ping (c,count=1), W=1 sec (timeout)
	OUTPUT=$(ping -c 1 -W 1 "$ADRESS" 2>/dev/null)

	if ! echo "$OUTPUT" | grep "time=" > /dev/null; then
		((COUNT++))
		echo "Failed to get response ($COUNT times in a row)"
	else
		COUNT=0

		#read time of response
		TIME=$(echo "$OUTPUT" | grep "time=" | sed -E 's/.*time=([0-9.]+) ms/\1/')
		echo "time of response = ${TIME} ms"

		#check ms (compare two integers, "-gt" greater than)
		#if [ "$TIME" -gt 0.1 ]; then
		#	echo "Warning: time of ping > 100 msec!"
		
		#for float: bc ->1(true) if TIME > 100
		if  (( $(echo "$TIME > 0.4" | bc -l) )); then
			echo "Warning: time of ping > 100 msec"
		
		fi
	fi

	#check 3 pings ("-ge" greater than or equal)
	if [ "$COUNT" -ge 3 ]; then
		echo "Three consecutive pings faild. Stop checking!"
		break
	fi

	sleep 1
done

echo "script done"

