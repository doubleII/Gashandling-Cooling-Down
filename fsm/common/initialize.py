from .state import State
from fsm.data.models import Device


class Initialize(State):
    """ start Zustand """
    def __init__(self, fsm):
        super(Initialize, self).__init__(fsm)
        self.valves = {}
        for i in list(range(1, 7)) + list(range(10, 14)):
            self.valves[i] = Device('V%d' % i, "false")

    def enter(self):
        self.log.info('Initialize enter')
        # this state does not need a time parameters
        super(Initialize, self).enter(0, 0)

    def execute(self):
        # todo set all device to false or check if the are working
        self.log.info('Initialize execute')
        for v in self.valves.values():
            v.read()
        self.fsm.to_transition("to_measure_precooling")

    def exit(self):
        self.log.info('initialize successful')
