#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    utils.py --> Helper functions
'''
import sys
import telnetlib
import time
from traceback import format_exc
import xbmc
import xbmcaddon

ADDON_ID = "script.avrremotecontrol"
ADDON_NAME = "AVR Remote Control"

def log_msg(msg, loglevel=xbmc.LOGDEBUG):
    '''log message to kodi log'''

    if isinstance(msg, unicode):
        msg = msg.encode('utf-8')

    xbmc.log(ADDON_NAME+" --> %s" % msg, level=loglevel)

def log_exception(modulename, exceptiondetails):
    '''helper to properly log an exception'''

    log_msg(format_exc(sys.exc_info()), xbmc.LOGWARNING)
    log_msg("Exception in %s ! --> %s" % (modulename, exceptiondetails), xbmc.LOGERROR)

def telnet_execute(command, withresponse=False):
    ''' Send a command to the AVR Device via telnet '''
    log_msg(ADDON_NAME+" --> (telnet_execute)")

    addon = xbmcaddon.Addon(ADDON_ID)
    ipaddress = addon.getSetting('arc_ip')
    port = int(addon.getSetting('arc_port'))
    timeout = int(addon.getSetting('arc_timeout'))
    delay = float(int(addon.getSetting('arc_delay'))/1000)

    log_msg("(telnet_execute) ip: %s, port: %s, timeout: %s, delay: %s" \
        % (ipaddress, port, timeout, delay))

    try:
        _tn = telnetlib.Telnet(ipaddress, port, timeout)
    except Exception as exc:
        log_exception(__name__, exc)
        return "Error occured while connecting to AVR telnet server"

    log_msg('(telnet_execute) Request: '+command, loglevel=xbmc.LOGNOTICE)

    _tn.write(command+"\r")
    if withresponse:
        time.sleep(delay)
        response = _tn.read_eager()
    else:
        response = "not waiting for a response"
    _tn.close()

    log_msg("(telnet_execute) Response: "+response, loglevel=xbmc.LOGNOTICE)

    return response

def get_addon_path():
    ''' Get installed addon path '''

    return xbmcaddon.Addon(ADDON_ID).getAddonInfo('path').decode("utf-8")
