import swisseph as swe
import matplotlib.pyplot as plt
import os
from datetime import datetime

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

def get_planet_positions(birth_date, birth_time, lat, lon, timezone):
    year, month, day = map(int, birth_date.split("-"))
    hour, minute = map(int, birth_time.split(":"))
    ut = hour + minute / 60.0 - timezone
    jd = swe.julday(year, month, day, ut)

    positions = {}
    for name, planet_id in PLANETS.items():
        pos, _ = swe.calc_ut(jd, planet_id)
        positions[name] = pos[0]

    return positions

def create_chart_image(birth_date, birth_time, lat, lon, timezone):
    positions = get_planet_positions(birth_date, birth_time, lat, lon, timezone)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.set_theta_zero_location('E')
    ax.set_theta_direction(-1)
    ax.set_yticklabels([])
    ax.set_xticks([i * (3.14159 / 6) for i in range(12)])
    ax.set_xticklabels(['♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓'])

    for i in range(12):
        angle = i * 30 * (3.14159 / 180)
        ax.plot([angle, angle], [0, 1], color='lightgray', lw=0.8)

    for planet, angle in positions.items():
        theta = (angle % 360) * (3.14159 / 180)
        ax.plot(theta, 1, 'o', label=planet)
        ax.text(theta, 1.05, planet, ha='center', va='center', fontsize=9)

    output_path = "chart.png"
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    return output_path
