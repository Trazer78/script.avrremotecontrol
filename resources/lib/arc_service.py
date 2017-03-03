#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    arc_service.py --> Service implementation
'''
from resources.lib.arc_monitor import ArcMonitor
from resources.lib.arc_player import ArcPlayer
from resources.lib.utils import ADDON_ID, log_msg
import xbmc
import xbmcaddon

class ArcService(object):
    ''' AVR Remote Control service implementation '''

    def __init__(self):
        self.logprefix = "("+self.__class__.__name__+")"

        addon = xbmcaddon.Addon(ADDON_ID)
        # Get info
        self.addonversion = addon.getAddonInfo('version')
        self.addonname = addon.getAddonInfo('name')

        log_msg('%s version %s started' \
            % (self.logprefix, self.addonversion), xbmc.LOGNOTICE)

        self.arcmonitor = ArcMonitor()
        self.arcplayer = ArcPlayer()

        while not self.arcmonitor.abortRequested():
            # Sleep/wait for abort for 1 second.
            self.arcmonitor.waitForAbort(10)

        log_msg('%s version %s shutdown requested' \
            % (self.logprefix, self.addonversion), xbmc.LOGNOTICE)

        # Cleanup
        self.close()

    def close(self):
        ''' Cleanup '''
        del self.arcmonitor
        del self.arcplayer
        log_msg('%s version %s finished' \
            % (self.logprefix, self.addonversion), xbmc.LOGNOTICE)
