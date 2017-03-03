#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    utils.py --> Helper functions
'''
import os
import json
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
    log_msg('Exception in %s ! --> %s' % (modulename, exceptiondetails), xbmc.LOGERROR)

def telnet_execute(avrcommand, withresponse=False):
    ''' Send a command to the AVR Device via telnet '''

    addon = xbmcaddon.Addon(ADDON_ID)
    ipaddress = addon.getSetting('ip')
    port = int(addon.getSetting('port'))
    timeout = int(addon.getSetting('timeout'))
    delay = float(int(addon.getSetting('delay'))/1000)

    log_msg('(telnet_execute) ip: %s, port: %s, timeout: %s, delay: %s' \
        % (ipaddress, port, timeout, delay))

    try:
        _tn = telnetlib.Telnet(ipaddress, port, timeout)
    except Exception as exc:
        log_exception(__name__, exc)
        return "Error occured while connecting to AVR telnet server"

    log_msg('(telnet_execute) command: %s' % avrcommand, xbmc.LOGNOTICE)

    try:
        _tn.write(avrcommand+"\r")
    except Exception as exc:
        log_exception(__name__, exc)
        _tn.close()
        return "Error occured while writing to AVR telnet server"

    if withresponse:
        time.sleep(delay)
        response = _tn.read_eager()
    else:
        response = "not waiting for a response"
    _tn.close()

    log_msg('(telnet_execute) Response: %s' % \
        (response), loglevel=xbmc.LOGNOTICE)

    return response

def decode_folder(folder):
    """
    :param folder:
    :return:
    """
    return folder.decode(sys.getfilesystemencoding())

def get_addon_path():
    ''' Get installed addon path '''

    return xbmcaddon.Addon(ADDON_ID).getAddonInfo('path').decode("utf-8")

def load_json(filename):
    ''' Load json from file to object '''

    jsonfile = decode_folder(os.path.join(get_addon_path(), filename))

    log_msg('%s --> (load_json) Loading from file: %s' % (ADDON_NAME, jsonfile))

    with open(jsonfile, 'r') as devicefile:
        jsoninfo = json.loads(devicefile.read())

    log_msg('%s --> (load_json) Loaded from file: %s' % (ADDON_NAME, jsoninfo))

    return jsoninfo
