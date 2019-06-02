[![Pypi](https://img.shields.io/pypi/v/eorzeaenv.svg?style=flat-square)](https://pypi.org/project/EorzeaEnv/)
[![Pypi](https://img.shields.io/pypi/pyversions/eorzeaenv.svg?style=flat-square)](https://pypi.org/project/EorzeaEnv/)
![Build Status](https://img.shields.io/travis/EltonChou/EorzeaEnv.svg?style=flat-square)

# EorzeaEnv
## Installation
```
pip install EorzeaEnv
```

## Usage
```py
from EorzeaEnv import EorzeaTime
from EorzeaEnv import EorzeaWeather
```

### Eorzea Time

```sh
>>> EorzeaTime.now()
'EorzeaTime(Sixth Embral Moon, 11, 21, 56, 0.50, Althyk)'

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
```python
# defalut step value is 5
t = EorzeaTime.weather_period(step=3)

# defalut lang is 'en'
# defalut strict is True
weather_en = EorzeaWeather.forecast('Eureka Pyros', t, strict=True)
weather_jp = EorzeaWeather.forecast('Eureka Pyros', t, lang='ja', strict=True)
weather_de = EorzeaWeather.forecast('Eureka Pyros', t, lang='de', strict=True)
weather_fr = EorzeaWeather.forecast('Eureka Pyros', t, lang='fr', strict=True)
```
or
```py
weather_en = []
for t in EorzeaTime.weather_period(step=3):
    w = EorzeaWeather.forecast('Eureka Pyros', t)
    weather_en.append(w)
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
## Thanks
- [Rogueadyn-SaintCoinach](https://github.com/Rogueadyn/SaintCoinach)
