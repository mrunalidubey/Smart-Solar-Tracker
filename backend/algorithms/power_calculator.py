
class PowerCalculator:

    def __init__(self, panel_area=1.6, efficiency=0.20):
        self.panel_area = panel_area
        self.efficiency = efficiency
        self.voltage = 18

    def calculate_power(self, sunlight_intensity):

        power = (
            sunlight_intensity
            * self.panel_area
            * self.efficiency
        )

        current = power / self.voltage if power > 0 else 0

        return {
            "voltage": round(self.voltage if power > 0 else 0, 2),
            "current": round(current, 2),
            "power": round(power, 2)
        }

    def calculate_energy(self, power, duration_hours):

        energy = power * duration_hours

        return round(energy, 2)


if __name__ == "__main__":

    calculator = PowerCalculator()

    result = calculator.calculate_power(900)

    print("SOLAR POWER CALCULATION")
    print("-----------------------")

    for key, value in result.items():
        print(f"{key}: {value}")

    energy = calculator.calculate_energy(
        result["power"], 1
    )

    print("Energy generated:", energy, "Wh")
