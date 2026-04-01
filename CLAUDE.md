# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

EorzeaEnv is a Python library for Final Fantasy XIV in-game time and weather calculations. It provides tools to convert Unix timestamps to Eorzea time, forecast weather by location, and predict special weather events (rainbows, etc.).

## Commands

```bash
# Install dependencies
poetry install

# Run tests with coverage
make cov-test

# Run a single test file
pytest test/test_forecast.py -v

# Run a single test
pytest test/test_forecast.py::test_function_name -v

# Lint and format (ruff)
tox -e lint       # ruff format --check + ruff check
tox -e type       # mypy

# Run all environments (clean → py3.x matrix → lint → type → cov-report)
tox

# Run a specific tox environment
tox -e py311
tox -e lint
tox -e type
tox -e cov-report  # combine .coverage.* files and generate HTML report
tox -e clean       # erase all coverage data

# After changing version in pyproject.toml, sync to __init__.py
make update-version

# Update requirements files
make freeze
```

## Architecture

Five public classes exported from `EorzeaEnv/__init__.py`:

- **`EorzeaTime`** — Converts Unix timestamps to Eorzea in-game time using the constant `3600.0 / 175.0`. Exposes properties like `bell`, `sun`, `moon`, `phase`, and supports comparison operators. `now()` returns a cached current Eorzea time. `weather_period()` is a generator yielding 8-bell intervals used for weather forecasting.

- **`EorzeaWeather`** — Forecasts weather for a location at a given time. Accepts single timestamps or iterables, and either `EorzeaTime` or Unix floats. Uses the Rogueadyn SaintCoinach algorithm against lookup tables in `EorzeaEnv/Data/`.

- **`EorzeaPlaceName`** — Validates and normalizes FFXIV location names. Two modes: strict (exact match) or fuzzy (RapidFuzz, default cutoff 80). Raises `InvalidEorzeaPlaceName` on failure. Stores an internal index used by `EorzeaWeather` lookups.

- **`EorzeaLang`** — Enum of supported locales: `EN`, `JA`, `DE`, `FR`, `KO`, `ZH_SC`, `ZH_TC`.

- **`EorzeaRainbow`** — Predicts rainbow appearances. Tracks a 2-slot weather history (deque); rainbows appear when rainy weather (indices 7, 8, 10) transitions to clear during sun phases 27–32 or 1–6.

### Data Layer (`EorzeaEnv/Data/`)

- `PlaceName.py` — Large multilingual lookup dict (~302KB) mapping place names across all 7 locales.
- `WeatherRate.py` — Cumulative probability tables for weather by territory.
- `TerritoryWeather.py` — Maps territory indices to weather rate indices.
- `Weather.py` — Multilingual weather type name translations.

### Error Hierarchy

```
EorzeaEnvError
├── InvalidEorzeaPlaceName (also ValueError)
└── WeatherRateDataError
```

## Development Notes

- Python 3.8–3.14 supported; numpy version differs by Python version (1.19+ for 3.8–3.11, 2.0+ for 3.12+).
- `tox.toml` defines environments per Python version plus `lint`, `type`, `cov-report`, and `clean`. In CI, `tox-gh` (≥1.2) maps each runner's Python version to a subset of envs via the `[gh]` table — Python 3.11 additionally runs `lint` and `type`; all legs run `gh-cov-report` (XML) for Codecov upload.
- `utils/sync_version.py` reads version from `pyproject.toml` and writes it to `EorzeaEnv/__init__.py`.
- Unreleased features in CHANGELOG: Diamondust and Aurora predictors (similar pattern to `EorzeaRainbow`).
