#!/usr/bin/python3


# Calculation defaults and constants

BATTERY_12V_VOLTAGE_MIN = 11.0 * 1000
BATTERY_12V_VOLTAGE_MAX = 14.3 * 1000
BATTERY_12V_VOLTAGE_AVG = 12.2 * 1000
BATTERY_24V_VOLTAGE_MIN = 23.0 * 1000
BATTERY_24V_VOLTAGE_MAX = 26.3 * 1000
BATTERY_24V_VOLTAGE_AVG = 24.3 * 1000
UNKNOW_PID = "Unknown"

"""
For each PID, this dictionary contains the following fixed values:
- battery_voltage_min: the minimum battery voltage
- battery_voltage_max: the maximum battery voltage
- load_voltage_avg: the average load voltage
"""
PID_FIXED_VALUES = {
    "0xA060": {
        "battery_voltage_min": BATTERY_12V_VOLTAGE_MIN,
        "battery_voltage_max": BATTERY_12V_VOLTAGE_MAX,
        "load_voltage_avg": BATTERY_12V_VOLTAGE_AVG,
    },
    # TODO add others models...
    UNKNOW_PID: {
        "battery_voltage_min": BATTERY_12V_VOLTAGE_MIN,
        "battery_voltage_max": BATTERY_12V_VOLTAGE_MAX,
        "load_voltage_avg": BATTERY_12V_VOLTAGE_AVG,
    },
}


# Calculation methods

def calculate_battery_voltage_min(properties_cache):
    try:
        product_id = properties_cache['product_id']['value']
        return PID_FIXED_VALUES[product_id]['battery_voltage_min']

    except KeyError:
        return PID_FIXED_VALUES[UNKNOW_PID]['battery_voltage_min']


def calculate_battery_voltage_max(properties_cache):
    try:
        product_id = properties_cache['product_id']['value']
        return PID_FIXED_VALUES[product_id]['battery_voltage_max']

    except KeyError:
        return PID_FIXED_VALUES[UNKNOW_PID]['battery_voltage_max']


def calculate_battery_voltage_percent(properties_cache):
    try:
        battery_voltage: float = properties_cache['battery_voltage']['value']
        battery_voltage_min: float = properties_cache['battery_voltage_min']['value']
        battery_voltage_max: float = properties_cache['battery_voltage_max']['value']

    except KeyError:
        return None

    battery_voltage = battery_voltage - battery_voltage_min
    battery_voltage_max = battery_voltage_max - battery_voltage_min
    return round(battery_voltage / (battery_voltage_max/100), 2)


def calculate_load_voltage(properties_cache):
    try:
        product_id = properties_cache['product_id']['value']
        load_voltage_avg = PID_FIXED_VALUES[product_id]['load_voltage_avg']
        load_current = properties_cache['load_current']['value']
        return load_voltage_avg if load_current > 0 else 0.0

    except KeyError:
        return PID_FIXED_VALUES[UNKNOW_PID]['load_voltage_avg']


def calculate_load_power(properties_cache):
    try:
        load_voltage = properties_cache['load_voltage']['value']    # mV
        load_current = properties_cache['load_current']['value']    # mA
        # return load_voltage * load_current                          # mW
        load_voltage = load_voltage / 1000                          # V
        load_current = load_current / 1000                          # A
        load_power = load_voltage * load_current                    # W
        return load_power * 1000                                    # mW
        # return load_power                                           # W

    except KeyError:
        return None


def calculate_load_power_percent(properties_cache):
    try:
        load_power = properties_cache['load_power']['value']
        load_power_max = properties_cache['load_power_max']['value']
        if load_power == 0 or load_power_max == 0:
            return 0.0
        return round(load_power / (load_power_max/100), 2)

    except KeyError:
        return None


def calculate_load_power_max(properties_cache):
    try:
        load_power = properties_cache['load_power']['value']
        try:
            load_power_max = properties_cache['load_power_max']['value']
        except KeyError:
            return properties_cache['load_power']['value']

        return load_power if load_power > load_power_max else None

    except KeyError:
        return None


def calculate_panel_power_percent(properties_cache):
    try:
        panel_power = properties_cache['panel_power']['value']
        panel_power_max = properties_cache['panel_power_max']['value']
        if panel_power == 0 or panel_power_max == 0:
            return 0.0
        return round(panel_power / (panel_power_max/100), 2)

    except KeyError:
        return None


def calculate_panel_power_max(properties_cache):
    try:
        panel_power = properties_cache['panel_power']['value']
        try:
            panel_power_max = properties_cache['panel_power_max']['value']
        except KeyError:
            return properties_cache['panel_power']['value']

        return panel_power if panel_power > panel_power_max else None

    except KeyError:
        return None
