"""
Module: sensorkit/report.py
Contributor: Ewura Esi Ohene-Boakye
Student ID: 41492029
Date: 05/08/2026
Role: Produce a printed summary of calibrated readings for one sensor.

This module ties together a sensor (from sensors.py) and the statistics
functions (from stats.py). Complete the TODOs below.
"""
from .stats import mean, minimum, maximum, spread


def summarise(sensor, raw_readings):
    """
    Given a sensor object and a list of raw readings:
      1. Calibrate every raw reading using sensor.read(...)
      2. Print a short summary using the stats functions.
    """
    # TODO : build a list `calibrated` containing sensor.read(r)
    #         for every r in raw_readings
    calibrated=[]
    for r in raw_readings:
        calibrated += [sensor.read(r)]

    # TODO : get the unit string from sensor.units() and store it in `u`
    u=sensor.units()
    # TODO : print the report. Suggested lines (format numbers to 2 d.p.):
    name= sensor.name
    avg= mean(calibrated)
    min_val=minimum(calibrated)
    max_val=maximum(calibrated)
    the_spread=spread(calibrated)
    report =f'Report for {name}\n count: {len(calibrated)}\nmean: {avg:.2f} {u}\nmin: {min_val:.2f} {u}\nmax:{max_val:.2f} {u}\nspread: {the_spread:.2f} {u}'
    #         Report for <sensor.name>
    #           count:   <how many readings>
    #           mean:    <mean> <u>
    #           min:     <minimum> <u>
    #           max:     <maximum> <u>
    #           spread:  <spread> <u>
    print(report)
