import asyncio
import os
import sys
from core.monitor import CPUMonitor, MemoryMonitor
from core.logger import DataLogger


async def run_monitoring():
    # Initialize our objects
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
            print(f"STATUS: {results[0]}")
            print(f"STATUS: {results[1]}")
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
        print("\n[Shutting down...] Session logs saved. Goodbye!")
        sys.exit(0)