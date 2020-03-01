import PyTango

from fsm.common.logging import MyLogger

tango_base_path = 'tango://cci3he10.se.frm2.tum.de:10000/box/plc/_'
tango_lakeshore_path = 'tango://cci3he10.se.frm2.tum.de:10000/box/lakeshore/'


class Device(object):
    def __init__(self, name):
        # control elements lakeshore
        filter = 'sens'
        f = name.find(filter)
        if name.find(filter) != -1:
            self.dev = tango_lakeshore_path + name
        else:
            self._dev = tango_base_path + name

        self._dev = PyTango.DeviceProxy(tango_base_path, name.lower())
        self._name = name
        self._status = self.read()
        self.log = MyLogger().get_logger()
        # todo get feedback from device

    def move(self, status):
        """ change status """
        self._status = status
        self.log.info('Device: {0}, Status: {1}'.format(self._name, self._status))
        # todo change the status of device

    def read(self):
        """ get (read) status from device """
        return self._dev.value
        # test
        # return '0'

