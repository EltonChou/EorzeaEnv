# Changelog

## Unreleased
- Diamondust predictor.
- Aurora predictor.

## [2.2.3] - 2022-08-29
### Changed
- Refined type hint

## [2.2.2] - 2022-08-27
### Fixed
- Fixed WeatherRate data missing. (452d11b)

## [2.2.1] - 2022-08-26
### Changed
- `EorzeaTime.weather_period` accepts base timestamp. (a6cbb3e)
- Make `EorzeaRainbow` stricter. (22d015b)(c72a32b)
### Fixed
- Fixed `EorzeaRainbow` bug. (c72a32b)

## [2.2.0] - 2022-08-25
### Added
- Add patch 6.2 weather data. (14799ec)
- Add `EorzeaRainbow` to predict rainbow occurrence. (fead17f)(52d3829)
### Changed
- Refactor `EorzeaTime`, the behavior didn't change too much. (b20519c)
- Instance of `EorzeaTime` can compare to each other. (b20519c)
- Add argument in `EorzeaWeather.forecast` that can return weather index instead of weather name. (602da0c)
- `EorzeaWeather.weather_period` can generate infinite period with argument `step='inf'`. (42e9681)
- `timestamp` argument in `EorzeaWeather.forecast` accepts `EorzeaTime` instance.
### Deprecated
- float and int type of `timestamp` argument supporting in `EorzeaWeather.forecast` would be removed from 2.5.0.

## [2.1.0] - 2022-08-23
### Added
- Add python3.10 supporting
### Fixed
- Fix EorzeaWeather.forecast timestamp type issue.
- Fix EorzeaTime.weather_period timestamp type issue.
- Fix type hint.
### Removed
- **Discard python3.6 supporting.**
- **Discard python3.7 supporting.**

## [2.0.0] - 2022-05-30
### Added
- EorzeaPlaceName

## [1.5.2] - 2022-05-08
### Added
- 6.1 weather data

## [1.5.1] - 2021-12-04
### Removed
- Remove python 3.10 support

## [1.5.0] - 2021-12-04
### Added
- 6.0 weather data

## [1.4.6] - 2021-05-05
### Added
- 5.5 weather data

## [1.4.5] - 2021-01-15
### Added
- 5.4 weather data

## [1.4.4] - 2020-10-22
### Added
- EorzeaLang
- EorzeaWeather.forecast with overload

## [1.4.3] - 2020-10-20
### Added
- 5.35 weather data

## [1.4.1] - 2019-06-29
### Added
- 5.1 weather data

## [1.4.0] - 2019-06-29
### Added
- 5.0 weather data
### Deleted
- `EorzeaWeather.forecast_weather()`

## [1.3.0] - 2019-06-25
### Added
- forecast in EorzeaWeather
### Changed
- rewrite docstring
### Deprecated
- forecast_weather in EorzeaWeather is deprecated

