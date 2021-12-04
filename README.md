[![Pypi](https://img.shields.io/pypi/v/eorzeaenv.svg?style=flat-square)](https://pypi.org/project/EorzeaEnv/)
[![Pypi](https://img.shields.io/pypi/pyversions/eorzeaenv.svg?style=flat-square)](https://pypi.org/project/EorzeaEnv/)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FEltonChou%2FEorzeaEnv%2Fbadge&style=flat-square)](https://github.com/EltonChou/EorzeaEnv/actions)
![PyPI - Downloads](https://img.shields.io/pypi/dm/EorzeaEnv?style=flat-square)

# EorzeaEnv

+ [CHANGELOG](https://github.com/EltonChou/EorzeaEnv/blob/master/CHANGELOG.md)

## Installation
```
pip install EorzeaEnv
```

## Usage
```py
from EorzeaEnv import EorzeaLang
from EorzeaEnv import EorzeaTime
from EorzeaEnv import EorzeaWeather
```

### Eorzea Time

```sh
>>> EorzeaTime.now()
'EorzeaTime(Sixth Embral Moon, 11, 21, 56, Phase:0.50, Althyk)'

>>> EorzeaTime.now().moon
'Sixth Embral Moon'

>>> EorzeaTime.now().sun
11

>>> EorzeaTime.now().hour
21

>>> EorzeaTime.now().minute
56

>>> EorzeaTime.now().phase
0.50

>>> EorzeaTime.now().guardian
'Althyk'
```

### Weather Forecast
+ Using period as tuple or list
```python
# defalut step value is 5
# This method return a generator if you need to re-use it save the values as `tuple` or `list`.
t = tuple(EorzeaTime.weather_period(step=3))

# defalut lang is 'en'
# defalut strict is True for strict mode
# False for fuzzy mode: `adsfEureka Pyrosadsf` is valid
weather_en = EorzeaWeather.forecast('Eureka Pyros', t, strict=True)
weather_ja = EorzeaWeather.forecast('Eureka Pyros', t, lang=EorzeaLang.JA, strict=True)
weather_de = EorzeaWeather.forecast('Eureka Pyros', t, lang=EorzeaLang.DE, strict=True)
weather_fr = EorzeaWeather.forecast('Eureka Pyros', t, lang=EorzeaLang.FR, strict=True)
```
```sh
>>> print(weather_en)
['Thunder', 'Snow', 'Blizzards']

>>> print(weather_ja)
['雷', '雪', '吹雪']

>>> print(weather_de)
['Gewittrig', 'Schnee', 'Schneesturm']

>>> print(weather_fr)
['Orages', 'Neige', 'Blizzard']
```
+ Using period in for-loop
```py
weather_en = []
for t in EorzeaTime.weather_period(step=3):
    w = EorzeaWeather.forecast('Eureka Pyros', t)
    weather_en.append(w)
```
```sh
>>> print(weather_en)
['Thunder', 'Snow', 'Blizzards']
```
+ Using period generator directly
```py
weather = EorzeaWeather.forecast('Eureka Pyros', EorzeaTime.weather_period(step=3))
```
```sh
>>> print(weather_en)
['Thunder', 'Snow', 'Blizzards']
```
+ Also support float type
```py
weather = EorzeaWeather.forecast('Eureka Pyros', 1603644000.0)
```
```sh
>>> print(weather)
'Thunder'
```


## Thanks
- [Rogueadyn-SaintCoinach](https://github.com/Rogueadyn/SaintCoinach)
