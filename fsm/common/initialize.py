from fsm.data.models import Device
from .state import State


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
        self.fsm.p_in_let = Device(self.fsm.data['Initialize']['pInlet'])
        self.fsm.p_still = Device(self.fsm.data['Initialize']['pStill'])
        self.fsm.p_kond = Device(self.fsm.data['Initialize']['pKond'])
        self.fsm.p_out_let = Device(self.fsm.data['Initialize']['pUotlet'])
        self.fsm.p_vacc = Device(self.fsm.data['Initialize']['pVacc'])
        self.fsm.p_v_15 = Device(self.fsm.data['Initialize']['pV15'])
        self.fsm.temp_sensor_a = Device(self.fsm.data['Initialize']['temp_sensor_a'])
        self.fsm.temp_sensor_b = Device(self.fsm.data['Initialize']['temp_sensor_b'])


        self.fsm.to_transition("to_measure_precooling")

    def exit(self):
        self.log.info('initialize successful')
