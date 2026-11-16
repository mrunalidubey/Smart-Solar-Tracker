
import math


class SolarSimulator:
    def __init__(self):
        self.sunrise = 6
        self.sunset = 18
        self.max_intensity = 1000
        self.max_elevation = 60

    def simulate(self, hour, cloud_cover=0):
        """
        Simulate sunlight intensity and sun position.

        hour: Time between 0 and 24
        cloud_cover: Percentage between 0 and 100
        """

        if not 0 <= hour <= 24:
            raise ValueError("Hour must be between 0 and 24")

        if not 0 <= cloud_cover <= 100:
            raise ValueError("Cloud cover must be between 0 and 100")

        if hour < self.sunrise or hour > self.sunset:
            return {
                "hour": hour,
                "sunlight_intensity": 0,
                "sun_elevation": 0,
                "sun_azimuth": 0,
                "daylight": False
            }

        # Calculate sunlight intensity
        progress = (hour - self.sunrise) / (
            self.sunset - self.sunrise
        )

        sunlight = math.sin(math.pi * progress)

        intensity = (
            self.max_intensity
            * sunlight
            * (1 - cloud_cover / 100)
        )

        # Calculate sun elevation
        elevation = self.max_elevation * sunlight

        # Approximate sun direction
        azimuth = 90 + (180 * progress)

        return {
            "hour": round(hour, 2),
            "sunlight_intensity": round(intensity, 2),
            "sun_elevation": round(elevation, 2),
            "sun_azimuth": round(azimuth, 2),
            "daylight": True
        }

if __name__ == "__main__":
    solar = SolarSimulator()

    result = solar.simulate(
        hour=12,
        cloud_cover=10
    )

    print("SOLAR SIMULATION RESULTS")
    print("------------------------")

    for key, value in result.items():
        print(f"{key}: {value}")
