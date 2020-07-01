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
