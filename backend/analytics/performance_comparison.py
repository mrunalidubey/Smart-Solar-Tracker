
from backend.algorithms.power_calculator import PowerCalculator
from backend.simulation.solar_simulator import SolarSimulator


class PerformanceComparison:
    def __init__(self):
        self.solar = SolarSimulator()
        self.calculator = PowerCalculator()

    def compare(self, cloud_cover=10):
        tracking_energy = 0
        fixed_energy = 0

        # Calculate energy over 12 one-hour intervals
        for hour in range(6, 18):
            start = self.solar.simulate(hour, cloud_cover)
            end = self.solar.simulate(hour + 1, cloud_cover)

            tracking_start = self.calculator.calculate_power(
                start["sunlight_intensity"]
            )["power"]

            tracking_end = self.calculator.calculate_power(
                end["sunlight_intensity"]
            )["power"]

            fixed_start = self.calculator.calculate_power(
                start["sunlight_intensity"] * 0.75
            )["power"]

            fixed_end = self.calculator.calculate_power(
                end["sunlight_intensity"] * 0.75
            )["power"]

            tracking_energy += (tracking_start + tracking_end) / 2
            fixed_energy += (fixed_start + fixed_end) / 2

        energy_gain = tracking_energy - fixed_energy

        improvement = (
            (energy_gain / fixed_energy) * 100
            if fixed_energy > 0 else 0
        )

        return {
            "tracking_energy": round(tracking_energy, 2),
            "fixed_energy": round(fixed_energy, 2),
            "energy_gain": round(energy_gain, 2),
            "improvement_percentage": round(improvement, 2)
        }


if __name__ == "__main__":
    comparison = PerformanceComparison()
    result = comparison.compare()

    print("\nFIXED VS TRACKING PANEL")
    print("-----------------------")

    for key, value in result.items():
        print(f"{key}: {value}")
