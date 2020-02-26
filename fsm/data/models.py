import PyTango
from fsm.common.logging import MyLogger

tango_base = 'tango://cci3he10.se.frm2.tum.de:10000/box/plc/_'

class Device(object):
    def __init__(self, name, status):
        self._dev = PyTango.DeviceProxy(tango_base + name.lower())
        self._name = name
        self._status = status
        self.log = MyLogger().get_logger()
        # todo get feedback from device

    def move(self, target):
        self._target = target
        self.log.info('Device: {0}, target: {1}'.format(self._name, self._target))
        # todo change the status of device

    def read(self):
        return self._dev.value
