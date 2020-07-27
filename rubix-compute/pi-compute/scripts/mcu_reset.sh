#!/bin/sh -e
#
# 
#

BASE_GPIO_PATH=/sys/class/gpio

if [ ! -e $BASE_GPIO_PATH/gpio12 ]; then
	echo "12" > $BASE_GPIO_PATH/export
fi
echo "out" > $BASE_GPIO_PATH/gpio12/direction
printf "MCU Reset! %s\n"
echo "0" > $BASE_GPIO_PATH/gpio12/value
sleep 1
echo "1" > $BASE_GPIO_PATH/gpio12/value
printf "MCU Restarted! %s\n"


exit 0



