# Pioneer (2013)

Compatible with following AVR's
- Pioneer VSX-923

## Command list

### Power
| Script command  	    | telnet command   	|                                   |
| ---------------------	| -----------------	| --------------------------------- |
| POWER_ON   	        | PO   	            |
| POWER_OFF  	        | PF               	|
| POWER_TOGGLE  	    | PZ              	|
| POWER_QUERY           | ?P                |

### Volume
| Script command  	    | telnet command   	|                                   |
| ---------------------	| -----------------	| --------------------------------- |
| VOLUME_UP   	        | VU   	            |                                   |
| VOLUME_DOWN  	        | VD               	|                                   |
| VOLUME_SET  	        | ***VL           	| Range between 000 - 185 by ASCII  |
| VOLUME_QUERY          | ?V                |                                   |

### Mute
| Script command  	    | telnet command   	|                                   |
| ---------------------	| -----------------	| --------------------------------- |
| MUTE_ON   	        | MO   	            |
| MUTE_OFF  	        | MF               	|
| MUTE_TOGGLE  	        | MZ              	|
| MUTE_QUERY            | ?M                |

### Input
| Script command  	    | telnet command   	|                                   |
| ---------------------	| -----------------	| --------------------------------- |
| INPUT_CD   	        | 01FN 	            |                                   |
| INPUT_TUNER  	        | 02FN 	            |                                   |
| INPUT_DVD   	        | 04FN 	            |                                   |
| INPUT_BD   	        | 25FN 	            |                                   |
| INPUT_TV   	        | 05FN 	            |                                   |
| INPUT_SATCBL 	        | 06FN 	            |                                   |
| INPUT_AUX   	        | 10FN   	        | VIDEO 1 (VIDEO)                   |
| INPUT_NETWORK	        | 26FN 	            |                                   |
| INPUT_PANDORA	        | 41FN 	            |                                   |
| INPUT_SIRIUSXM        | 40FN 	            |                                   |
| INPUT_SPOTIFY	        | ? 	            |                                   |
| INPUT_FAVORITES       | 45FN 	            |                                   |
| INPUT_INTERNETRADIO   | 38FN 	            |                                   |
| INPUT_SERVER 	        | 44FN 	            |                                   |
| INPUT_IPODUSB	        | 17FN 	            |                                   |
| INPUT_PHONO 	        | 00FN 	            |                                   |
| INPUT_USBDAC 	        | 13FN 	            |                                   |
| INPUT_HDMI1 	        | 19FN 	            |                                   |
| INPUT_HDMI2 	        | 20FN 	            |                                   |
| INPUT_HDMI3 	        | 21FN 	            |                                   |
| INPUT_HDMI4 	        | 22FN 	            |                                   |
| INPUT_HDMI5 	        | 23FN 	            |                                   |
| INPUT_HDMI6 	        | 24FN 	            |                                   |
| INPUT_HDMI7 	        | 34FN 	            |                                   |
| INPUT_HDMI_TOGGLE     | 31FN 	            |                                   |
| INPUT_MHL 	        | 48FN 	            |                                   |
| INPUT_DVRBDR 	        | 15FN 	            |                                   |
| INPUT_ADAPTER	        | 33FN 	            |                                   |
| INPUT_MULTICHANNEL    | 12FN 	            |                                   |
| INPUT_TOGGLE_UP       | FU 	            |                                   |
| INPUT_TOGGLE_DOWN     | FD 	            |                                   |
| INPUT_QUERY 	        | ?F 	            |                                   |