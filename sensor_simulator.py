"""
sensor_simulator.py
Simulates IoT sensor readings for the Remote Farm Management System.
Generates temperature, humidity, and soil moisture data for farm fields.
"""

import random
import time
from datetime import datetime


FIELDS = ["Field_A", "Field_B", "Field_C"]


def read_temperature(field: str) -> float:
    """Simulate a temperature sensor reading in Celsius."""
    base = {"Field_A": 24.0, "Field_B": 26.5, "Field_C": 22.0}
    return round(base.get(field, 25.0) + random.uniform(-2.0, 2.0), 2)


def read_humidity(field: str) -> float:
    """Simulate a humidity sensor reading as a percentage."""
    base = {"Field_A": 60.0, "Field_B": 55.0, "Field_C": 70.0}
    return round(base.get(field, 65.0) + random.uniform(-5.0, 5.0), 2)


def read_soil_moisture(field: str) -> float:
    """Simulate a soil moisture sensor reading as a percentage."""
    base = {"Field_A": 40.0, "Field_B": 35.0, "Field_C": 50.0}
    return round(base.get(field, 45.0) + random.uniform(-3.0, 3.0), 2)


def collect_readings() -> list[dict]:
    """Collect one round of sensor readings from all fields."""
    timestamp = datetime.now().isoformat()
    readings = []
    for field in FIELDS:
        reading = {
            "timestamp": timestamp,
            "field": field,
            "temperature_c": read_temperature(field),
            "humidity_pct": read_humidity(field),
            "soil_moisture_pct": read_soil_moisture(field),
        }
        readings.append(reading)
    return readings


def check_alerts(reading: dict) -> list[str]:
    """Return a list of alert messages if any sensor value is out of range."""
    alerts = []
    if reading["temperature_c"] > 35:
        alerts.append(f"[ALERT] High temperature in {reading['field']}: {reading['temperature_c']}°C")
    if reading["humidity_pct"] < 30:
        alerts.append(f"[ALERT] Low humidity in {reading['field']}: {reading['humidity_pct']}%")
    if reading["soil_moisture_pct"] < 20:
        alerts.append(f"[ALERT] Low soil moisture in {reading['field']}: {reading['soil_moisture_pct']}%")
    return alerts


def run(interval_seconds: int = 5, cycles: int = 3):
    """Run the sensor simulator for a given number of cycles."""
    print("=== Remote Farm Sensor Simulator ===\n")
    for cycle in range(1, cycles + 1):
        print(f"--- Cycle {cycle} ---")
        readings = collect_readings()
        for r in readings:
            print(
                f"[{r['timestamp']}] {r['field']} | "
                f"Temp: {r['temperature_c']}°C | "
                f"Humidity: {r['humidity_pct']}% | "
                f"Soil Moisture: {r['soil_moisture_pct']}%"
            )
            for alert in check_alerts(r):
                print(alert)
        print()
        if cycle < cycles:
            time.sleep(interval_seconds)
    print("Simulation complete.")


if __name__ == "__main__":
    run(interval_seconds=2, cycles=3)
