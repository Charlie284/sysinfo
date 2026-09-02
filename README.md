# sysinfo-cli

A cross-platform CLI tool that prints system information.

## Features
- OS and kernel info
- CPU cores and usage
- RAM usage
- Disk usage
- System uptime

## Works on
- Linux
- macOS
- Windows

## Requirements
- Python 3.9+

## Install

Clone the repository, then install the CLI and its declared `psutil` dependency:

```sh
python3 -m pip install .
```

## Run

```sh
sysinfo
```

You can also run `python3 sysinfo.py` from the repository after installation.

## Development

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e . ruff
python -m unittest discover -s tests -v
ruff check .
```
