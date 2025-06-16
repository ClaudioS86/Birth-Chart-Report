
import subprocess
import json
import os
from datetime import datetime

def run_astrolog_aspects(birth_date, birth_time, latitude, longitude, timezone):
    dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    date_str = dt.strftime("%d %b %Y")
    time_str = dt.strftime("%H:%M")

    cmd = [
        "astrolog", "-qa", "-n", "-v0", "-X",
        "--lon", str(longitude),
        "--lat", str(latitude),
        "--tz", str(timezone),
        date_str, time_str
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    aspects = []
    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 4 and parts[0] != "":
            aspects.append({
                "planet": parts[2],
                "aspect": parts[1],
                "orb": float(parts[3])
            })

    return aspects


def generate_chart_image(birth_date, birth_time, latitude, longitude, timezone, output_path="chart.png"):
    dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    date_str = dt.strftime("%d %b %Y")
    time_str = dt.strftime("%H:%M")

    cmd = [
        "astrolog", "-Xn", "-i", "-z0", "-Q",
        "--lon", str(longitude),
        "--lat", str(latitude),
        "--tz", str(timezone),
        date_str, time_str,
        "-o", output_path
    ]

    subprocess.run(cmd)

    return output_path
