#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    arc_module.py --> Script/Module implementation
'''
import sys
import xbmc
import xbmcaddon
from resources.lib.devices.avr_controller import AVRController
from resources.lib.utils import log_msg, ADDON_ID

class ArcModule(object):
    ''' AVR Remote Control module implementation '''

    def __init__(self):
        self.logprefix = '(%s)' % self.__class__.__name__

        addon = xbmcaddon.Addon(ADDON_ID)
        self.addonversion = addon.getAddonInfo('version')
        make = addon.getSetting("make")
        model = addon.getSetting('%s_model' % make.lower())

        log_msg('%s version %s entered' \
            % (self.logprefix, self.addonversion), xbmc.LOGNOTICE)

        # Parse submitted arguments
        self._parse_argv()

        # Instantiate classes
        self.avrcontroller = AVRController(make, model)

        for command in self.commands:
            self.run_command(command)

        # Cleanup
        self.close()

    def _parse_argv(self):
        # structure command[|parameter]
        self.commands = []

        for arg in sys.argv[1:]:
            param = arg.replace('"', '').replace("'", " ")
            if param.startswith('command='):
                self.commands.append(param[8:])
            else:
                pass

    def run_command(self, command):
        ''' Run a command '''

        if command.find('|') > -1:
            action = command.split('|')

            log_msg('%s.run_command. command: %s, parameter: %s' \
                % (self.logprefix, action[0], action[1]), xbmc.LOGNOTICE)

            return self.avrcontroller.run_command(action[0], action[1])
        else:
            log_msg('%s.run_command. Command %s missing required parameter' \
                % (self.logprefix, command), xbmc.LOGNOTICE)

    def close(self):
        ''' Cleanup '''
        log_msg('%s version %s exited' \
            % (self.logprefix, self.addonversion), xbmc.LOGNOTICE)
