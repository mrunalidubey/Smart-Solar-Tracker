
from flask import Flask, render_template, request

from backend.simulation.simulation_engine import SimulationEngine
from backend.analytics.energy_analysis import EnergyAnalysis
from backend.analytics.performance_comparison import PerformanceComparison
from backend.database.db_manager import DatabaseManager
from backend.database.models import SimulationRecord

app = Flask(__name__)

engine = SimulationEngine()
energy_analysis = EnergyAnalysis()
comparison = PerformanceComparison()
database = DatabaseManager()


@app.route("/")
def dashboard():
    hour = request.args.get("hour", default=12, type=int)
    cloud_cover = request.args.get("cloud", default=10, type=int)

    hour = max(6, min(hour, 18))
    cloud_cover = max(0, min(cloud_cover, 100))

    simulation = engine.run_simulation(
        hour=hour,
        cloud_cover=cloud_cover
    )

    daily = energy_analysis.analyze_day(
        cloud_cover=cloud_cover
    )

    comparison_data = comparison.compare(
        cloud_cover=cloud_cover
    )

    record = SimulationRecord(
        hour=hour,
        cloud_cover=cloud_cover,
        sunlight_intensity=simulation["sunlight"]["sunlight_intensity"],
        power=simulation["power"]["power"],
        energy=simulation["power"]["power"],
        motor_angle=simulation["motor"]["current_angle"],
        tracking_status=", ".join(simulation["tracking"]["movement"])
    )

    database.save_simulation(record)
    history = database.get_recent_simulations(10)

    return render_template(
        "index.html",
        simulation=simulation,
        daily=daily,
        comparison=comparison_data,
        selected_hour=hour,
        selected_cloud=cloud_cover,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
