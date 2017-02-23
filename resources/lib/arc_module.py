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
from resources.lib.utils import log_msg, log_exception, ADDON_ID

class ArcModule(object):
    ''' AVR Remote Control module implementation '''

    def __init__(self):
        self.logprefix = "("+self.__class__.__name__+")"

        addon = xbmcaddon.Addon(ADDON_ID)
        self.addonversion = addon.getAddonInfo('version')
        device = addon.getSetting("arc_device")

        log_msg("%s version %s entered" \
            % (self.logprefix, self.addonversion), xbmc.LOGNOTICE)

        # Parse submitted arguments
        self._parse_argv()

        # Instantiate classes
        self.avrcontroller = AVRController(device)

        for command in self.commands:
            log_msg(self.logprefix+' '+command, xbmc.LOGNOTICE)

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

        pos = command.find('|')
        if pos > -1:
            cmd = command[:pos]
            param = command[pos+1:]

            log_msg(self.logprefix+' '+cmd, xbmc.LOGNOTICE)
            log_msg(self.logprefix+' '+param, xbmc.LOGNOTICE)

            self.avrcontroller.parse_command(cmd, param)
        else:
            self.avrcontroller.parse_command(command)

    def close(self):
        ''' Cleanup '''
        log_msg("%s version %s exited" \
            % (self.logprefix, self.addonversion), xbmc.LOGNOTICE)
