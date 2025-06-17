
from pyswisseph import swe, swe_set_ephe_path, swe_calc_ut
import swisseph as swe
import math
from datetime import datetime

ASPECTS = {
    "Conjunction": 0,
    "Opposition": 180,
    "Trine": 120,
    "Square": 90,
    "Sextile": 60
}

ORBS = {
    "Conjunction": 8,
    "Opposition": 8,
    "Trine": 7,
    "Square": 6,
    "Sextile": 6
}

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Uranus": swe.URANUS,
    "Neptune": swe.NEPTUNE,
    "Pluto": swe.PLUTO
}

def get_julian_day(date_str, time_str):
    year, month, day = map(int, date_str.split("-"))
    hour, minute = map(int, time_str.split(":"))
    return swe.julday(year, month, day, hour + minute / 60.0)

def calculate_aspects(jd, lat, lon):
    positions = {}
    for name, planet_id in PLANETS.items():
        pos, _ = swe.calc_ut(jd, planet_id)
        positions[name] = pos[0]

    aspects = {}
    for planet1, pos1 in positions.items():
        aspects[planet1] = []
        for planet2, pos2 in positions.items():
            if planet1 == planet2:
                continue
            angle = abs(pos1 - pos2)
            if angle > 180:
                angle = 360 - angle
            for aspect_name, aspect_angle in ASPECTS.items():
                if abs(angle - aspect_angle) <= ORBS[aspect_name]:
                    aspects[planet1].append({
                        "planet": planet2,
                        "aspect": aspect_name,
                        "orb": round(abs(angle - aspect_angle), 2)
                    })
    return aspects


def run_aspect_calc(birth_date, birth_time, lat, lon, timezone):
    planet_positions = get_planet_positions(birth_date, birth_time, lat, lon, timezone)
    aspects = calculate_aspects(planet_positions)
    return {
        "positions": planet_positions,
        "aspects": aspects
    }
