class Resistor:
    def __init__(self, resistance_ohms, voltage):
        self.resistance_ohms = resistance_ohms
        self.voltage = voltage

    def calculate_current(self):
        return self.voltage / self.resistance_ohms