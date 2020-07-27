#!/bin/sh -e
#
# 
#

BASE_GPIO_PATH=/sys/class/gpio

if [ ! -e $BASE_GPIO_PATH/gpio26 ]; then
	echo "26" > $BASE_GPIO_PATH/export
fi
echo "out" > $BASE_GPIO_PATH/gpio26/direction
printf "LAN Reset! %s\n"
echo "0" > $BASE_GPIO_PATH/gpio26/value
sleep 1
echo "1" > $BASE_GPIO_PATH/gpio26/value
printf "LAN Restarted! %s\n"


exit 0



