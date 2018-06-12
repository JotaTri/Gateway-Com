import numpy

from core.timer import RepeatingTimer

import datetime

import sqlite3

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
        self.service_ids = argv[0][2].replace('[','').replace(']', '').split(',')
        for arg in argv[0]:
            print arg
        self.master_formula = False
        self.topico = 'topico'
        self.timer = RepeatingTimer(self.time_delta, self.execute)
        # print self.master_formula

    def configure(self, formula):
        pass
    def execute(self):
        conn = sqlite3.connect('/home/jota/DB/uiot.db')
        cursor = conn.cursor()
        time_delta = (datetime.datetime.now() - datetime.timedelta(minutes = self.time_delta))#.strftime()
        print time_delta
        d = cursor.execute('SELECT created_at as "[timestamp]" FROM data WHERE id < 10')
        for item in d:
            print item[0]
            temp = datetime.datetime.strptime(item[0], '%Y-%m-%d %H:%M:%S.%f')
            print temp
            print type(temp)
        d = cursor.execute('SELECT data FROM data WHERE created_at > "' + time_delta.strftime('%Y-%m-%d %H:%M:%S.%f') + '"').fetchall()
        values = []
        for item in d:
            print item[0]
            print type(item[0])
            print float(item[0])
            values.append(float(item[0]))
            print values
        # print 'Executando a Media dos servicos de nome ' + self.service_type + ' e dos servicos de ids ' + str(self.service_ids) +  ' a partir dos ultimos ' + str(self.time_delta) + ' minutos'
        # print 'Executando o PUBLISH no topico:' + self.topico
        # return numpy.sum(values)/len(values)
        print numpy.sum(values)/len(values)

class MED_N(object):
    def __init__(self, **kwargs):
        pass
    def configure(self, formula):
        pass
    def execute(self, values):
        return numpy.sum(values)/len(values)
