from threading import Timer

class RepeatingTimer(object):
    def __init__(self, time_delta, topic, services, function):
        self.time_delta = time_delta
        self.topic = topic
        # self.services = services
        self.function = function
        self.timer = Timer(self.time_delta, self.function_handler, [services])

    def function_handler(self, services):
        self.function(services, self.time_delta)
        self.timer = Timer(self.time_delta, self.function_handler, [services])
        self.timer.start()

    def cancel(self):
        self.timer.cancel()
    # def new_service_timer(self, service_id, time_delta):
    #     self.service_timers[service_id] = Timer(time_delta, self.p, [service_id, time_delta])
    #     self.service_timers[service_id].start()

    def p(self, service_id, time_delta):
        print service_id
        print time_delta

class teste(object):
    """docstring for teste."""
    def coisa(self, par1, par2):
        print par1
        print par2
t = RepeatingTimer(2,1,1,teste().coisa)
t.timer.start()
while True:
    pass
