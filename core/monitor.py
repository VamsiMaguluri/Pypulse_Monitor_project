import psutil
from abc import ABC, abstractmethod

class BaseMonitor(ABC):
    """Abstract Base Class: Every monitor must follow this structure."""
    def __init__(self, name, interval):
        self.name = name
        self.interval = interval

    @abstractmethod
    async def collect(self):
        """This must be overridden by subclasses."""
        pass

class CPUMonitor(BaseMonitor):
    """Monitors CPU usage percentage."""
    async def collect(self):

        usage = psutil.cpu_percent(interval=None)
        return f"[{self.name}] Usage: {usage}%"

class MemoryMonitor(BaseMonitor):
    """Monitors RAM usage percentage."""
    async def collect(self):
        mem = psutil.virtual_memory()
        return f"[{self.name}] Used: {mem.percent}%"