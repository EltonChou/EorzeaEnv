from enum import Enum

from .eorzea_time import EorzeaTime
from .eorzea_weather import EorzeaWeather


__title__ = 'EorzeaEnv'
__author__ = 'Elton H.Y. Chou'
__license__ = 'MIT'
__version__ = '1.4.5'


class EorzeaLang(str, Enum):
    EN = "en"
    JA = "ja"
    DE = "de"
    FR = "fr"