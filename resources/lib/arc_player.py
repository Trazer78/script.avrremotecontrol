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

        self.addon = xbmcaddon.Addon(ADDON_ID)
        device = self.addon.getSetting('arc_device')

        # Get event settings
        self.service_started = self.addon.getSetting('arc_service_started')
        self.playback_started = self.addon.getSetting('arc_playback_started')
        self.playback_paused = self.addon.getSetting('arc_playback_paused')
        self.playback_resumed = self.addon.getSetting('arc_playback_resumed')
        self.playback_ended = self.addon.getSetting('arc_playback_ended')
        self.playback_stopped = self.addon.getSetting('arc_playback_stopped')

        # Exececute command on startup of service
        self.avrcontroller = AVRController(device)
        log_msg('%s Detected service started' % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.service_started)

    def onPlayBackStarted(self):
        ''' Event: xbmc.Player.onPlayBackStarted '''
        log_msg("%s Detected playback started" % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_started)

    def onPlayBackPaused(self):
        ''' Event: xbmc.Player.onPlayBackPaused '''
        log_msg("%s Detected playback paused" % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_paused)

    def onPlayBackResumed(self):
        ''' Event: xbmc.Player.onPlayBackResumed '''
        log_msg("%s Detected playback resumed" % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_resumed)

    def onPlayBackEnded(self):
        ''' Event: xbmc.Player.onPlayBackEnded '''
        log_msg("%s Detected playback ended" % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_ended)

    def onPlayBackStopped(self):
        ''' Event: xbmc.Player.onPlayBackStopped '''
        log_msg("%s Detected playback stopped" % (self.logprefix), loglevel=xbmc.LOGNOTICE)
        self.run_commands(self.playback_stopped)

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
