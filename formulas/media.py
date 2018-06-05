import numpy

from core.timer import RepeatingTimer

class MED(object):
    def __init__(self, **kwargs):
        print 'init funfado'
        self.values = []
        pass

    def add_values(value):
        self.values.append(value)

    def execute(self):
        pass

class MED_T(object):
    def __init__(self, *argv):
        self.time_delta = int(argv[0][0])
        self.service_type = argv[0][1]
        self.service_ids = argv[0][2]
        self.master_formula = False
        self.timer = RepeatingTimer(self.time_delta, 'topico', self.execute)
        # print self.master_formula

    def configure(self, formula):
        pass
    def execute(self, topic, delta):
        print 'execuuuuu           te'
        print topic
        print delta
        # return numpy.sum(values)/len(values)

class MED_N(object):
    def __init__(self, **kwargs):
        pass
    def configure(self, formula):
        pass
    def execute(self, values):
        return numpy.sum(values)/len(values)
