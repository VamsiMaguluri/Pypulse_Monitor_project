import unittest
import asyncio
from core.monitor import CPUMonitor

class TestMonitors(unittest.TestCase):
    def test_cpu_monitor_init(self):
        """Test if the monitor initializes with the correct name."""
        monitor = CPUMonitor("TestCPU", 1)
        self.assertEqual(monitor.name, "TestCPU")

    def test_cpu_collect_type(self):
        """Test if the collect method returns a string."""
        monitor = CPUMonitor("TestCPU", 1)
        result = asyncio.run(monitor.collect())
        self.assertIsInstance(result, str)
        self.assertIn("Usage", result)

if __name__ == '__main__':
    unittest.main()