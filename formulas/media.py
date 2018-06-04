import numpy

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
    def __init__(self, **kwargs):
        self.time_delta = kwargs['delta']
        self.service_type = kwargs['service_type']
        self.service_ids = kwargs['service_ids']
        self.master_formula = False
        print self.time_delta
        print self.service_type
        print self.service_ids
        # print self.master_formula

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
