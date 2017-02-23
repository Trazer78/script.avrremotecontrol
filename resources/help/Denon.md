# Denon AVR-X2000 / E400

## Command list

### Power
| Script command  	    | telnet command   	|                                   |
| ---------------------	| -----------------	| --------------------------------- |
| POWER_ON   	        | PWON   	        |                                   |
| POWER_OFF  	        | PWSTANDBY        	|                                   |
| POWER_TOGGLE          |                   | Custom implementation             |
| POWER_QUERY           | PW?               |                                   |

### Volume
| Script command  	    | telnet command   	|                                   |
| ---------------------	| -----------------	| --------------------------------- |
| VOLUME_UP   	        | MVUP 	            |                                   |
| VOLUME_DOWN  	        | MVDOWN            |                                   |
| VOLUME_SET  	        | MV**           	| Range between 00 - 98 by ASCII    |
| VOLUME_QUERY          | MV?               |                                   |

### Mute
| Script command  	    | telnet command   	|                                   |
| ---------------------	| -----------------	| --------------------------------- |
| MUTE_ON   	        | MUON              |                                   |
| MUTE_OFF  	        | MUOFF           	|                                   |
| MUTE_TOGGLE           |                   | Custom implementation             |
| MUTE_QUERY            | MU?               |                                   |

### Input
| Script command  	    | telnet command   	|                                   |
| ---------------------	| -----------------	| --------------------------------- |
| INPUT_CD   	        | SICD 	            |                                   |
| INPUT_TUNER  	        | SITUNER           |                                   |
| INPUT_DVD   	        | SIDVD	            |                                   |
| INPUT_BD   	        | SIBD 	            |                                   |
| INPUT_TV   	        | SITV 	            |                                   |
| INPUT_SATCBL 	        | SISAT/CBL         |                                   |
| INPUT_MEDIAPLAYER     | SIMPLAY  	        |                                   |
| INPUT_GAME   	        | SIGAME   	        |                                   |
| INPUT_AUX   	        | SIAUX1   	        |                                   |
| INPUT_NETWORK	        | SINET	            |                                   |
| INPUT_PANDORA	        | SIPANDORA         |                                   |
| INPUT_SIRIUSXM        | SISIRIUSXM        |                                   |
| INPUT_SPOTIFY	        | SISPOTIFY         |                                   |
| INPUT_FAVORITES       | SIFAVORITES       |                                   |
| INPUT_INTERNETRADIO   | SIIRADIO          |                                   |
| INPUT_SERVER 	        | SISERVER 	        |                                   |
| INPUT_IPODUSB	        | SIIPOD/USB        |                                   |
| INPUT_QUERY 	        | SI? 	            |                                   |

### Video Resolution
| Script command  	    | telnet command   	|                                   |
| ---------------------	| -----------------	| --------------------------------- |
|  VIDEO_RES_HDMI_AUTO  | VSSCHAUTO         |                                   |
