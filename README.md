# ☀️ Smart Solar Tracker

A Python-based solar tracking simulation and analytics dashboard that models sunlight conditions, virtual sensors, panel movement, and energy generation.

## 🚀 Project Overview

Smart Solar Tracker is a software-based simulation project designed to demonstrate how an automated solar tracking system can respond to changing sunlight conditions and estimate energy performance.

It includes a Flask web dashboard with interactive controls, visualizations, and performance analytics.

## ✨ Features

- **Solar Simulation:** Simulates sunlight intensity, sun elevation, and azimuth.
- **Virtual LDR Sensors:** Generates readings from four virtual light sensors.
- **Tracking Algorithm:** Calculates the direction of panel movement.
- **Motor Simulation:** Models panel movement and motor status.
- **Power Calculation:** Estimates voltage, current, and generated power.
- **Energy Analytics:** Calculates daily energy estimates and peak generation.
- **Performance Comparison:** Compares fixed and tracking panel estimates.
- **Interactive Dashboard:** Displays simulation results and charts.

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Chart.js
- SQLite (database module)

## 📂 Project Structure

```text
SmartSolarTracker/
├── app.py
├── config.py
├── requirements.txt
├── backend/
│   ├── algorithms/
│   ├── analytics/
│   ├── database/
│   └── simulation/
├── templates/
├── static/
│   ├── css/
│   └── js/
├── data/
└── tests/
```

## ⚙️ Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/mrunalidubey/Smart-Solar-Tracker.git
```

2. Navigate to the project directory:

```bash
cd Smart-Solar-Tracker
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python3 app.py
```

5. Open in your browser:

```text
http://127.0.0.1:5001
```

## 📊 Dashboard Modules

- Simulation Controls
- Virtual Solar Panel Visualization
- Power Overview
- LDR Sensor Readings
- Tracking Status
- Motor Simulation Status
- Fixed vs Tracking Comparison
- Energy Analytics
- Interactive Performance Charts

## ⚠️ Project Scope

This is a software-only simulation. No physical solar panels, motors, or sensors are connected.

Sensor readings, motor movements, and energy performance are simulated estimates based on simplified mathematical models. The fixed-panel comparison uses an assumed irradiance factor.

## 🎯 Objective

To explore solar tracking concepts, simulation logic, energy calculations, and data visualization through a modular Python application.

## 👩‍💻 Author

**Mr​​unali Dubey**

B.Tech Computer Science and Engineering — AI & Data Science

[GitHub Profile](https://github.com/mrunalidubey)

---

*Built as an academic and portfolio project.*