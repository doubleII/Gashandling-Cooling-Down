from .state import State
from fsm.data.models import Device


class Initialize(State):
    """ start Zustand """
    def __init__(self, fsm):
        super(Initialize, self).__init__(fsm)


    def enter(self):
        self.log.info('Initialize enter')
        # this state does not need a time parameters
        super(Initialize, self).enter(0, 0)

    def execute(self):
        self.log.info('Initialize execute')
        init_valves = self.fsm.data['Initialize']['valves']
        for i in init_valves:
            self.fsm.valves[i] = Device('v%d' % i)
            self.fsm.valves[i].read()

        self.fsm.booster_pump = Device(self.fsm.data['Initialize']['forpump'])
        self.fsm.compressor = Device(self.fsm.data['Initialize']['compressor'])

        self.fsm.to_transition("to_measure_precooling")

    def exit(self):
        self.log.info('initialize successful')
