[![Pypi](https://img.shields.io/pypi/v/eorzeaenv.svg?style=flat-square)](https://pypi.org/project/EorzeaEnv/)
[![Pypi](https://img.shields.io/pypi/pyversions/eorzeaenv.svg?style=flat-square)](https://pypi.org/project/EorzeaEnv/)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FEltonChou%2FEorzeaEnv%2Fbadge&style=flat-square)](https://github.com/EltonChou/EorzeaEnv/actions)
![PyPI - Downloads](https://img.shields.io/pypi/dm/EorzeaEnv?style=flat-square)
![Coverage](https://img.shields.io/codecov/c/github/EltonChou/EorzeaEnv?style=flat-square)

# EorzeaEnv

+ [CHANGELOG](https://github.com/EltonChou/EorzeaEnv/blob/master/CHANGELOG.md)

## Installation
```
pip install eorzeaenv
```

## Usage
```py
from EorzeaEnv import EorzeaLang, EorzeaTime, EorzeaWeather, EorzeaPlaceName
```

### Eorzea Language enum
```py
support_langs = [
    EorzeaLang.EN,
    EorzeaLang.JA,
    EorzeaLang.DE,
    EorzeaLang.FR,
    EorzeaLang.ZH_SC,
    EorzeaLang.KO,
]
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
+ Get the unix timestamp (int not float)
```sh
>>> EorzeaTime.now().get_unix_time()
1661114514
```
+ Get the eorzea timestamp (int not float)
```sh
>>> EorzeaTime.now().get_eorzea_time()
34177649220
```

### Weather Forecast
+ Using period as tuple or list
```python
# defalut step value is 5
# This method return a generator if you need to re-use it save the values as `tuple` or `list`.
t = tuple(EorzeaTime.weather_period(step=3))

# Use EorzeaPlaceName to ensure the place is valid or
# you can directly pass the place string to forecast.
place_name = EorzeaPlaceName('Eureka Pyros')

# Defalut lang is 'en'
# Defalut strict is `True` for strict mode `False` for fuzzy mode.
# eg. `eurekaa puros` is valid in fuzzy mode.

# In fuzzy mode, you can set the cutoff score to prevent unexpected place name to be passed.
# default value is 80. (100 >= value >= 0)
EorzeaWeather.set_fuzzy_cutoff(95)

weather_en = EorzeaWeather.forecast(place_name, t, strict=True)
weather_ja = EorzeaWeather.forecast(place_name, t, lang=EorzeaLang.JA, strict=True)
weather_de = EorzeaWeather.forecast(place_name, t, lang=EorzeaLang.DE, strict=True)
weather_fr = EorzeaWeather.forecast(place_name, t, lang=EorzeaLang.FR, strict=True)
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
+ Provide a desired base time to calculate.
```py
for t in EorzeaTime.weather_period(step=3, from_=datetime(2025, 10, 25).timestamp()):
    w = EorzeaWeather.forecast('Eureka Pyros', t)
    print(w)
```
+ Using period generator directly
```py
weather = EorzeaWeather.forecast('Eureka Pyros', EorzeaTime.weather_period(step=3))
```
```sh
>>> print(weather_en)
['Thunder', 'Snow', 'Blizzards']
```

### Eorzea place name

An instance of EorzeaPlaceName would be always a valid place name in this pacakge.

An invalid place name will raises `InvalidEorzeaPlaceName` error.

```py
place_name = EorzeaPlaceName(
    'The Ruby Sea',
    # `False` to fuzzy mode, default is `True`
    strict=True,
    # Stricted scope for validation of place name.
    # default is all supports locale.
    locale_scopes=[
        EorzeaLang.EN,
        EorzeaLang.JA,
        EorzeaLang.FR,
        EorzeaLang.DE],
    # Used in fuzzy mode to cut-off the result under the score.
    # default is `80`.
    fuzzy_cutoff=80
)
```
```sh
>>> place_name
EorrzeaPlaceName('The Ruby Sea')

>>> print(place_name)
'The Ruby Sea`
```

Belowings are valid place names in strict mode with full locale scopes (default settings).
```py
EorzeaPlaceName('The Ruby Sea') # valid `The Ruby Sea`
EorzeaPlaceName('the ruby sea') # valid `The Ruby Sea`
EorzeaPlaceName('ruby sea') # valid `The Ruby Sea`
EorzeaPlaceName('rubinsee') # valid `Rubinsee`
EorzeaPlaceName('紅玉海') # valid `紅玉海`
```

With stricted scopes.
```py
scopes = [EorzeaLang.JA, EorzeaLang.DE]

EorzeaPlaceName('The Ruby Sea', locale_scopes=scopes) # raises error
EorzeaPlaceName('the ruby sea', locale_scopes=scopes) # raises error
EorzeaPlaceName('ruby sea', locale_scopes=scopes) # raises error
EorzeaPlaceName('rubinsee', locale_scopes=scopes) # valid `Rubinsee`
EorzeaPlaceName('紅玉海', locale_scopes=scopes) # valid `紅玉海`
```

In fuzzy mode.
```py
EorzeaPlaceName('the ruby see', strict=False) # valid `The Ruby Sea`
EorzeaPlaceName('ruby see', strict=False) # valid `The Ruby Sea`
EorzeaPlaceName('rubisee', strict=False) # valid `Rubinsee`
EorzeaPlaceName('紅玉貝', strict=False) # raises error
EorzeaPlaceName('紅玉貝', strict=False, fuzzy_cutoff=66) # valid `紅玉海`
```

### Eorzea rainbow predict

Use EorzeaRainbow to predict when will the rainbow appears.

```py
from datetime import datetime

from EorzeaEnv import EorzeaPlaceName, EorzeaRainbow, EorzeaTime, EorzeaWeather

rainbow_times: list[datetime] = []

place = EorzeaPlaceName("東ラノシア")
the_rainbow = EorzeaRainbow(place_name=place)


for t in EorzeaTime.weather_period(step='inf'):
    the_rainbow.append(t, EorzeaWeather.forecast(place, t, raw=True))
    if the_rainbow.is_appear:
        rainbow_times.append(datetime.fromtimestamp(t))
    if len(rainbow_times) == 20:
        break

print(rainbow_times)
```

### Errors
```py
from EorzeaEnv.errors import \
    EorzeaEnvError, \
    InvalidEorzeaPlaceName, \
    WeatherRateDataError
```

```
Exception
    |- EorzeaEnvError
        |- InvalidEorzeaPlaceName
        |- WeatherRateDataError
```

## Thanks
- [Rogueadyn-SaintCoinach](https://github.com/Rogueadyn/SaintCoinach)
