import sqlite3
from pathlib import Path

from backend.database.models import SimulationRecord


DATABASE_PATH = Path(__file__).resolve().parents[2] / "data" / "solar_tracker.db"


class DatabaseManager:
    def __init__(self, db_path=DATABASE_PATH):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.create_table()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self.get_connection() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS simulations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    hour INTEGER NOT NULL,
                    cloud_cover INTEGER NOT NULL,
                    sunlight_intensity REAL,
                    power REAL,
                    energy REAL,
                    motor_angle REAL,
                    tracking_status TEXT
                )
            """)

    def save_simulation(self, record):
        if not isinstance(record, SimulationRecord):
            raise TypeError("record must be a SimulationRecord")

        with self.get_connection() as connection:
            cursor = connection.execute("""
                INSERT INTO simulations (
                    hour, cloud_cover, sunlight_intensity,
                    power, energy, motor_angle, tracking_status
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                record.hour, record.cloud_cover,
                record.sunlight_intensity, record.power,
                record.energy, record.motor_angle,
                record.tracking_status
            ))
            return cursor.lastrowid

    def get_recent_simulations(self, limit=10):
        with self.get_connection() as connection:
            cursor = connection.execute(
                "SELECT * FROM simulations ORDER BY id DESC LIMIT ?",
                (max(1, int(limit)),)
            )
            columns = [item[0] for item in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


if __name__ == "__main__":
    database = DatabaseManager()
    print("Database initialized successfully!")
    print("Database location:", database.db_path)
