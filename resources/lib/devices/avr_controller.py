# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    avr_controller.py --> Generic AVR controller implementation
'''
from resources.lib.devices.denon import avr_x2000, avr_e400
from resources.lib.devices.pioneer import vsx_923
from resources.lib.utils import log_msg

class AVRController(object):
    ''' Generic AVRController class which contains logic based on device type '''

    def __init__(self, device):
        self.logprefix = '('+self.__class__.__name__+')'
        log_msg(self.logprefix+".__init__")

        # Initialize AVR Device
        self.avrdevice = self.get_device(device)

    def parse_command(self, command, parameter=None):
        ''' Call the specified command on the device '''
        if parameter is None:
            log_msg(self.logprefix+".parse_command, command: "+command)
        else:
            log_msg(self.logprefix+".parse_command, command: "+command+" param: "+parameter)

        if self.avrdevice != None:
            return self.avrdevice.parse_command(command, parameter)
        else:
            log_msg(self.logprefix+" Unsupported AVR")
            return "Unsupported AVR"

    def get_device(self, device):
        ''' Get device instance based on the device model '''

        if device == 'Pioneer VSX-923':
            return vsx_923.PioneerVSX923()
        elif device == 'Denon AVR-X2000':
            return avr_x2000.DenonAVRX2000()
        elif device == 'Denon AVR-E400':
            return avr_e400.DenonAVRE400()
        else:
            return None
