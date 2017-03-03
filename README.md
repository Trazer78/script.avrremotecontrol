# AVR Remote Control add-on [![License](https://img.shields.io/badge/License-GPL%20v3%2B-blue.svg)](https://github.com/trazer78/script.avrremotecontrol/blob/master/LICENSE.txt)

My first try at a Kodi addon to control an AVR via telnet.

For your information (a word of caution):
As i'm just getting started with Python development I currently look to other
addons for inspiration and information. As my Python experience grows it may lead to
new insights.

Breaking change for v0.0.3
* Commands are separated into command and parameter
  - Example: POWER_ON -> POWER|ON
  Check the readme for the supported devices for all commands

## Supported devices
- [Denon AVR-X2000](/resources/help/Denon.md)
- [Denon AVR-E400](/resources/help/Denon.md)
- [Pioneer VSX-923](/resources/help/Pioneer.md)

## Module/Script Example commands

### Power
```
RunScript(script.avrremote,command=POWER|ON)
```
```
RunScript(script.avrremote,command=POWER|OFF)
```
```
RunScript(script.avrremote,command=POWER|TOGGLE)
```
```
RunScript(script.avrremote,command=POWER|QUERY)
```
### Volume
```
RunScript(script.avrremote,command=VOLUME|UP)
```
```
RunScript(script.avrremote,command=VOLUME|DOWN)
```
```
RunScript(script.avrremote,command=VOLUME|SET***,command=VOLUME_QUERY)
```
```
RunScript(script.avrremote,command=VOLUME|QUERY)
```
### Mute
```
RunScript(script.avrremote,command=MUTE|ON)
```
```
RunScript(script.avrremote,command=MUTE|OFF)
```
```
RunScript(script.avrremote,command=MUTE|TOGGLE)
```
```
RunScript(script.avrremote,command=MUTE|QUERY)
```
### Input(s)
```
RunScript(script.avrremote,command=INPUT|CD)
```
```
RunScript(script.avrremote,command=INPUT|CD,command=INPUT|DVD)
```

## Service example commands
```
Setting: [command]|[parameter];[command]|[parameter]
```
```
Setting: [command]|[parameter];[command]
```