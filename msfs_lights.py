from SimConnect import *
from enum import Enum

# ---- See License at bottom of file ----

class AirplaneLights(Enum):
    NAVIGATION = "NAV LIGHTS"
    BEACON = "BEACON LIGHTS"
    LANDING = "LANDING LIGHTS"
    TAXI = "TAXI LIGHTS"
    STROBE = "STROBE LIGHTS"
    LOGO = "LOGO LIGHTS"
    WING = "WING LIGHTS"
    RUNWAY_TURN_OFF = "RUNWAY TURN OFF LIGHTS"
    RECOGNITION = "RECOGNITION LIGHTS"

# get IS_NIGHT from simconnect
def is_night():
    sm = SimConnect()
    aq = AircraftRequests(sm)
    results = aq.get("IS_NIGHT")
    sm.exit()
    return results

def get_airplane_altitude():
    sm = SimConnect()
    aq = AircraftRequests(sm)
    altitude = aq.get("PLANE ALTITUDE")
    sm.exit()
    return altitude

def is_on_ground():
    sm = SimConnect()
    aq = AircraftRequests(sm)
    on_ground = aq.get("SIM_ON_GROUND")
    sm.exit()
    return on_ground


def get_msfs_time_of_day():
    sm = SimConnect()
    aq = AircraftRequests(sm)
    zulu_time = aq.get("ZULU_TIME")
    sm.exit()
    return zulu_time


def get_airplane_altitude():
    sm = SimConnect()
    aq = AircraftRequests(sm)
    altitude = aq.get("PLANE_ALTITUDE")
    sm.exit()
    return altitude


def set_airplane_light_value(light: AirplaneLights, value: bool):
    sm = SimConnect()
    aq = AircraftRequests(sm)

    if light == AirplaneLights.LANDING:
        aq.set("LIGHT LANDING ON", int(value))
    elif light == AirplaneLights.TAXI:
        aq.set("LIGHT TAXI ON", int(value))
    elif light == AirplaneLights.BEACON:
        aq.set("LIGHT BEACON ON", int(value))
    elif light == AirplaneLights.NAV:
        aq.set("LIGHT NAV ON", int(value))
    elif light == AirplaneLights.STROBE:
        aq.set("LIGHT STROBE ON", int(value))
    elif light == AirplaneLights.LOGO:
        aq.set("LIGHT LOGO ON", int(value))
    elif light == AirplaneLights.CABIN:
        aq.set("LIGHT CABIN ON", int(value))
    elif light == AirplaneLights.RECOGNITION:
        aq.set("LIGHT RECOGNITION ON", int(value))
    sm.exit()


def get_airplane_light_values():
    # Establish a connection to the simulator
    sm = SimConnect()
    aq = AircraftRequests(sm)
    # Retrieve light values from MSFS
    light_values = {}
    for light in AirplaneLights:
        light_value = aq.get(str(light.value))
        light_values[light] = light_value
    # Close the connection to the simulator
    sm.exit()
    return light_values
