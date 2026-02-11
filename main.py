import asyncio
import os
import sys
from core.monitor import CPUMonitor, MemoryMonitor
from core.logger import DataLogger

# Color Constants
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


async def run_monitoring():
    cpu_task = CPUMonitor("CPU", 2)
    mem_task = MemoryMonitor("RAM", 2)
    logger = DataLogger()

    print("--- PyPulse Monitoring Started ---")

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            results = await asyncio.gather(
                cpu_task.collect(),
                mem_task.collect()
            )

            print("=========================================")
            print("        PYPULSE LIVE DASHBOARD           ")
            print("=========================================")

            for result in results:
                try:
                    percentage = float(result.split(": ")[1].replace("%", ""))
                    color = RED if percentage > 80 else GREEN
                except (IndexError, ValueError):
                    color = RESET 

                print(f"STATUS: {color}{result}{RESET}")

            print("=========================================")
            print("Action: Recording to logs/system_data.txt")
            print("Press Ctrl+C to Exit Safely")

            logger.log_data(results[0], results[1])
            await asyncio.sleep(2)

    except asyncio.CancelledError:
        pass


if __name__ == "__main__":
    try:
        asyncio.run(run_monitoring())
    except KeyboardInterrupt:
        print("\n[Shutting down...] Goodbye!")
        sys.exit(0)