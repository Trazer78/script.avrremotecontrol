#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    arc_player.py --> Custom Kodi Player class
'''
from resources.lib.devices.avr_controller import AVRController
from resources.lib.utils import log_msg, ADDON_ID
import xbmc
import xbmcaddon

class ArcPlayer(xbmc.Player):
    ''' Custom Kodi Player class to handle events '''

    def __init__(self):
        self.logprefix = '('+self.__class__.__name__+')'

        addon = xbmcaddon.Addon(ADDON_ID)
        make = addon.getSetting('make')
        model = addon.getSetting('%s_model' % make.lower())

        # Get event settings
        self.playback_started = addon.getSetting('playback_started')
        self.playback_paused = addon.getSetting('playback_paused')
        self.playback_resumed = addon.getSetting('playback_resumed')
        self.playback_ended = addon.getSetting('playback_ended')
        self.playback_stopped = addon.getSetting('playback_stopped')

        self.avrcontroller = AVRController(make, model)

    def onPlayBackStarted(self):
        ''' Event: xbmc.Player.onPlayBackStarted '''
        log_msg('%s Detected playback started' % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_started)

    def onPlayBackPaused(self):
        ''' Event: xbmc.Player.onPlayBackPaused '''
        log_msg('%s Detected playback paused' % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_paused)

    def onPlayBackResumed(self):
        ''' Event: xbmc.Player.onPlayBackResumed '''
        log_msg('%s Detected playback resumed' % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_resumed)

    def onPlayBackEnded(self):
        ''' Event: xbmc.Player.onPlayBackEnded '''
        log_msg('%s Detected playback ended' % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_ended)

    def onPlayBackStopped(self):
        ''' Event: xbmc.Player.onPlayBackStopped '''
        log_msg('%s Detected playback stopped' % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_stopped)

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
