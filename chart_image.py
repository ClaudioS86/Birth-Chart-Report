import swisseph as swe
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import io
from matplotlib.patches import Wedge, Circle
from matplotlib.offsetbox import AnchoredText

ZODIAC_SIGNS = [
    (“♈”, '#f7879a'), (“♉”, '#fbb36b'), (“♊”, '#fff96c'), (“♋”, '#a3e048'),
    (“♌”, '#50c4fe'), (“♍”, '#d59bf6'), (“♎”, '#f7879a'), (“♏”, '#fbb36b'),
    (“♐”, '#fff96c'), (“♑”, '#a3e048'), (“♒”, '#50c4fe'), (“♓”, '#d59bf6')
]

PLANETS = {
    "Sun": swe.SUN, "Moon": swe.MOON, "Mercury": swe.MERCURY, "Venus": swe.VENUS, "Mars": swe.MARS,
    "Jupiter": swe.JUPITER, "Saturn": swe.SATURN, "Uranus": swe.URANUS, "Neptune": swe.NEPTUNE, "Pluto": swe.PLUTO
}

PLANET_SYMBOLS = {
    "Sun": '☉', "Moon": '☽', "Mercury": '☿', "Venus": '♀', "Mars": '♂',
    "Jupiter": '♃', "Saturn": '♄', "Uranus": '♅', "Neptune": '♆', "Pluto": '♇'
}

def get_julian_day(date_str, time_str):
    year, month, day = map(int, date_str.split("-"))
    hour, minute = map(int, time_str.split(":"))
    return swe.julday(year, month, day, hour + minute / 60.0)

def draw_chart(date_str, time_str, lat, lon, timezone, name="Client"): 
    jd = get_julian_day(date_str, time_str) - (timezone / 24.0)
    positions = {}
    for planet, pid in PLANETS.items():
        pos, _ = swe.calc_ut(jd, pid)
        positions[planet] = pos[0]

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Cerchi
    outer = Circle((0, 0), 1, fill=False, color='black', lw=2)
    mid = Circle((0, 0), 0.9, fill=False, color='gray', lw=1)
    ax.add_patch(outer)
    ax.add_patch(mid)

    # Case
    for i in range(12):
        angle = 360 / 12 * i
        rad = np.deg2rad(angle)
        ax.plot([0, np.cos(rad)], [0, np.sin(rad)], color='black', lw=1)

    # Segni zodiacali colorati
    for i, (symbol, color) in enumerate(ZODIAC_SIGNS):
        start = i * 30
        wedge = Wedge((0, 0), 1, start, start + 30, width=0.1, facecolor=color, edgecolor='none')
        ax.add_patch(wedge)
        mid_angle = np.deg2rad(start + 15)
        ax.text(0.95 * np.cos(mid_angle), 0.95 * np.sin(mid_angle), symbol, ha='center', va='center', fontsize=14)

    # Pianeti
    for name, angle in positions.items():
        rad = np.deg2rad(angle)
        x, y = 0.75 * np.cos(rad), 0.75 * np.sin(rad)
        ax.plot(x, y, 'o', color='black')
        ax.text(x, y, PLANET_SYMBOLS[name], fontsize=12, ha='center', va='center', color='black')

    # Nome del cliente
    ax.text(0, 1.15, name, ha='center', va='bottom', fontsize=14, weight='bold')

    # Tabellone posizioni
    table_text = f"Date: {date_str} {time_str}\nLat: {lat}  Lon: {lon}  TZ: GMT{timezone:+}h\n\n"
    for name, angle in positions.items():
        deg = int(angle)
        min = int((angle - deg) * 60)
        table_text += f"{PLANET_SYMBOLS[name]} {name:<8}: {deg}°{min:02}'\n"

    at = AnchoredText(table_text, loc='lower left', prop=dict(size=8), frameon=True)
    ax.add_artist(at)

    # Export
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return buf
