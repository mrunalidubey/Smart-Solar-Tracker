from dataclasses import dataclass


@dataclass
class SimulationRecord:
    hour: int
    cloud_cover: int
    sunlight_intensity: float
    power: float
    energy: float
    motor_angle: float
    tracking_status: str
