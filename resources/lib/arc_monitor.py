#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    arc_monitor.py --> Custom Kodi Monitor class
'''
from resources.lib.devices.avr_controller import AVRController
from resources.lib.utils import log_msg, log_exception, ADDON_ID
import xbmc
import xbmcaddon

class ArcMonitor(xbmc.Monitor):
    ''' Custom Monitor class to handle events '''

    #def __init__(self, **kwargs):
    def __init__(self):
        xbmc.Monitor.__init__(self)
        self.logprefix = '('+self.__class__.__name__+')'

        self.addon = xbmcaddon.Addon(ADDON_ID)

        device = self.addon.getSetting('arc_device')
        self.avrcontroller = AVRController(device)

        self.service_stopped = self.addon.getSetting('arc_service_stopped')

    def onNotification(self, sender, method, data):
        ''' builtin function for the xbmc.Monitor class '''
        try:
            if method == "System.OnQuit":
                self.system_onquit()

        except Exception as exc:
            log_exception(__name__, exc)

    def system_onquit(self):
        ''' Commands to send on Kodi shutdown '''
        log_msg("%s Detected kodi shutdown" % self.logprefix, loglevel=xbmc.LOGNOTICE)

        self.run_commands(self.service_stopped)

    def run_commands(self, setting):
        ''' Get seperate commands from setting '''
        log_msg('%s.run_commands, setting: %s' \
            % (self.logprefix, setting), loglevel=xbmc.LOGNOTICE)

        commands = setting.split(';')
        for command in commands:
            if '|' in command:
                pos = command.find('|')
                cmd = command[:pos]
                param = command[pos+1:]

                self.avrcontroller.parse_command(cmd, param)
            else:
                self.avrcontroller.parse_command(command)
