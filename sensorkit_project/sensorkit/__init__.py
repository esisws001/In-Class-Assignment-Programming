"""
sensorkit package
A small in-class sensor data toolkit assembled by the whole team.

This file is the ASSEMBLY step (done together once every module is complete).
It exposes the public API so a user can simply write:

    from sensorkit import Thermocouple, load_readings, summarise

If you add a StrainGauge class in sensors.py, add it to the import below too.
"""
from .base import Sensor
from .sensors import Thermocouple 
from .utils import load_readings, summarise

__all__ = [
    "Sensor",
    "Thermocouple",
    "load_readings",
    "summarise",
]
