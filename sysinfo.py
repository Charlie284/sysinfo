import platform
import shutil
import time
from datetime import timedelta

import psutil


def bytes_to_gb(value):
    return f"{value / (1024 ** 3):.2f} GB"


def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return str(timedelta(seconds=int(uptime_seconds)))


def main():
    print("=" * 40)
    print("System Information")
    print("=" * 40)

    # OS info
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"OS Version: {platform.version()}")
    print(f"Architecture: {platform.machine()}")

    # Kernel
    print(f"Kernel: {platform.uname().release}")

    print("\nCPU")
    print("-" * 40)
    print(f"Processor: {platform.processor() or 'Unknown'}")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Logical cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")

    print("\nMemory")
    print("-" * 40)
    mem = psutil.virtual_memory()
    print(f"Total: {bytes_to_gb(mem.total)}")
    print(f"Used: {bytes_to_gb(mem.used)}")
    print(f"Available: {bytes_to_gb(mem.available)}")
    print(f"Usage: {mem.percent}%")

    print("\nDisk")
    print("-" * 40)
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {bytes_to_gb(total)}")
    print(f"Used: {bytes_to_gb(used)}")
    print(f"Free: {bytes_to_gb(free)}")
    print(f"Usage: {used / total * 100:.1f}%")

    print("\nUptime")
    print("-" * 40)
    print(get_uptime())

    print("\nDone.")


if __name__ == "__main__":
    main()
