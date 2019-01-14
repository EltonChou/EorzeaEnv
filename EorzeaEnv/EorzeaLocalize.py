from EorzeaEnv.Data.WeatherLocalize import weather_localize as _wl


class EorzeaLocalize:

    @staticmethod
    def weather(weather, lang="en"):
        """lang: en, jp, fr, de"""
        return weather if lang is "en" else _wl[lang][weather]
