
from backend.simulation.solar_simulator import SolarSimulator
from backend.simulation.sensor_simulator import SensorSimulator
from backend.simulation.motor_simulator import MotorSimulator

from backend.algorithms.tracking_algorithm import TrackingAlgorithm
from backend.algorithms.power_calculator import PowerCalculator


class SimulationEngine:

    def __init__(self):
        self.solar = SolarSimulator()
        self.sensors = SensorSimulator()
        self.tracker = TrackingAlgorithm()
        self.calculator = PowerCalculator()
        self.motor = MotorSimulator()

    def run_simulation(self, hour, cloud_cover=0):

        sunlight = self.solar.simulate(hour, cloud_cover)

        sensor_readings = self.sensors.read_sensors(
            sunlight["sunlight_intensity"]
        )

        tracking_result = self.tracker.calculate_movement(
            sensor_readings
        )

        motor_result = self.motor.move_motor(
            tracking_result["movement"],
            duration=1
        )

        power_result = self.calculator.calculate_power(
            sunlight["sunlight_intensity"]
        )

        return {
            "sunlight": sunlight,
            "sensors": sensor_readings,
            "tracking": tracking_result,
            "motor": motor_result,
            "power": power_result
        }


if __name__ == "__main__":

    engine = SimulationEngine()
    result = engine.run_simulation(hour=12, cloud_cover=10)

    print("\nSMART SOLAR TRACKER")
    print("===================")
    print("SUNLIGHT:", result["sunlight"])
    print("SENSORS:", result["sensors"])
    print("TRACKING:", result["tracking"])
    print("MOTOR:", result["motor"])
    print("POWER:", result["power"])
