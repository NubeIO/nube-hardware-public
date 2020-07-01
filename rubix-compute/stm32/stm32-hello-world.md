## Software

Windows:
STM32 ST-LINK utility

- Flashing Firmware to STM32.
- Connect the ST-Link programmer to the SWD of the Rubix Compute.
- Open STM32 ST-Link Utility tool and Click “Connect” in order to connect to the STM32 of the Rubix Compute.
- Open a *.bin you wish to program. As sample *.bin file can be downloaded on the link below for you testing. 
[Hello World Bin](https://github.com/NubeIO/nube-hardware-public/blob/master/rubix-compute/stm32/nubeio-stm32-hello-world.zip )


## parts needed

### Generic ST-LINK V2
https://www.ebay.com.au/itm/AU-POST-ST-Link-V2-STLINK-Mini-STM8STM32-STLINK-Simulator-Download-Programming/264333418392?hash=item3d8b7fdf98:g:tCoAAOSwSzJc5eZa&frcectupt=true

### easy flashing software for Windows
https://www.st.com/en/development-tools/stsw-link004.html


###

```
stty -F /dev/ttyAMA0 38400 -cstopb -parenb && cat /dev/ttyAMA0
```

```
Nube iO STM32 Flash Test
Serial Settings: 
    38400, 8, N, 1
Checking components...
Done.
1 second counter running...
0
1
2
3
4
5
...
