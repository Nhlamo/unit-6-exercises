# ----- EXERCISE 1 CODE 

from resistor import Resistor

resistor1 = Resistor(resistance_ohms=10, voltage=5)
resistor2 = Resistor(resistance_ohms=220, voltage=12)
current1 = resistor1.calculate_current()
print("Resistor 1 Details:")
print(f"  Resistance: {resistor1.resistance_ohms} ohms")
print(f"  Voltage:    {resistor1.voltage} V")
print(f"  Current:    {current1:.4f} A\n")

current2 = resistor2.calculate_current()
print("Resistor 2 Details:")
print(f"  Resistance: {resistor2.resistance_ohms} ohms")
print(f"  Voltage:    {resistor2.voltage} V")
print(f"  Current:    {current2:.4f} A")


# --- EXERCISE 2 CODE ---
from sensor_utils import celsius_to_fahrenheit

celsius_readings = [0.0, 20.5, 37.0, 100.0]
print("Temperature Conversion Log:")
for celsius in celsius_readings:
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"  {celsius}°C = {fahrenheit}°f")

# --- EXERCSE 3 CODE ---

from system_logger import log_event

log_event("INFO: Motor starting sequence initiated.")

voltage_reading = 12.0
log_event(f"MEASUREMENT: Main circuit voltage recorded at {voltage_reading} V.")

try:
    print("Simulating dangerous operation...")
    resistance = 0
    current = voltage_reading / resistance
except ZeroDivisionError as e:
    log_event(f"CRITICAL ERROR: Short circuit hazard detected! {e}")

print("All events have been successfully recorded to system.log.")