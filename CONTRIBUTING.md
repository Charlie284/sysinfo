# Contributing

Thanks for your interest in improving sysinfo-cli.

## Set up

```sh
git clone https://github.com/Charlie284/sysinfo
cd sysinfo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e . ruff
```

## Test and lint

```sh
python -m unittest discover -s tests -v
ruff check .
```

Tests use `unittest` and `unittest.mock` to patch `psutil`/`shutil`, so they run
on any machine without depending on real system metrics. When you add behavior
to `sysinfo.py`, cover it the same way — patch the system call, assert on the
rendered output or the returned string.

Ruff is configured in `pyproject.toml` (`target-version = "py39"`); keep changes
compatible with Python 3.9.

## Style

- Keep the project a single top-level module unless a change genuinely needs
  more structure.
- Prefer stdlib facilities (`platform`, `shutil`, `datetime`) and `psutil` for
  system metrics; don't add new dependencies without discussion.
- Output formatting lives in `main()` — keep section headers and separators
  consistent with the existing style.

## Pull requests

Open a PR against `main` describing what changed and why. If it alters the
printed output, include before/after sample output in the description.
