#! /bin/bash

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
#                                                                             #     
# This script configures which GPIO pins of the Raspberry Pi will be          #
# available and in which direction (read or write). It also takes some        #
# actions if someone interacts with the selected pins.                        #
#                                                                             #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


if [[ $EUID -ne 0 ]]; then
   echo "Error: This script must be run as root" >&2
   exit 1
fi

SHUTDOWN_PIN="5"

echo "$SHUTDOWN_PIN" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio"$SHUTDOWN_PIN"/direction

while ( true )
do
    # check if the pin is connected to GND and, if so, halt the system
    if [ $(</sys/class/gpio/gpio"$SHUTDOWN_PIN"/value) == 0 ]
    then
        echo "$SHUTDOWN_PIN" > /sys/class/gpio/unexport
        shutdown -h now "System halted by a GPIO action"
    fi
    
    sleep 60
done

