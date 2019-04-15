class Celsius:
    def __init__(self,temperature=0):
        self._temperature=max(temperature,-273)
    def to_fahrenheit(self):
        F=9/5*self.temperature +32
        return F
    def get_temperature(self):
        return self._temperature
    def set_temperature(self,value):
        if value > -273 :
            self._temperature = value
        else:
            self._temperature = -273
    temperature=property(fget=get_temperature,fset=set_temperature)