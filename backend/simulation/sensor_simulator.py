
import random


class SensorSimulator:

    def __init__(self):
        self.base_intensity = 500

    def read_sensors(self, sunlight_intensity):

        if sunlight_intensity <= 0:
            return {
                "top_left": 0,
                "top_right": 0,
                "bottom_left": 0,
                "bottom_right": 0
            }

        variation = random.randint(-50, 50)

        sensors = {
            "top_left": sunlight_intensity + variation,
            "top_right": sunlight_intensity - variation,
            "bottom_left": sunlight_intensity - variation // 2,
            "bottom_right": sunlight_intensity + variation // 2
        }

        return {
            key: max(0, round(value, 2))
            for key, value in sensors.items()
        }


if __name__ == "__main__":

    sensor = SensorSimulator()

    readings = sensor.read_sensors(900)

    print("VIRTUAL LDR SENSOR READINGS")
    print("---------------------------")

    for name, value in readings.items():
        print(f"{name}: {value}")
