
class MotorSimulator:
    def __init__(self):
        self.current_angle = 0
        self.target_angle = 0
        self.rotation_speed = 10  # degrees per second

    def move_motor(self, movement, duration=1):
        if "ROTATE RIGHT" in movement:
            self.target_angle += 10
        elif "ROTATE LEFT" in movement:
            self.target_angle -= 10
        elif "TILT UP" in movement:
            self.target_angle += 5
        elif "TILT DOWN" in movement:
            self.target_angle -= 5

        self.target_angle = max(-60, min(60, self.target_angle))

        difference = self.target_angle - self.current_angle
        max_movement = self.rotation_speed * duration

        if abs(difference) <= max_movement:
            self.current_angle = self.target_angle
        else:
            self.current_angle += (
                max_movement if difference > 0 else -max_movement
            )

        response_time = (
            abs(self.target_angle - self.current_angle)
            / self.rotation_speed
        )

        return {
            "current_angle": round(self.current_angle, 2),
            "target_angle": round(self.target_angle, 2),
            "response_time": round(response_time, 2),
            "status": (
                "ALIGNED"
                if self.current_angle == self.target_angle
                else "MOVING"
            )
        }


if __name__ == "__main__":
    motor = MotorSimulator()

    result = motor.move_motor(["ROTATE RIGHT"])

    print("\nMOTOR SIMULATION")
    print("----------------")

    for key, value in result.items():
        print(f"{key}: {value}")
