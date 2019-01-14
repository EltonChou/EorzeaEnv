from EorzeaEnv.Data.WeatherLocalize import weather_localize as _wl


class EorzeaLocalize:

    @staticmethod
    def weather(weather, lang="en"):
        """lang: en, jp, fr, de"""
        if lang is "en":
            return weather
        return _wl[lang][weather]
