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

# get the airplanes current altitude
def get_airplane_altitude():
    sm = SimConnect()
    aq = AircraftRequests(sm)
    altitude = aq.get("PLANE ALTITUDE")
    sm.exit()
    return altitude

# check if the plane is on the ground
def is_on_ground():
    sm = SimConnect()
    aq = AircraftRequests(sm)
    on_ground = aq.get("SIM_ON_GROUND")
    sm.exit()
    return on_ground

# get time in Zulu * not used but leaving it for now *
def get_msfs_time_of_day():
    sm = SimConnect()
    aq = AircraftRequests(sm)
    zulu_time = aq.get("ZULU_TIME")
    sm.exit()
    return zulu_time

# set the airplane lights ON/OFF
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

# get the airplanes lights value (ON/OFF)
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

# --------- license info ---------------------------------------------------#

# MIT License

# Copyright (c) 2023 - Jeremy Stevens

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -------------------- end of license info ---------------------------------------
