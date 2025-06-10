import swisseph as swe
import datetime

swe.set_ephe_path('.')  # or local path to ephemeris data

def calculate_birth_chart(birth_date, birth_time, lat, lon):
    year, month, day = map(int, birth_date.split("-"))
    hour, minute = map(int, birth_time.split(":"))
    ut = hour + minute / 60.0
    jd = swe.julday(year, month, day, ut)

    planets = {
        'Sun': swe.SUN,
        'Moon': swe.MOON,
        'Mercury': swe.MERCURY,
        'Venus': swe.VENUS,
        'Mars': swe.MARS,
        'Jupiter': swe.JUPITER,
        'Saturn': swe.SATURN,
        'Uranus': swe.URANUS,
        'Neptune': swe.NEPTUNE,
        'Pluto': swe.PLUTO,
        'True Node': swe.TRUE_NODE
    }

    result = {}
    for name, planet in planets.items():
        lon, lat_, dist, speed = swe.calc_ut(jd, planet)
        sign_index = int(lon // 30)
        degree = lon % 30
        sign = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces'][sign_index]
        result[name] = {
            "sign": sign,
            "degree": f"{degree:.2f}°"
        }

    # Ascendant and Houses
    hsys = 'P'  # Placidus
    _, ascmc, _, cusps = swe.houses(jd, lat, lon, hsys)
    result["Ascendant"] = {
        "degree": f"{ascmc[0]:.2f}°"
    }
    result["House Cusps"] = {f"House {i+1}": f"{c:.2f}°" for i, c in enumerate(cusps)}

    return result