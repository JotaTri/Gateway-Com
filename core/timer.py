from threading import Timer

import signal
import os
import time

class RepeatingTimer(object):
    def __init__(self, time_delta, topic, function):
        self.time_delta = time_delta
        self.topic = topic
        # self.services = services
        self.function = function
        print self.function
        self.timer = Timer(self.time_delta, self.function_handler, [topic])
        signal.signal(signal.SIGINT, self.cancel)
        self.timer.start()


    def function_handler(self, services):
        self.function(self.topic, self.time_delta)
        self.timer = Timer(self.time_delta, self.function_handler, [services])
        self.timer.start()

    def cancel(self,ignal, frame):
        print 'foiiiiiiiiii'
        self.timer.cancel()
        time.sleep(0.5)
        os._exit(1)
    # def new_service_timer(self, service_id, time_delta):
    #     self.service_timers[service_id] = Timer(time_delta, self.p, [service_id, time_delta])
    #     self.service_timers[service_id].start()

    def p(self, t):
        print t
