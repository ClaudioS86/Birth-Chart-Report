import swisseph as swe

# Imposta il percorso degli efemeridi
swe.set_ephe_path(".")

def calculate_birth_chart(birth_date, birth_time, lat, lon, timezone):
    # Converte i valori di input in float
    lat = float(lat)
    lon = float(lon)
    try:
        tz_offset = float(timezone)
    except:
        tz_offset = 0.0

    # Parsing data e ora
    year, month, day = map(int, birth_date.split("-"))
    hour, minute = map(int, birth_time.split(":"))
    ut = hour + minute / 60.0 - tz_offset

    print(f"[DEBUG] UTC: {ut:.2f} | TZ: {tz_offset} | LAT: {lat} | LON: {lon}")

    if ut < 0 or ut > 24:
        raise ValueError("Invalid UTC time after timezone adjustment")

    # Calcolo del giorno giuliano
    jd = swe.julday(year, month, day, ut)

    # Definizione dei pianeti principali
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
            calc_result = swe.calc_ut(jd, planet)[0]
            lon_p = calc_result[0]
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
            result[name] = { "error": f"calculation failed: {str(e)}" }

    # ✅ Calcolo Ascendente e Case (FIXED)
    try:
        hsys = b'P'  # deve essere byte string ✔️
        cusps, ascmc = swe.houses(jd, lat, lon, hsys)[0:2]
        result["Ascendant"] = { "degree": f"{ascmc[0]:.2f}°" }
        result["House Cusps"] = {
            f"House {i+1}": f"{c:.2f}°" for i, c in enumerate(cusps)
        }
    except Exception as e:
        result["Ascendant"] = { "error": f"could not calculate ascendant: {str(e)}" }
        result["House Cusps"] = { "error": f"could not calculate houses: {str(e)}" }

    return result
