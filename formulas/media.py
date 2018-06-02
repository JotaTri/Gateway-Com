import numpy

class MED(object):
    def __init__(self, values):
        self.values = values

    def execute(self):
        pass

class MED_T(object):
    def __init__(self, **kwargs):
        self.time_delta = kwargs['time_delta']
        self.service_type = kwargs['service_type']
        self.service_ids = kwargs['service_ids']
        self.master_formula = kwargs['master_formula']

    def configure(self, formula):
        pass
    def execute(self, ids):

        return numpy.sum(values)/len(values)

class MED_N(object):
    def __init__(self, **kwargs):
        pass
    def configure(self, formula):
        pass
    def execute(self, values):
        return numpy.sum(values)/len(values)
