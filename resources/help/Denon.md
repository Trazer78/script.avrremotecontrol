# Denon AVR-X2000 / E400

## Command list

### Power
| Command  	            | Parameter         | telnet command   	|                                   |
| ---------------------	| -----------------	| ----------------- | --------------------------------- |
| POWER                 | ON                | PWON   	        |                                   |
|                       | OFF               | PWSTANDBY        	|                                   |
|                       | TOGGLE            |                   | Custom implementation             |
|                       | QUERY             | PW?               |                                   |

### Volume
| Command  	            | Parameter         | telnet command   	|                                   |
| ---------------------	| -----------------	| ----------------- | --------------------------------- |
| VOLUME   	            | UP                | MVUP 	            |                                   |
|                       | DOWN              | MVDOWN            |                                   |
|                       | SET**             | MV**           	| Range between 00 - 98 by ASCII    |
|                       | QUERY             | MV?               |                                   |

### Mute
| Command  	            | Parameter         | telnet command   	|                                   |
| ---------------------	| -----------------	| ----------------- | --------------------------------- |
| MUTE                  | ON                | MUON              |                                   |
|                       | OFF               | MUOFF           	|                                   |
|                       | TOGGLE            |                   | Custom implementation             |
|                       | QUERY             | MU?               |                                   |

### Input
| Command  	            | Parameter         | telnet command   	|                                   |
| ---------------------	| -----------------	| ----------------- | --------------------------------- |
| INPUT                 | CD      	        | SICD 	            |                                   |
|                       | TUNER  	        | SITUNER           |                                   |
|                       | DVD   	        | SIDVD	            |                                   |
|                       | BD       	        | SIBD 	            |                                   |
|                       | TV       	        | SITV 	            |                                   |
|                       | SATCBL 	        | SISAT/CBL         |                                   |
|                       | MEDIAPLAYER       | SIMPLAY  	        |                                   |
|                       | GAME   	        | SIGAME   	        |                                   |
|                       | AUX   	        | SIAUX1   	        |                                   |
|                       | NETWORK	        | SINET	            |                                   |
|                       | PANDORA	        | SIPANDORA         |                                   |
|                       | SIRIUSXM          | SISIRIUSXM        |                                   |
|                       | SPOTIFY	        | SISPOTIFY         |                                   |
|                       | FAVORITES         | SIFAVORITES       |                                   |
|                       | IRADIO            | SIIRADIO          |                                   |
|                       | SERVER 	        | SISERVER 	        |                                   |
|                       | IPODUSB	        | SIIPOD/USB        |                                   |
|                       | QUERY 	        | SI? 	            |                                   |

### Video Resolution
| Command  	            | Parameter         | telnet command   	|                                   |
| ---------------------	| -----------------	| ----------------- | --------------------------------- |
|  VIDEO_SCALING_HDMI   | 480p              | VSSCH48P          |                                   |
|                       | 1080i             | VSSCH10I          |                                   |
|                       | 720p              | VSSCH72P          |                                   |
|                       | 1080p             | VSSCH10P          |                                   |
|                       | 10p24             | VSSCH10P24        |                                   |
|                       | 4K                | VSSCH4K           |                                   |
|                       | AUTO              | VSSCHAUTO         |                                   |
