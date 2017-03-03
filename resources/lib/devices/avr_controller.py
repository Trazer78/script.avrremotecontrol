# -*- coding: utf-8 -*-

'''
    script.avrremotecontrol
    Service and scripts for controlling AVR via telnet

    avr_controller.py --> Generic AVR controller implementation
'''
import importlib
#from resources.lib.devices.denon import avr_x2000, avr_e400
#from resources.lib.devices.pioneer import vsx_923
from resources.lib.utils import log_msg, log_exception

class AVRController(object):
    ''' Generic AVRController class which contains logic based on device type '''

    def __init__(self, make, model):
        self.logprefix = '('+self.__class__.__name__+')'
        log_msg('%s.__init__' % self.logprefix)

        # Initialize AVR Device
        self.avrdevice = self.get_device(make, model)

    def run_command(self, command, parameter, response=False):
        ''' Call the specified command on the device '''
        log_msg('%s.run_command. command: %s, parameter: %s' % \
            (self.logprefix, command, parameter))

        if self.avrdevice != None:
            return self.avrdevice.run_command(command, parameter, response)
        else:
            log_msg('%s.run_command Unsupported AVR' % self.logprefix)
            return "Unsupported AVR"

    def get_device(self, make, model):
        ''' Get device instance based on the device make and model '''
        log_msg('%s.get_device make: %s, model: %s' % (self.logprefix, make, model))

        # Classnames or named as [Make][Model] without spaces and - character
        avrclassname = '%s%s' % (make, model.replace('-', ''))
        try:
            # Fully qualified modulename:
            # resources.lib.devices.[make].[model]
            # [make]  -> lower case
            # [model] -> lower case and: - converted to _
            avrmodulename = "resources.lib.devices.%s.%s" \
                % (make.lower(), model.replace('-', '_').lower())
            avrmodule = importlib.import_module(avrmodulename)

            # return an instance of the determined class
            return getattr(avrmodule, avrclassname)()

        except Exception as exc:
            log_exception("", exc)
            return None
