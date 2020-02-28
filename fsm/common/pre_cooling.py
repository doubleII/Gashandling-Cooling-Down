from datetime import datetime
from time import process_time

from .state import State

import PyTango
# dev = PyTango.DeviceProxy('tango://cci3he10.se.frm2.tum.de:10000/box/plc/' + ventilname)


class Precooling(State):
    """ wird eine bestimmte Zeit vorgekühlt"""
    def __init__(self, fsm):
        super(Precooling, self).__init__(fsm)

    def enter(self):
        self.log.info('===> Precooling enter')
        # enter state timer
        super(Precooling, self).enter(self.fsm.data['Precooling']['precooling_timer'], self.fsm.data['Precooling']['time_interval'])

    def execute(self):
        self.log.info('Precooling execute method')
        self.state_timer = self.state_timer + process_time()
        self.fsm.precooling_table.clear()

        while self.state_timer > process_time():
            start_time = process_time()
            # interval zwischen die einzelne Messungen
            while start_time + self.time_interval > process_time():
                pass
            # todo read values from Tango
            column = []
            self.fsm.current_temp = 4 # todo read current temperature from sensor
            self.fsm.current_pressure = 7 # todo read current pressure form sensor
            column.append(self.fsm.current_temp)
            column.append(self.fsm.current_pressure)
            # create pre cooling table |current temperature|current pressure| two columns
            self.fsm.precooling_table.append(column)
            self.log.info('test_current_temperature {0} K, test_current_pressure: {1} mbar'
                          .format(self.fsm.current_temp, self.fsm.current_pressure))
            self.log.info('Precooling timer: {0}'.format(process_time()))
            self.log.info('<<< Get feedback for P and T')
        self.fsm.to_transition("to_measure_precooling")

    def exit(self):
        self.log.info('<=== Precooling exit')
