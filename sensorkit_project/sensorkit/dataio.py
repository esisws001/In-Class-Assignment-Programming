"""
Module: sensorkit/dataio.py
Contributor: Elim Kofi Essikpe
Student ID: 78642029
Date: 5th August, 2026
Role: Load raw sensor readings from a text/CSV file, safely.

Uses pathlib for the file path and exceptions to handle problems.
Complete the TODOs below.
"""
from pathlib import Path


def load_readings(filepath):
    """
    Read a file of raw numeric readings, one value per line, and return
    a list of floats.

    Rules:
      - If the file does not exist, raise FileNotFoundError.
      - Ignore blank lines.
      - If a line is not a valid number, skip it and print a short message
        instead of letting the program crash.
    """
    path = Path(filepath)
    readings = []
    with open (path, "r") as file:
        for line in file:
            try:
                line = float(line.strip())
                readings.append(line)                        
            except (ValueError):
                print(f"Skipping invalid line: {line!r}")

        return readings
