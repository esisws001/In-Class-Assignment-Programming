"""
Module: sensorkit/sensors.py
Contributor: <Samuel Kwaku Ankrah>
Student ID: <71002029>
Date: <05/08/2026>
Role: Provide concrete sensor classes built on the Sensor base class.

Each class must implement both abstract methods: read() and units().
Complete the TODOs below.
"""
from base import Sensor

class Thermocouple(Sensor):
    def __init__(self,name):
        super().__init__(name)
    def read(self, raw):
        return raw * 24.9 - 0.4
    def units(self):
        return 'C'
        
class PressureGauge(Sensor):
    def __init__(self,name):
        super().__init__(name)
    def read(self, raw):
        return raw * 2.5
    def units(self, raw):
        return 'bar'

class StrainGauge(Sensor):
     def __init__(self,name):
        super().__init__(name)
     def read(self, raw):
         return raw*1000
     def units(self, raw):
        return 'microstrain'
        
     








