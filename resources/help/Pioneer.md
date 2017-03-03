# Pioneer (2013)

Compatible with following AVR's
- Pioneer VSX-923

## Command list

### Power
| Command  	            | Parameter         | telnet command   	|                                   |
| ---------------------	| -----------------	| ----------------- | --------------------------------- |
| POWER                 | ON   	            | PO   	            |
|                       | OFF  	            | PF               	|
|                       | TOGGLE  	        | PZ              	|
|                       | QUERY             | ?P                |

### Volume
| Command  	            | Parameter         | telnet command   	|                                   |
| ---------------------	| -----------------	| ----------------- | --------------------------------- |
| VOLUME                | UP   	            | VU   	            |                                   |
|                       | DOWN  	        | VD               	|                                   |
|                       | SET***  	        | ***VL           	| Range between 000 - 185 by ASCII  |
|                       | QUERY             | ?V                |                                   |

### Mute
| Command  	            | Parameter         | telnet command   	|                                   |
| ---------------------	| -----------------	| ----------------- | --------------------------------- |
| MUTE                  | ON   	            | MO   	            |
|                       | OFF  	            | MF               	|
|                       | TOGGLE  	        | MZ              	|
|                       | QUERY             | ?M                |

### Input
| Command  	            | Parameter         | telnet command   	|                                   |
| ---------------------	| -----------------	| ----------------- | --------------------------------- |
| INPUT                 | CD   	            | 01FN 	            |                                   |
|                       | TUNER  	        | 02FN 	            |                                   |
|                       | DVD   	        | 04FN 	            |                                   |
|                       | BD   	            | 25FN 	            |                                   |
|                       | TV   	            | 05FN 	            |                                   |
|                       | SATCBL 	        | 06FN 	            |                                   |
|                       | AUX   	        | 10FN   	        | VIDEO 1 (VIDEO)                   |
|                       | NETWORK	        | 26FN 	            |                                   |
|                       | PANDORA	        | 41FN 	            |                                   |
|                       | SIRIUSXM          | 40FN 	            |                                   |
|                       | FAVORITES         | 45FN 	            |                                   |
|                       | IRADIO            | 38FN 	            |                                   |
|                       | SERVER 	        | 44FN 	            |                                   |
|                       | IPODUSB	        | 17FN 	            |                                   |
|                       | PHONO 	        | 00FN 	            |                                   |
|                       | USBDAC 	        | 13FN 	            |                                   |
|                       | HDMI1 	        | 19FN 	            |                                   |
|                       | HDMI2 	        | 20FN 	            |                                   |
|                       | HDMI3 	        | 21FN 	            |                                   |
|                       | HDMI4 	        | 22FN 	            |                                   |
|                       | HDMI5 	        | 23FN 	            |                                   |
|                       | HDMI6 	        | 24FN 	            |                                   |
|                       | HDMI7 	        | 34FN 	            |                                   |
|                       | HDMITOGGLE        | 31FN 	            |                                   |
|                       | MHL 	            | 48FN 	            |                                   |
|                       | DVRBDR 	        | 15FN 	            |                                   |
|                       | ADAPTER	        | 33FN 	            |                                   |
|                       | MULTICHANNEL      | 12FN 	            |                                   |
|                       | TOGGLEUP          | FU 	            |                                   |
|                       | TOGGLEDOWN        | FD 	            |                                   |
|                       | QUERY 	        | ?F 	            |                                   |