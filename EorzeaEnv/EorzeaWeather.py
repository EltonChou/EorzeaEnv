from numpy import uint32
from datetime import datetime as _dt
import json


class EorzeaWeather:
    def __init__(self):
        self.__fieldRates = {
            "Limsa Lominsa": [20, 50, 80, 90, 100],
            "Middle La Noscea": [20, 50, 70, 80, 90, 100],
            "Lower La Noscea": [20, 50, 70, 80, 90, 100],
            "Eastern La Noscea": [5, 50, 80, 90, 95, 100],
            "Western La Noscea": [10, 40, 60, 80, 90, 100],
            "Upper La Noscea": [30, 50, 70, 80, 90, 100],
            "Outer La Noscea": [30, 50, 70, 85, 100],
            "The Mist": [20, 50, 70, 80, 90, 100],
            "Gridania": [5, 20, 30, 40, 55, 85, 100],
            "Central Shroud": [5, 20, 30, 40, 55, 85, 100],
            "East Shroud": [5, 20, 30, 40, 55, 85, 100],
            "South Shroud": [5, 10, 25, 30, 40, 70, 100],
            "North Shroud": [5, 10, 25, 30, 40, 70, 100],
            "The Lavender Beds": [5, 20, 30, 40, 55, 85, 100],
            "Ul'dah": [40, 60, 85, 95, 100],
            "Western Thanalan": [40, 60, 85, 95, 100],
            "Central Thanalan": [15, 55, 75, 85, 95, 100],
            "Eastern Thanalan": [40, 60, 70, 80, 85, 100],
            "Southern Thanalan": [20, 60, 80, 90, 100],
            "Northern Thanalan": [5, 20, 50, 100],
            "The Goblet": [40, 60, 85, 95, 100],
            "Ishgard": [60, 70, 75, 90, 100],
            "Coerthas Central Highlands": [20, 60, 70, 75, 90, 100],
            "Coerthas Western Highlands": [20, 60, 70, 75, 90, 100],
            "The Sea of Clouds": [30, 60, 70, 80, 90, 100],
            "Azys Lla": [35, 70, 100],
            "The Diadem": [30, 60, 90, 100],
            "Idyllshire": [10, 20, 30, 40, 70, 100],
            "The Dravanian Forelands": [10, 20, 30, 40, 70, 100],
            "The Dravanian Hinterlands": [10, 20, 30, 40, 70, 100],
            "The Churning Mists": [10, 20, 40, 70, 100],
            "Mor Dhona": [15, 30, 60, 75, 100],
            "Rhalgr's Reach": [15, 60, 80, 90, 100],
            "The Fringes": [15, 60, 80, 90, 100],
            "The Peaks": [10, 60, 75, 85, 95, 100],
            "The Lochs": [20, 60, 80, 90, 100],
            "Kugane": [10, 20, 40, 80, 100],
            "Shirogane": [10, 20, 40, 80, 100],
            "The Ruby Sea": [10, 20, 35, 75, 100],
            "Yanxia": [5, 15, 25, 40, 80, 100],
            "The Azim Steppe": [5, 10, 17, 25, 35, 75, 100],
            "Eureka Anemos": [30, 60, 90, 100],
            "Eureka Pagos": [10, 28, 46, 64, 82, 100],
            "Eureka Pyros": [10, 28, 46, 64, 82, 100]
        }
        self.__fieldWeathers = {
            "Limsa Lominsa": ["Clouds", "Clear Skies", "Fair Skies", "Fog", "Rain"],
            "Middle La Noscea": ["Clouds", "Clear Skies", "Fair Skies", "Wind", "Fog", "Rain"],
            "Lower La Noscea": ["Clouds", "Clear Skies", "Fair Skies", "Wind", "Fog", "Rain"],
            "Eastern La Noscea": ["Fog", "Clear Skies", "Fair Skies", "Clouds", "Rain", "Showers"],
            "Western La Noscea": ["Fog", "Clear Skies", "Fair Skies", "Clouds", "Wind", "Gales"],
            "Upper La Noscea": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Thunder", "Thunderstorms"],
            "Outer La Noscea": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Rain"],
            "The Mist": ["Clouds", "Clear Skies", "Fair Skies", "Fair Skies", "Fog", "Rain"],
            "Gridania": ["Rain", "Rain", "Fog", "Clouds", "Fair Skies", "Clear Skies", "Fair Skies"],
            "Central Shroud": ["Thunder", "Rain", "Fog", "Clouds", "Fair Skies", "Clear Skies", "Fair Skies"],
            "East Shroud": ["Thunder", "Rain", "Fog", "Clouds", "Fair Skies", "Clear Skies", "Fair Skies"],
            "South Shroud": ["Fog", "Thunderstorms", "Thunder", "Fog", "Clouds", "Fair Skies", "Clear Skies"],
            "North Shroud": ["Fog", "Showers", "Rain", "Fog", "Clouds", "Fair Skies", "Clear Skies"],
            "The Lavender Beds": ["Clouds", "Rain", "Fog", "Clouds", "Fair Skies", "Clear Skies", "Fair Skies"],
            "Ul'dah": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Rain"],
            "Western Thanalan": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Rain"],
            "Central Thanalan": ["Dust Storms", "Clear Skies", "Fair Skies", "Clouds", "Fog", "Rain"],
            "Eastern Thanalan": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Rain", "Showers"],
            "Southern Thanalan": ["Heat Waves", "Clear Skies", "Fair Skies", "Clouds", "Fog"],
            "Northern Thanalan": ["Clear Skies", "Fair Skies", "Clouds", "Fog"],
            "The Goblet": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Rain"],
            "Ishgard": ["Snow", "Fair Skies", "Clear Skies", "Clouds", "Fog"],
            "Coerthas Central Highlands": ["Blizzards", "Snow", "Fair Skies", "Clear Skies", "Clouds", "Fog"],
            "Coerthas Western Highlands": ["Blizzards", "Snow", "Fair Skies", "Clear Skies", "Clouds", "Fog"],
            "The Sea of Clouds": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Wind", "Umbral Wind"],
            "Azys Lla": ["Fair Skies", "Clouds", "Thunder"],
            "The Diadem": ["Fair Skies", "Fog", "Wind", "Umbral Wind"],
            "Idyllshire": ["Clouds", "Fog", "Rain", "Showers", "Clear Skies", "Fair Skies"],
            "The Dravanian Forelands": ["Clouds", "Fog", "Thunder", "Dust Storms", "Clear Skies", "Fair Skies"],
            "The Dravanian Hinterlands": ["Clouds", "Fog", "Rain", "Showers", "Clear Skies", "Fair Skies"],
            "The Churning Mists": ["Clouds", "Gales", "Umbral Static", "Clear Skies", "Fair Skies"],
            "Mor Dhona": ["Clouds", "Fog", "Gloom", "Clear Skies", "Fair Skies"],
            "Rhalgr's Reach": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Thunder"],
            "The Fringes": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Thunder"],
            "The Peaks": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Wind", "Dust Storms"],
            "The Lochs": ["Clear Skies", "Fair Skies", "Clouds", "Fog", "Thunderstorms"],
            "Kugane": ["Rain", "Fog", "Clouds", "Fair Skies", "Clear Skies"],
            "Shirogane": ["Rain", "Fog", "Clouds", "Fair Skies", "Clear Skies"],
            "The Ruby Sea": ["Thunder", "Wind", "Clouds", "Fair Skies", "Clear Skies"],
            "Yanxia": ["Showers", "Rain", "Fog", "Clouds", "Fair Skies", "Clear Skies"],
            "The Azim Steppe": ["Gales", "Wind", "Rain", "Fog", "Clouds", "Fair Skies", "Clear Skies"],
            "Eureka Anemos": ["Fair Skies", "Gales", "Showers", "Snow"],
            "Eureka Pagos": ["Clear Skies", "Fog", "Heat Waves", "Snow", "Thunder", "Blizzards"],
            "Eureka Pyros": ["Fair Skies", "Heat Waves", "Thunder", "Blizzards", "Umbral Wind", "Snow"]
        }

    @property
    def field(self):
        return self.__fieldWeathers.keys()

    def forecast_weather(self, field, local_time_stamp=None):
        field_rates = self.__fieldRates[field]
        if not local_time_stamp:
            target = self._calculate_forecast_target(_dt.now().timestamp())
        else:
            target = self._calculate_forecast_target(local_time_stamp)

        for rate in field_rates:
            if target < rate:
                index = field_rates.index(rate)
                return self.__fieldWeathers[field][index]

    def _calculate_forecast_target(self, local_time_stamp=None):
        '''
        Thanks to Rogueadyn's SaintCoinach library for this calculation.
        '''
        bell = local_time_stamp / 175
        # Do the magic 'cause for calculations
        # 16:00 is 0, 00:00 is 8 and 08:00 is 16
        increment = uint32(bell + 8 - (bell % 8)) % 24
        # Take Eorzea days since unix epoch
        total_days = uint32(local_time_stamp / 4200)
        calc_base = total_days * 0x64 + increment
        step1 = uint32(calc_base << 0xB) ^ calc_base
        step2 = (step1 >> 8) ^ step1
        return int(step2 % 100)
