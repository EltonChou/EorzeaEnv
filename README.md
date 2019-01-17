
[![Pypi](https://img.shields.io/pypi/v/eorzeaenv.svg?style=flat-square)](https://pypi.org/project/EorzeaEnv/)
[![Pypi](https://img.shields.io/pypi/pyversions/eorzeaenv.svg?style=flat-square)](https://pypi.org/project/EorzeaEnv/)
[![Build Status](https://travis-ci.org/EltonChou/EorzeaEnv.svg?branch=1.2.0)](https://travis-ci.org/EltonChou/EorzeaEnv)

# EorzeaEnv
## Installation
```
pip install EorzeaEnv
```

## Usage
```python
from EorzeaEnv.EorzeaTime import EorzeaTime
from EorzeaEnv.EorzeaWeather import EorzeaWeather
from EorzeaEnv.EorzeaLocalize import EorzeaLocalize
```

### Eorzea Time

```python
EorzeaTime.now() #EorzeaTime(Sixth Embral Moon, 11, 21, 56, 0.50, Althyk)
EorzeaTime.now().moon #Sixth Embral Moon
EorzeaTime.now().sun #11
EorzeaTime.now().hour #21
EorzeaTime.now().minute #56
EorzeaTime.now().phase #0.50
EorzeaTime.now().guardian #Althyk
```

### Weather Forecast
```python
weather_list = []

for t in EorzeaTime.weather_period():
    weather = EorzeaWeather.forecast_weather("Eureka Pyros", t)
    weather_list.append(weather)

print(weather_list)
#['Heat Waves', 'Snow', 'Thunder', 'Thunder', 'Heat Waves']
```
## Thanks
- [Rogueadyn-SaintCoinach](https://github.com/Rogueadyn/SaintCoinach)
