#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    vsx_923.py --> Pioneer VSX-923 implementation
'''
import os
from resources.lib.utils import log_msg, telnet_execute, load_json
import xbmc

class PioneerVSX923(object):
    ''' Pioneer VSX-923 implementation '''

    # Volume range settings
    VOLUME_MIN = 000
    VOLUME_MAX = 185

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

        return telnet_execute(avrcommand, response)

    # VOLUME
    def volume_up(self):
        ''' Custom: VOLUME_UP '''
        log_msg('%s.volume_up' % self.logprefix)

        if self.get_volumelevel() < self.VOLUME_MAX:
            return self.execute_avrcommand(self.find_avrcommand("VOLUME", "UP"))

    def volume_down(self):
        ''' Custom: VOLUME|DOWN '''
        log_msg('%s.volume_down' % self.logprefix)

        if  self.get_volumelevel() > self.VOLUME_MIN:
            return self.execute_avrcommand(self.find_avrcommand("VOLUME", "DOWN"))

    def volume_set(self, volumelevel):
        ''' Custom: VOLUME|SET*** '''
        log_msg('%s.volume_set, volumelevel: %s' % (self.logprefix, volumelevel))

        if int(volumelevel) >= self.VOLUME_MIN and int(volumelevel) <= self.VOLUME_MAX:
            return self.execute_avrcommand('VL'+volumelevel)
        else:
            pass

    def get_volumelevel(self):
        ''' Get current volume level from the AVR '''
        log_msg('%s.get_volumelevel' % self.logprefix)

        avrcommand = self.find_avrcommand("VOLUME", "QUERY")
        level = (self.execute_avrcommand(avrcommand, True)[:3]).strip()

        log_msg('%s.get_volumelevel. Current volume level: %s' % (self.logprefix, level), xbmc.LOGNOTICE)

        return int(level)

    def input_query(self):
        ''' Custom: INPUT|QUERY '''
        log_msg('%s.volume_down' % self.logprefix)

        avrcommand = self.find_avrcommand("INPUT", "QUERY")
        currentinput = self.execute_avrcommand(avrcommand, True)
        if currentinput != '':
            cmd = '%s%s' % (currentinput[2:].strip(), currentinput[:2].strip())
            inputcmd = self.get_input(self.deviceinfo, cmd)
            log_msg('%s.input_query, currentinput: %s' % (self.logprefix, inputcmd))
            return inputcmd
        else:
            return ''

    def get_deviceinfo(self):
        ''' Return a list of simple commands'''
        log_msg('%s.get_commandlist' % self.logprefix)

        infofile = os.path.join('resources', 'lib', 'devices', 'pioneer', 'vsx_923.json')

        return load_json(infofile)

    def get_input(self, jsonobject, inputvalue):
        ''' Returns a list of inputs available '''

        inputs = jsonobject["commands"]["INPUT"]
        for cmd, param in inputs.iteritems():
            if param == inputvalue:
                return cmd

        return ''
