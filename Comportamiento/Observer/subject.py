"""1. Gestiona todos los obervadorer que serán notificados cuando cambie el estado del sujeto."""


class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def register_observer(self, observer):    
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observer(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observer()  
        

    