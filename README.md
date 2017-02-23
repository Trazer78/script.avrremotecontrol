# AVRRemote add-on [![License](https://img.shields.io/badge/License-GPL%20v2%2B-blue.svg)](https://github.com/trazer78/script.avrremote/blob/master/LICENSE.txt)

## Supported devices
- [Denon AVR X2000](/resources/help/Denon.md)
- [Denon E400](/resources/help/Denon.md)
- [Pioneer VSX-923](/resources/help/Pioneer.md)

## Example commands

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