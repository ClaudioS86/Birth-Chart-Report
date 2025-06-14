import swisseph as swe

swe.set_ephe_path('.')  # imposta il percorso degli efemeridi

def calculate_birth_chart(birth_date, birth_time, lat, lon, timezone):
    year, month, day = map(int, birth_date.split("-"))
    hour, minute = map(int, birth_time.split(":"))

    # Conversione valori in float
    lat = float(lat)
    lon = float(lon)

    try:
        tz_offset = float(timezone)
    except:
        tz_offset = 0.0

    ut = hour + minute / 60.0 - tz_offset

    print(f"[DEBUG] UTC: {ut:.2f} | TZ: {tz_offset} | LAT: {lat} | LON: {lon}")

    if ut < 0 or ut > 24:
        raise ValueError("Invalid UTC time after timezone adjustment")

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
        try:
            lon_p, lat_, dist, speed = swe.calc_ut(jd, planet)
            sign_index = int(lon_p // 30)
            degree = lon_p % 30
            sign = [
                'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
            ][sign_index]

            result[name] = {
                "sign": sign,
                "degree": f"{degree:.2f}°"
            }

        except Exception as e:
            result[name] = {"error": "calculation failed"}

    # Ascendente e case
    hsys = b'P'
    try:
        _, ascmc, _, cusps = swe.houses(jd, lat, lon, hsys)
        result["Ascendant"] = { "degree": f"{ascmc[0]:.2f}°" }
        result["House Cusps"] = {
            f"House {i+1}": f"{c:.2f}°" for i, c in enumerate(cusps)
        }
    except Exception as e:
        result["Ascendant"] = { "error": "could not calculate ascendant" }
        result["House Cusps"] = { "error": "could not calculate houses" }

    return result
