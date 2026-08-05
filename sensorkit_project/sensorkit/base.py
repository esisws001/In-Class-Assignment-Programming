"""
Module: sensorkit/base.py
Contributor: Huda Suglo Suleman
Student ID: 58632029
Date: August 5th, 2026.
Role: Define the abstract Sensor base class that every sensor must follow.

Complete the TODOs below.
"""
from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, name):
        self.name= name

    @abstractmethod
    def read(self, raw):
        """Convert a raw signal value into a calibrated reading."""
        pass

   @abstractmethod
    def units(self):
        """Return this sensor's unit string, e.g. 'C' or 'bar'."""
        pass

    def describe(self):
        """Concrete method shared by all sensors."""
        print (f' {self.name} sensor, measured in {self.units}')
        
