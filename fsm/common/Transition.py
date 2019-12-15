from fsm.common.logging import MyLogger

LOGGER = MyLogger().get_logger()


class Transition(object):
    """ """
    def __init__(self, to_state):
        self.to_state = to_state

    def execute(self):
        LOGGER.info('Transitioning to state {0} ...'.format(self.to_state))
