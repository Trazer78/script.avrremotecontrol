# AVR Remote Control add-on [![License](https://img.shields.io/badge/License-GPL%20v3%2B-blue.svg)](https://github.com/trazer78/script.avrremotecontrol/blob/master/LICENSE.txt)

A (currently) rough working add-on for controlling an AVR from Kodi.

## Supported devices
- [Denon AVR-X2000](/resources/help/Denon.md)
- [Denon AVR-E400](/resources/help/Denon.md)
- [Pioneer VSX-923](/resources/help/Pioneer.md)

## Module/Script Example commands

### Power
```
RunScript(script.avrremote,command=POWER_ON)
```
```
RunScript(script.avrremote,command=POWER_OFF)
```
```
RunScript(script.avrremote,command=POWER_TOGGLE)
```
```
RunScript(script.avrremote,command=POWER_QUERY)
```
### Volume
```
RunScript(script.avrremote,command=VOLUME_UP)
```
```
RunScript(script.avrremote,command=VOLUME_DOWN)
```
```
RunScript(script.avrremote,command=VOLUME_SET|***,command=VOLUME_QUERY)
```
```
RunScript(script.avrremote,command=VOLUME_QUERY)
```
### Mute
```
RunScript(script.avrremote,command=MUTE_ON)
```
```
RunScript(script.avrremote,command=MUTE_OFF)
```
```
RunScript(script.avrremote,command=MUTE_TOGGLE)
```
```
RunScript(script.avrremote,command=MUTE_QUERY)
```
### Input(s)
```
RunScript(script.avrremote,command=INPUT_CD)
```
```
RunScript(script.avrremote,command=INPUT_CD,command=INPUT_DVD)
```

## Service example commands
```
Setting: [command][|parameter];[command][|parameter]
```
```
Setting: [command];[command][|parameter]
```
```
Setting: [command];[command]
```