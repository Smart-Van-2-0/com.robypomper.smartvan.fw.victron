#!/usr/bin/python3

from fw_victron.victron._definitions import *


def props_parser_none(raw_value):
    """
    This parser is used when the property doesn't need to be parsed.
    """
    return raw_value


def props_parser_bool(raw_value: str) -> bool:
    """
    This parser is used when the property is a boolean.
    """
    try:
        return bool(raw_value)
    except Exception:
        raise ValueError("Can't cast '{}' into {}".format(raw_value, "bool"))


# LOAD -> load_state
# Alarm -> alarm_condition
# Relay -> relay_state
def props_parser_on_off(raw_value: str) -> bool:
    """
    This parser is used when the property is a boolean represented as a string "on" or "off".
    """
    try:
        if raw_value.lower() == "on":
            return True
        elif raw_value.lower() == "off":
            return False
        else:
            raise ValueError("Can't cast '{}' into {}, invalid value".format(raw_value, "float"))
    except Exception:
        raise ValueError("Can't cast '{}' into {}".format(raw_value, "float"))


def props_parser_int(raw_value: str) -> int:
    """
    This parser is used when the property is an integer.
    """
    try:
        return int(raw_value)
    except Exception:
        raise ValueError("Can't cast '{}' into {}".format(raw_value, "int"))


def props_parser_float(raw_value: str) -> float:
    """
    This parser is used when the property is a float.
    """
    try:
        return float(raw_value)
    except Exception:
        raise ValueError("Can't cast '{}' into {}".format(raw_value, "float"))


def props_parser_float_multi1000(raw_value: str) -> float:
    """
    This parser is used when the property is a float that must be multiplied by 1000.
    """
    return props_parser_float(raw_value) * 1000


# FW -> firmware
def props_parser_fw16(raw_value):
    """
    This parser is used when the property is a firmware version represented as a 16-bit integer.
    """
    if raw_value == b'\xff\xff\xff':
        return 'NO FIRMWARE'
    if raw_value[0] == '0':
        return f'{raw_value[1:2]}.{raw_value[2:]}'
    else:
        return f'{raw_value[0:1]}.{raw_value[1:2]}{raw_value[2:]}'


# FWE -> firmware (24bit)
def props_parser_fw24(raw_value):
    """
    This parser is used when the property is a firmware version represented as a 24-bit integer.
    """
    raise NotImplementedError("Method props_parser_fw24() not implemented.")


# AR -> alarm_reason
# WARN -> warning_reason
def props_parser_alarm_or_warning_reason(raw_value: str):
    """
    This parser is used when the property is an alarm or warning reason.

    The raw value is a string that represents a code that must be mapped to a
    human-readable value. The mapping is done using the WARN_AR dictionary.
    """
    try:
        return WARN_AR[raw_value]
    except Exception:
        raise ValueError("Can't find {} mapped value for '{}' code".format("WARN_AR", raw_value))


# OF -> off_reason
def props_parser_off_reason(raw_value: str):
    """
    This parser is used when the property is an off reason.

    The raw value is a string that represents a code that must be mapped to a
    human-readable value. The mapping is done using the OR dictionary.
    """
    try:
        return OR[raw_value]
    except Exception:
        raise ValueError("Can't find {} mapped value for '{}' code".format("OR", raw_value))


# ERR -> error_code
def props_parser_error_code(raw_value: str):
    """
    This parser is used when the property is an error code.

    The raw value is a string that represents a code that must be mapped to a
    human-readable value. The mapping is done using the ERROR dictionary.
    """
    try:
        return ERROR[raw_value]
    except Exception:
        raise ValueError("Can't find {} mapped value for '{}' code".format("ERROR", raw_value))


# CS -> state_operation
def props_parser_state_operation(raw_value: str):
    """
    This parser is used when the property is a state operation.

    The raw value is a string that represents a code that must be mapped to a
    human-readable value. The mapping is done using the CS dictionary.
    """
    try:
        return CS[raw_value]
    except Exception:
        raise ValueError("Can't find {} mapped value for '{}' code".format("CS", raw_value))


# BMV -> model_description
def props_parser_model_description(raw_value: str):
    return 0  # BMV property code was deprecated


# MODE -> device_mode
def props_parser_mode(raw_value: str):
    """
    This parser is used when the property is a device mode.

    The raw value is a string that represents a code that must be mapped to a
    human-readable value. The mapping is done using the MODE dictionary.
    """
    try:
        return MODE[raw_value]
    except Exception:
        raise ValueError("Can't find {} mapped value for '{}' code".format("MODE", raw_value))


# MPPT -> tracker_operation_mode
def props_parser_mode_mppt(raw_value: str):
    """
    This parser is used when the property is a tracker operation mode.

    The raw value is a string that represents a code that must be mapped to a
    human-readable value. The mapping is done using the MPPT dictionary.
    """
    try:
        return MPPT[raw_value]
    except Exception:
        raise ValueError("Can't find {} mapped value for '{}' code".format("MPPT", raw_value))


# MON -> dc_monitor_mode
def props_parser_mode_monitor(raw_value: str):
    """
    This parser is used when the property is a dc monitor mode.

    The raw value is a string that represents a code that must be mapped to a
    human-readable value. The mapping is done using the MON dictionary.
    """
    try:
        return MON[raw_value]
    except Exception:
        raise ValueError("Can't find {} mapped value for '{}' code".format("MON", raw_value))
