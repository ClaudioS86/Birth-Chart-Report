import swisseph as swe

# Imposta il percorso degli efemeridi
swe.set_ephe_path('.')

def calculate_birth_chart(birth_date, birth_time, lat, lon):
    # Converte la data e ora in tempo universale
    year, month, day = map(int, birth_date.split("-"))
    hour, minute = map(int, birth_time.split(":"))
    ut = hour + minute / 60.0
    jd = swe.julday(year, month, day, ut)

    # Pianeti principali da calcolare
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
        try:
            lon, lat_, dist, speed = swe.calc_ut(jd, planet)[0]
        except (ValueError, TypeError, IndexError):
            result[name] = {"error": "calculation failed"}
            continue

        sign_index = int(lon // 30)
        degree = lon % 30
        sign = [
            'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
            'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
        ][sign_index]

        result[name] = {
            "sign": sign,
            "degree": f"{degree:.2f}°"
        }

    # Calcolo Ascendente e Case
    hsys = b'P'  # Placidus
    try:
        _, ascmc, _, cusps = swe.houses(jd, lat, lon, hsys)
        result["Ascendant"] = { "degree": f"{ascmc[0]:.2f}°" }
        result["House Cusps"] = {
            f"House {i+1}": f"{c:.2f}°" for i, c in enumerate(cusps)
        }
    except (ValueError, TypeError, IndexError):
        result["Ascendant"] = { "error": "could not calculate ascendant" }
        result["House Cusps"] = { "error": "could not calculate houses" }

    return result
