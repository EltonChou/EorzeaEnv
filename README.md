# EorzeaEnv
## Installation
`pip install EorzeaEnv`

## Usage
```python
from EorzeaEnv import EorzeaWeather, EorzeaTime
```
### Time
```python
EorzeaTime.now() #EorzeaTime(13, 35)
EorzeaTime.now().hour #13
EorzeaTime.now().minute #35
```

### Forecast
```python
weather_list = []

for t in EorzeaTime.next_weather_period_start():
    weather = EorzeaWeather.forecast_weather("Eureka Pyros", t)
    weather_list.append(weather)

print(weather)
#['Heat Waves', 'Snow', 'Thunder', 'Thunder', 'Heat Waves']
```
## Thanks
- [Rogueadyn-SaintCoinach](https://github.com/Rogueadyn/SaintCoinach)