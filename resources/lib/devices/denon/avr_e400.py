#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    avr_e400.py --> Denon AVR-E400 implementation
'''
import ast
import os
from resources.lib.utils import log_msg, telnet_execute, get_addon_path

class DenonAVRE400(object):
    ''' Denon AVR-E400 implementation '''

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

    # POWER
    def power_toggle(self):
        ''' Custom POWER_TOGGLE '''
        log_msg(self.logprefix+'.power_toggle')

        poweron = self.find_command("POWER_ON")
        poweroff = self.find_command("POWER_OFF")
        powerquery = self.find_command("POWER_QUERY")

        status = self.execute_command(powerquery, True)
        if status == poweron:
            return self.execute_command(poweroff)
        elif status == poweroff:
            return self.execute_command(poweron)

    # VOLUME
    def volume_up(self):
        ''' Custom VOLUME_UP '''
        log_msg(self.logprefix+'.volume_up')

        volumequery = self.find_command("VOLUME_QUERY")
        volumelevel = self.get_volumelevel(self.execute_command(volumequery, True))
        if float(volumelevel/10) <= 80:
            return self.execute_command(self.find_command("VOLUME_UP"))

    def volume_down(self):
        ''' Custom VOLUME_DOWN '''
        log_msg(self.logprefix+'.volume_down')

        volumequery = self.find_command("VOLUME_QUERY")
        volumelevel = self.get_volumelevel(self.execute_command(volumequery, True))
        if int(volumelevel) > 0:
            return self.execute_command(self.find_command("VOLUME_DOWN"))

    def volume_set(self, volumelevel):
        ''' Custom VOLUME_SET '''
        log_msg(self.logprefix+'.volume_set, volumelevel: '+volumelevel)

        volumequery = self.find_command("VOLUME_QUERY")
        if self.validate_volume(volumelevel) and \
            self.execute_command(volumequery, True) != volumelevel:
            return self.execute_command('MV'+volumelevel)

    def get_volumelevel(self, value):
        ''' Get current volumelevel from AVR response '''

        # Example response: MV315 MVMAX80
        values = value.split(' ')
        return values[0][2:]

    def validate_volume(self, volumelevel):
        ''' Validate volumelevel '''
        log_msg(self.logprefix+'.validate_volume, volumelevel: '+volumelevel)

        if int(volumelevel[:2]) >= 0 and int(volumelevel[:2] <= 98):
            if volumelevel.len() == 2:
                return True
            elif volumelevel.len() == 3 and volumelevel[2:] == '5':
                return True
            else:
                return False
        else:
            return False

    # MUTE
    def mute_toggle(self):
        ''' Custom MUTE_TOGGLE '''
        log_msg(self.logprefix+'.mute_toggle')

        muteon = self.find_command("MUTE_ON")
        muteoff = self.find_command("MUTE_OFF")
        mutequery = self.find_command("MUTE_QUERY")

        status = self.execute_command(mutequery)
        if status == muteon:
            return self.execute_command(muteoff)
        elif status == muteoff:
            return self.execute_command(muteon)

    def get_commandlist(self):
        ''' Return a list of simple commands'''
        log_msg(self.logprefix+'.get_commandlist')

        # Load commands list
        # commandfile = os.path.join(get_addon_path(), 'resources/lib/devices/denon/avr_e400.codes')
        # with open(commandfile, 'r') as codefile:
        #     self.commandlist = ast.literal_eval(codefile.read())

        return {
            # Power
            "POWER_ON": "PWON", "POWER_OFF": "PWSTANDBY", "POWER_QUERY": "PW?",
            # Volume
            "VOLUME_UP": "MVUP", "VOLUME_DOWN": "MVDOWN",
            "VOLUME_SET": "VL***", "VOLUME_QUERY": "MV?",
            # Mute
            "MUTE_ON": "MUON", "MUTE_OFF": "MUOFF", "MUTE_QUERY": "MU?",
            # Inputs
            "INPUT_CD": "SICD", "INPUT_DVD": "SIDVD", "INPUT_BD": "SIBD",
            "INPUT_TUNER" : "SITUNER", "INPUT_TV": "SITV",
            "INPUT_SATCBL": "SISAT/CBL",
            "INPUT_MEDIAPLAYER": "SIMPLAY",
            "INPUT_AUX": "SIAUX1",
            "INPUT_NETWORK": "SINET",
            "INPUT_PANDORA": "SIPANDORA",
            "INPUT_SIRIUSXM": "SISIRIUSXM",
            "INPUT_FLICKR": "SIFLICKR",
            "INPUT_SPOTIFY": "SISPOTIFY",
            "INPUT_FAVORITES": "SIFAVORITES",
            "INPUT_INTERNETRADIO": "SIIRADIO",
            "INPUT_SERVER": "SISERVER",
            "INPUT_IPODUSB": "SIIPOD/USB",
            "INPUT_QUERY": "SI?",
            "VIDEO_RES_HDMI_AUTO": "VSSCHAUTO"
        }
