import contextlib
import io
import unittest
from unittest.mock import patch

import sysinfo


class SysinfoTests(unittest.TestCase):
    def test_bytes_to_gb_formats_binary_gigabytes(self):
        self.assertEqual(sysinfo.bytes_to_gb(3 * 1024**3), "3.00 GB")

    @patch("sysinfo.time.time", return_value=100_000)
    @patch("sysinfo.psutil.boot_time", return_value=96_339)
    def test_uptime_uses_the_system_boot_time(self, _boot_time, _time):
        self.assertEqual(sysinfo.get_uptime(), "1:01:01")

    @patch("sysinfo.get_uptime", return_value="1 day, 2:03:04")
    @patch("sysinfo.shutil.disk_usage", return_value=(1000, 400, 600))
    @patch("sysinfo.psutil.virtual_memory")
    @patch("sysinfo.psutil.cpu_percent", return_value=12.5)
    @patch("sysinfo.psutil.cpu_count", side_effect=[4, 8])
    def test_main_prints_each_system_information_section(
        self,
        _cpu_count,
        _cpu_percent,
        virtual_memory,
        _disk_usage,
        _uptime,
    ):
        virtual_memory.return_value = type(
            "Memory",
            (),
            {"total": 1000, "used": 400, "available": 600, "percent": 40.0},
        )()

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            sysinfo.main()

        rendered = output.getvalue()
        for heading in ("System Information", "CPU", "Memory", "Disk", "Uptime"):
            self.assertIn(heading, rendered)
        self.assertIn("Physical cores: 4", rendered)
        self.assertIn("Logical cores: 8", rendered)
        self.assertIn("CPU usage: 12.5%", rendered)
        self.assertIn("Usage: 40.0%", rendered)
        self.assertIn("1 day, 2:03:04", rendered)


if __name__ == "__main__":
    unittest.main()
