# PyPulse: Real-Time System Monitor

PyPulse is a high-performance system monitoring tool built with **Python** using asynchronous programming. It tracks CPU and RAM usage in real-time, displays a live dashboard in the terminal, and logs data for future analysis.

## 🚀 Key Features
* **Asynchronous Concurrency:** Uses `asyncio` to monitor multiple system resources simultaneously without blocking the execution thread.
* **Object-Oriented Design:** Implements Abstract Base Classes (ABC) for modularity and easy extension of new monitors.
* **Persistent Logging:** Automatically records system health metrics to a timestamped log file.
* **Clean CLI UX:** Provides a self-refreshing terminal dashboard for a professional user experience.

## 🛠️ Tech Stack
* **Language:** Python 3.14
* **Libraries:** `psutil` (System metrics), `asyncio` (Concurrency)
* **Architecture:** Modular OOP (Object-Oriented Programming)

## 📂 Project Structure
- `main.py`: The entry point and asynchronous event loop.
- `core/monitor.py`: Contains the logic for resource data collection.
- `core/logger.py`: Manages file I/O and data persistence.
- `logs/`: Directory where system metrics are stored.

##  🚦How to Run
1. Clone the repository.
2. Install dependencies: `pip install psutil`
3. Run the application: `python main.py`