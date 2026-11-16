
class TrackingAlgorithm:

    def __init__(self, threshold=20):
        self.threshold = threshold

    def calculate_movement(self, sensors):

        top = (
            sensors["top_left"] +
            sensors["top_right"]
        ) / 2

        bottom = (
            sensors["bottom_left"] +
            sensors["bottom_right"]
        ) / 2

        left = (
            sensors["top_left"] +
            sensors["bottom_left"]
        ) / 2

        right = (
            sensors["top_right"] +
            sensors["bottom_right"]
        ) / 2

        vertical_difference = top - bottom
        horizontal_difference = left - right

        movement = []

        if abs(vertical_difference) > self.threshold:
            if vertical_difference > 0:
                movement.append("TILT DOWN")
            else:
                movement.append("TILT UP")

        if abs(horizontal_difference) > self.threshold:
            if horizontal_difference > 0:
                movement.append("ROTATE RIGHT")
            else:
                movement.append("ROTATE LEFT")

        if not movement:
            movement.append("PANEL ALIGNED")

        return {
            "vertical_difference": round(vertical_difference, 2),
            "horizontal_difference": round(horizontal_difference, 2),
            "movement": movement
        }


if __name__ == "__main__":

    tracker = TrackingAlgorithm()

    sensors = {
        "top_left": 850,
        "top_right": 700,
        "bottom_left": 600,
        "bottom_right": 550
    }

    result = tracker.calculate_movement(sensors)

    print("SOLAR TRACKING RESULT")
    print("---------------------")

    for key, value in result.items():
        print(f"{key}: {value}")
