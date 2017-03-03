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
        self.logprefix = '(%s)' % self.__class__.__name__

        log_msg('%s Detected service started' % (self.logprefix), loglevel=xbmc.LOGNOTICE)

        addon = xbmcaddon.Addon(ADDON_ID)

        self.service_start = addon.getSetting('service_start')
        self.service_stop = addon.getSetting('service_stop')
        self.input_start = addon.getSetting('service_input_start')
        self.input_stop = addon.getSetting('service_input_stop')
        self.input_restore = bool(addon.getSetting('service_input_restore'))
        make = addon.getSetting('make')
        model = addon.getSetting('%s_model' % make.lower())

        self.avrcontroller = AVRController(make, model)

        # If the restore input setting is set Query the AVR for current input
        if self.input_restore:
            self.input_original = self.avrcontroller.run_command("INPUT", "QUERY", True)

        if self.input_start != '':
            self.run_commands('INPUT|%s' % self.input_start)

        # Additional commands to run when kodi/service starts
        if self.service_start != '':
            self.run_commands(self.service_start)

    def onNotification(self, sender, method, data):
        ''' builtin function for the xbmc.Monitor class '''
        try:
            if method == "System.OnQuit":
                self.system_onquit()

        except Exception as exc:
            log_exception(__name__, exc)

    def system_onquit(self):
        ''' Commands to send on Kodi shutdown '''
        log_msg('%s Detected kodi shutdown' % self.logprefix, loglevel=xbmc.LOGNOTICE)

        # If the restore input setting is set restore the AVR to original input
        if self.input_restore:
            self.run_commands('INPUT|%s' % self.input_original)
        else:

            if self.input_stop != '':
                self.run_commands('INPUT|%s' % self.input_stop)

        # Additional commands to run when kodi stops
        if self.service_stop != '':
            self.run_commands(self.service_stop)

    def run_commands(self, setting):
        ''' Get seperate commands from setting '''
        log_msg('%s.run_commands, setting: %s' \
            % (self.logprefix, setting), loglevel=xbmc.LOGNOTICE)

        commands = setting.split(';')
        for command in commands:
            if '|' in command:
                # pos = command.find('|')
                # cmd = command[:pos]
                # param = command[pos+1:]
                # self.avrcontroller.run_command(cmd, param)
                action = command.split('|')
                self.avrcontroller.run_command(action[0], action[1])

            else:
                log_msg('%s.run_commands. Command %s missing required parameter' % \
                    (self.logprefix, command), xbmc.LOGNOTICE)

