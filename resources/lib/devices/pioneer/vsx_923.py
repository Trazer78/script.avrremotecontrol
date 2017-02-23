#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    vsx_923.py --> Pioneer VSX-923 implementation
'''
import ast
import os
from resources.lib.utils import log_msg, telnet_execute, get_addon_path

class PioneerVSX923(object):
    ''' Pioneer VSX-923 implementation '''

    # Volume range settings
    VOLUME_MIN = 000
    VOLUME_MAX = 185

    def __init__(self):
        self.logprefix = '('+self.__class__.__name__+')'
        log_msg(self.logprefix+'.__init__')

        # Available telnet commands list
        self.commandlist = self.get_commandlist()

    def parse_command(self, command, parameter=None):
        ''' Find function based on the command passed '''
        if parameter is None:
            log_msg(self.logprefix+'.parse_command, command: '+command)
        else:
            log_msg(self.logprefix+'.parse_command, command: '+command+' param: '+parameter)

        # Check if the specified command has a custom implementation.
        if hasattr(self, command.lower()):
            if command == 'VOLUME_SET':
                return self.volume_set(parameter)
            else:
                return getattr(self, command.lower())()
        else:
            avrcommand = self.find_command(command)
            if avrcommand != None:
                return self.execute_command(avrcommand)

            else:
                return "Unrecognized command"

    def find_command(self, command):
        ''' Find the telnet command based on the generic command '''
        log_msg(self.logprefix+'.find_command, command: '+command)

        return self.commandlist.get(command, None)

    def execute_command(self, avrcommand, withresponse=False):
        ''' Execute command against telnet '''
        log_msg(self.logprefix+'.execute_command, command: '+avrcommand)

        return telnet_execute(avrcommand, withresponse)

    # VOLUME
    def volume_up(self):
        ''' Custom: VOLUME_UP '''
        log_msg(self.logprefix+'.volume_up')

        avrcommand = self.find_command("VOLUME_QUERY")
        if int(self.execute_command(avrcommand, True)[3:]) < self.VOLUME_MAX:
            return self.execute_command(self.find_command("VOLUME_UP"))


    def volume_down(self):
        ''' Custom: VOLUME_DOWN '''
        log_msg(self.logprefix+'.volume_down')

        avrcommand = self.find_command("VOLUME_QUERY")
        if int(self.execute_command(avrcommand, True)[3:]) > self.VOLUME_MIN:
            return self.execute_command(self.find_command("VOLUME_DOWN"))


    def volume_set(self, volumelevel):
        ''' Custom: VOLUME_SET '''
        log_msg(self.logprefix+'.volume_set, volumelevel: '+volumelevel)

        if int(volumelevel) >= self.VOLUME_MIN and int(volumelevel) <= self.VOLUME_MAX:
            return self.execute_command('VL'+volumelevel)
        else:
            pass

    def get_commandlist(self):
        ''' Return a list of simple commands'''
        log_msg(self.logprefix+'.get_commandlist')

        # # Load commands list
        # commandfile = os.path.join(get_addon_path(), 'resources/lib/devices/pioneer/2013.codes')
        # log_message(self.logprefix+'.get_commandlist, commandfile: '+commandfile)

        # with open(commandfile, 'r') as codefile:
        #     self.commandlist = ast.literal_eval(codefile.read())

        return {
            "POWER_ON": "PO", "POWER_OFF": "PF", "POWER_TOGGLE": "PZ", "POWER_QUERY": "?P",
            "VOLUME_UP": "VU", "VOLUME_DOWN": "VD", "VOLUME_SET": "VL***", "VOLUME_QUERY": "?V",
            "MUTE_ON": "MO", "MUTE_OFF": "MF", "MUTE_TOGGLE": "MZ", "MUTE_QUERY": "?M",
            "INPUT_CD": "01FN",
            "INPUT_TUNER" : "02FN",
            "INPUT_DVD": "04FN", "INPUT_BD": "25FN",
            "INPUT_TV": "05FN",
            "INPUT_SATCBL": "06FN",
            "INPUT_AUX": "10FN",
            "INPUT_NETWORK": "26FN",
            "INPUT_PANDORA": "41FN", "INPUT_SIRIUSXM": "40FN",
            "INPUT_FAVORITES": "45FN",
            "INPUT_INTERNETRADIO": "38FN",
            "INPUT_SERVER": "44FN",
            "INPUT_IPODUSB": "17FN",
            "INPUT_PHONO": "00FN",
            "INPUT_USBDAC": "13FN",
            "INPUT_HDMI1": "19FN", "INPUT_HDMI2": "20FN", "INPUT_HDMI3": "21FN",
            "INPUT_HDMI4": "22FN", "INPUT_HDMI5": "23FN", "INPUT_HDMI6": "24FN",
            "INPUT_HDMI7": "34FN", "INPUT_HDMI_TOGGLE": "31FN", "INPUT_HDMI_MHL": "48FN",
            "INPUT_DVRBDR": "15FN",
            "INPUT_ADAPTER": "33FN", "INPUT_MULTICHANNEL": "12FN",
            "INPUT_TOGGLE_UP": "FU", "INPUT_TOGGLE_DOWN": "FD",
            "INPUT_QUERY": "?F"
        }
