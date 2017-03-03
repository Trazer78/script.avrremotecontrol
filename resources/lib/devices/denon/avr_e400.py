#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    avr_e400.py --> Denon AVR-E400 implementation
'''
import ast
import os
import json
from resources.lib.utils import log_msg, telnet_execute, load_json

class DenonAVRE400(object):
    ''' Denon AVR-E400 implementation '''

    def __init__(self):
        self.logprefix = '('+self.__class__.__name__+')'
        log_msg('%s.__init__' % self.logprefix)

        # Available telnet commands list
        self.deviceinfo = self.get_deviceinfo()

        log_msg('%s.__init__ loaded device info for %s %s' % \
            (self.logprefix, self.deviceinfo["make"], self.deviceinfo["model"]))

    def run_command(self, command, parameter, response=False):
        ''' Find function based on the command passed '''
        log_msg('%s.run_command, group: %s parameter %s' % (self.logprefix, command, parameter))

        # Check if the specified command has a custom implementation.
        checkdef = "%s_%s" % (command, parameter)
        if hasattr(self, checkdef.lower()):
            if command.lower() == "volume":
                if parameter[:3].lower() == "set":
                    volumelevel = parameter[3:]
                    return self.volume_set(volumelevel)
            else:
                return getattr(self, checkdef.lower())()
        else:
            avrcommand = self.find_avrcommand(command, parameter)
            if avrcommand != None:
                return self.execute_avrcommand(avrcommand, response)

            else:
                return "Unrecognized command"

    def find_avrcommand(self, command, parameter):
        ''' Find the telnet command based on the command and parameter '''
        log_msg('%s.find_avrcommand, command: %s, parameter: %s ' \
            % (self.logprefix, command, parameter))

        try:
            avrcommand = (self.deviceinfo["commands"][command.upper()][parameter]) \
                .strip().encode("ascii", "ignore")
        except KeyError:
            return None

        return avrcommand

    def execute_avrcommand(self, avrcommand, response=False):
        ''' Execute command against telnet '''
        log_msg('%s.execute_avrcommand %s' % (self.logprefix, avrcommand))

        return telnet_execute(avrcommand, response).strip()

    # POWER
    def power_toggle(self):
        ''' Custom POWER_TOGGLE '''
        log_msg('%s.power_toggle' % self.logprefix)

        poweron = self.find_avrcommand("POWER", "ON")
        poweroff = self.find_avrcommand("POWER", "OFF")
        powerquery = self.find_avrcommand("POWER", "QUERY")

        status = self.execute_avrcommand(powerquery, True)
        if status == poweron:
            return self.execute_avrcommand(poweroff)
        elif status == poweroff:
            return self.execute_avrcommand(poweron)

    # VOLUME
    def volume_up(self):
        ''' Custom VOLUME|UP '''
        log_msg('%s.volume_up' % self.logprefix)

        volumequery = self.find_avrcommand("VOLUME", "QUERY")
        volumelevel = self.get_volumelevel(self.execute_avrcommand(volumequery, True))
        if float(volumelevel/10) <= 80:
            return self.execute_avrcommand(self.find_avrcommand("VOLUME", "UP"))

    def volume_down(self):
        ''' Custom VOLUME|DOWN '''
        log_msg('%s.volume_down' % self.logprefix)

        volumequery = self.find_avrcommand("VOLUME", "QUERY")
        volumelevel = self.get_volumelevel(self.execute_avrcommand(volumequery, True))
        if int(volumelevel) > 0:
            return self.execute_avrcommand(self.find_avrcommand("VOLUME", "DOWN"))

    def volume_set(self, volumelevel):
        ''' Custom VOLUME|SET** '''
        log_msg('%s.volume_set, volumelevel: %s' % (self.logprefix, volumelevel))

        volumequery = self.find_avrcommand("VOLUME", "QUERY")
        if self.validate_volume(volumelevel) and \
            self.execute_avrcommand(volumequery, True) != volumelevel:
            return self.execute_avrcommand('MV'+volumelevel)

    def get_volumelevel(self, value):
        ''' Get current volumelevel from AVR response '''

        # Example response: MV315 MVMAX80
        values = value.split(' ')
        return values[0][2:]

    def validate_volume(self, volumelevel):
        ''' Validate volumelevel '''
        log_msg('%s.validate_volume, volumelevel: %s' % (self.logprefix, volumelevel))

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
        log_msg('%s.mute_toggle' % self.logprefix)

        muteon = self.find_avrcommand("MUTE", "ON")
        muteoff = self.find_avrcommand("MUTE", "OFF")
        mutequery = self.find_avrcommand("MUTE", "QUERY")

        status = self.execute_avrcommand(mutequery)
        if status == muteon:
            return self.execute_avrcommand(muteoff)
        elif status == muteoff:
            return self.execute_avrcommand(muteon)

    #INPUT
    def input_query(self):
        ''' Custom: INPUT|QUERY '''
        log_msg('%s.input_query' % self.logprefix)

        avrcommand = self.find_avrcommand("INPUT", "QUERY")
        currentinput = self.execute_avrcommand(avrcommand, True)
        if currentinput != '':
            inputcmd = currentinput.split(' ').strip()
            log_msg('%s.input_query, currentinput: %s' % (self.logprefix, inputcmd))
            return inputcmd
        else:
            return ''

    # Generic function(s)
    def get_deviceinfo(self):
        ''' Return a list of simple commands'''
        log_msg('%s.get_commandlist' % self.logprefix)

        infofile = os.path.join('resources', 'lib', 'devices', 'denon', 'avr_e400.json')

        return load_json(infofile)

