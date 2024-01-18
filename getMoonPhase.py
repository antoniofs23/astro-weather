import datetime
import ephem
from emoji import emojize


def get_moon_phase():
    moon_phases = [
        "new_moon",
        "waxing_crescent_moon",
        "first_quarter_moon",
        "waxing_gibbous_moon",
        "full_moon",
        "waning_gibbous_moon",
        "last_quarter_moon",
        "waning_crescent_moon",
    ]

    today = ephem.Date(datetime.date.today())
    nnm = ephem.next_new_moon(today)
    pnm = ephem.previous_new_moon(today)
    ephem_phase = (today - pnm) / (nnm - pnm)
    phase_index = int(ephem_phase * len(moon_phases))
    moon_phase = moon_phases[phase_index]

    moon_phase_emoji = emojize(":" + moon_phase + ":")

    return moon_phase_emoji, nnm
