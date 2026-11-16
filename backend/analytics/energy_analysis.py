
from backend.simulation.simulation_engine import SimulationEngine


class EnergyAnalysis:
    def __init__(self):
        self.engine = SimulationEngine()

    def analyze_day(self, cloud_cover=10):
        hourly_data = []

        for hour in range(6, 19):
            result = self.engine.run_simulation(
                hour=hour,
                cloud_cover=cloud_cover
            )

            hourly_data.append({
                "hour": hour,
                "power": result["power"]["power"]
            })

        total_energy = 0

        # Trapezoidal integration over each 1-hour interval
        for i in range(len(hourly_data) - 1):
            p1 = hourly_data[i]["power"]
            p2 = hourly_data[i + 1]["power"]
            total_energy += (p1 + p2) / 2

        powers = [item["power"] for item in hourly_data]

        peak_power = max(powers) if powers else 0
        best_hour = (
            hourly_data[powers.index(peak_power)]["hour"]
            if powers else 0
        )

        average_power = total_energy / 12 if hourly_data else 0

        return {
            "total_energy_wh": round(total_energy, 2),
            "peak_power_w": round(peak_power, 2),
            "average_power_w": round(average_power, 2),
            "best_hour": best_hour,
            "hourly_data": hourly_data
        }


if __name__ == "__main__":
    analysis = EnergyAnalysis()
    result = analysis.analyze_day()

    print("\nDAILY ENERGY ANALYSIS")
    print("---------------------")

    for key, value in result.items():
        print(f"{key}: {value}")
