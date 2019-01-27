
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
weather_en = []
weather_jp = []
weather_de = []
weather_fr = []

# defalut step value is 5
for t in EorzeaTime.weather_period(step=3):
    # defalut lang is 'en'
    w_en = EorzeaWeather.forecast_weather('Eureka Pyros', t)
    w_jp = EorzeaWeather.forecast_weather('Eureka Pyros', t, lang='jp')
    w_de = EorzeaWeather.forecast_weather('Eureka Pyros', t, lang='de')
    w_fr = EorzeaWeather.forecast_weather('Eureka Pyros', t, lang='fr')
    weather_en.append(w_en)
    weather_jp.append(w_jp)
    weather_de.append(w_de)
    weather_fr.append(w_fr)
```


```sh
>>> print(weather_en)
['Thunder', 'Snow', 'Blizzards']

>>> print(weather_jp)
['雷', '雪', '吹雪']

>>> print(weather_de)
['Gewittrig', 'Schnee', 'Schneesturm']

>>> print(weather_fr)
['Orages', 'Neige', 'Blizzard']
```
## Thanks
- [Rogueadyn-SaintCoinach](https://github.com/Rogueadyn/SaintCoinach)
