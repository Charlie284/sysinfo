# sysinfo-cli

A cross-platform CLI tool that prints concise system information: OS and kernel
details, CPU cores and usage, RAM usage, root-disk usage, and system uptime —
one command, no flags.

## Features

- OS and kernel info (`platform.system()`, `platform.version()`, `platform.machine()`)
- CPU model, physical and logical core counts, and current usage (1-second sample)
- RAM total / used / available / percent (`psutil.virtual_memory()`)
- Root-filesystem disk total / used / free / percent (`shutil.disk_usage("/")`)
- System uptime derived from `psutil.boot_time()`

## Works on

- Linux
- macOS
- Windows

On Windows, disk usage is still sampled at the root path `/`, which resolves to
the current drive's root.

## Requirements

- Python 3.9+
- `psutil>=5.9,<8` (installed automatically by pip)

## Install

Clone the repository, then install the CLI and its declared `psutil` dependency:

```sh
python3 -m pip install .
```

This installs a `sysinfo` console script (`sysinfo:main`). Installing requires
`setuptools>=77` in the build environment; pip normally resolves this for you,
but on very old system Python installs it is easier to use a virtual
environment (see Development below).

## Run

```sh
sysinfo
```

You can also run `python3 sysinfo.py` from the repository after installation.

Example output:

```text
========================================
System Information
========================================
OS: Linux 6.8.0-1061-aws
OS Version: #64~22.04.1-Ubuntu SMP ...
Architecture: x86_64
Kernel: 6.8.0-1061-aws

CPU
----------------------------------------
Processor: x86_64
Physical cores: 2
Logical cores: 2
CPU usage: 2.0%

Memory
----------------------------------------
Total: 7.76 GB
Used: 1.19 GB
Available: 6.56 GB
Usage: 15.4%

Disk
----------------------------------------
Total: 123.87 GB
Used: 13.83 GB
Free: 110.02 GB
Usage: 11.2%

Uptime
----------------------------------------
0:01:42

Done.
```

## Notes

- `CPU usage` is a blocking 1-second sample (`psutil.cpu_percent(interval=1)`),
  so the command takes about a second to run.
- Byte values are reported in binary gigabytes (GiB) with two decimals.
- `Processor` may print `Unknown` on platforms where `platform.processor()`
  returns an empty string.
- Uptime is rendered with `datetime.timedelta`, so days appear as
  `N days, H:MM:SS`.

## Development

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e . ruff
python -m unittest discover -s tests -v
ruff check .
```

The project is a single module (`sysinfo.py`) packaged with setuptools via
`pyproject.toml`. Ruff is configured there too (`target-version = "py39"`).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).
