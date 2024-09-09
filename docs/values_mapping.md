# FW Victron - Values Mapping

The properties exposed on the DBus vary depending on
the [type of device](supported_devices.md). A description of the
DBus object to be exposed is defined for each type of device. The DBus object
definitions are specified in the
[dbus_definitions.py](/fw_victron/victron/_dbus_descs.py) file.

During the `main_loop`, this script refresh the device's data and parse any
property found, if the property value is update the script sends the property
update to the DBus. To parse the property it uses the info contained into
the`PROPS_CODE` table. Sometime, it can trigger an exception because the updated
property is not present into the DBus object definitions. In this case add the
property to the DBus object definitions or fix the `PROPS_CODES` table.

## DBus properties

Exposed properties can be of two types: direct or calculated. Direct properties
are exported as they come from the device. Calculated properties are the result
of an elaboration.

### Direct

Direct properties are defined into the `PROPS_CODES` table into
the [mappings.py](/fw_victron/victron/mappings.py) file.

For each property are defined following fields:

* `KEY`: property name on device side
* `name`: property name on DBus
* `desc`: human-readable description of the property
* `parser`: the method to use to parse the value read from the device

| Prop.'s KEY | Prop.'s Name on DBus                | Description                                                                | Parser method                          |
|-------------|-------------------------------------|----------------------------------------------------------------------------|----------------------------------------|
| `V`         | `battery_voltage`                   | Main or channel 1 (battery) voltage                                        | `props_parser_float`                   |
| `V2`        | `battery_voltage_ch2`               | Channel 2 (battery) voltage                                                | `props_parser_float`                   |
| `V3`        | `battery_voltage_ch3`               | Channel 3 (battery) voltage                                                | `props_parser_float`                   |
| `VS`        | `battery_voltage_aux`               | Auxiliary (starter) voltage                                                | `props_parser_float`                   |
| `VM`        | `mid_point_voltage`                 | Mid-point voltage of the battery bank                                      | `props_parser_float`                   |
| `DM`        | `mid_point_deviation`               | Mid-point deviation of the battery bank                                    | `props_parser_float`                   |
| `VPV`       | `panel_voltage`                     | Panel voltage                                                              | `props_parser_float`                   |
| `PPV`       | `panel_power`                       | Panel power                                                                | `props_parser_float`                   |
| `I`         | `battery_current`                   | Main or channel 1 battery current                                          | `props_parser_float`                   |
| `I2`        | `battery_current_ch2`               | Channel 2 battery current                                                  | `props_parser_float`                   |
| `I3`        | `battery_current_ch3`               | Channel 3 battery current                                                  | `props_parser_float`                   |
| `IL`        | `load_current`                      | Load current                                                               | `props_parser_float`                   |
| `LOAD`      | `load_state`                        | Load output state (ON/OFF)                                                 | `props_parser_on_off`                  |
| `T`         | `battery_temperature`               | Battery temperature                                                        | `props_parser_float`                   |
| `P`         | `instantaneous_power`               | Instantaneous power                                                        | `props_parser_float`                   |
| `CE`        | `consumed_amp_hours`                | Consumed Amp Hours                                                         | `props_parser_float`                   |
| `SOC`       | `state_of_charge`                   | State of charge                                                            | `props_parser_float`                   |
| `TTG`       | `time_to_go`                        | Time to go                                                                 | `props_parser_float`                   |
| `Alarm`     | `alarm_condition`                   | Alarm condition active                                                     | `props_parser_on_off`                  |
| `Relay`     | `relay_state`                       | Relay state                                                                | `props_parser_on_off`                  |
| `AR`        | `alarm_reason`                      | Alarm reason                                                               | `props_parser_alarm_or_warning_reason` |
| `OR`        | `off_reason`                        | Off reason                                                                 | `props_parser_off_reason`              |
| `H1`        | `depth_deepest_discharge`           | Depth of the deepest discharge                                             | `props_parser_float`                   |
| `H2`        | `depth_last_discharge`              | Depth of the last discharge                                                | `props_parser_float`                   |
| `H3`        | `depth_average_discharge`           | Depth of the average discharge                                             | `props_parser_float`                   |
| `H4`        | `number_charge_cycles`              | Number of charge cycles                                                    | `props_parser_int`                     |
| `H5`        | `number_full_discharges`            | Number of full discharges                                                  | `props_parser_int`                     |
| `H6`        | `cumulative_mp_drawn`               | Cumulative Amp Hours drawn                                                 | `props_parser_float`                   |
| `H7`        | `min_battery_voltage`               | Minimum main (battery) voltage                                             | `props_parser_float`                   |
| `H8`        | `max_battery_voltage`               | Maximum main (battery) voltage                                             | `props_parser_float`                   |
| `H9`        | `seconds_since_last_full_charge`    | Number of seconds since last full charge                                   | `props_parser_int`                     |
| `H10`       | `number_automatic_synchronizations` | Number of automatic synchronizations                                       | `props_parser_int`                     |
| `H11`       | `number_low_voltage_alarms`         | Number of low main voltage alarms                                          | `props_parser_int`                     |
| `H12`       | `number_high_voltage_alarms`        | Number of high main voltage alarms                                         | `props_parser_int`                     |
| `H13`       | `number_low_voltage_alarms_aux`     | Number of low auxiliary voltage alarms                                     | `props_parser_int`                     |
| `H14`       | `number_high_voltage_alarms_aux`    | Number of high auxiliary voltage alarms                                    | `props_parser_int`                     |
| `H15`       | `min_battery_voltage_aux`           | Minimum auxiliary (battery) voltage                                        | `props_parser_float`                   |
| `H16`       | `max_battery_voltage_aux`           | Maximum auxiliary (battery) voltage                                        | `props_parser_float`                   |
| `H17`       | `discharged_energy`                 | Amount of discharged energy (BMV) / Amount of produced energy (DC monitor) | `props_parser_float`                   |
| `H18`       | `charged_energy`                    | Amount of charged energy (BMV) / Amount of consumed energy (DC monitor)    | `props_parser_float`                   |
| `H19`       | `yield_total`                       | Yield total (user resettable counter)                                      | `props_parser_float`                   |
| `H20`       | `yield_today`                       | Yield today                                                                | `props_parser_float`                   |
| `H21`       | `max_power_today`                   | Maximum power today                                                        | `props_parser_float`                   |
| `H22`       | `yield_yesterday`                   | Yield yesterday                                                            | `props_parser_float`                   |
| `H23`       | `max_power_yesterday`               | Maximum power yesterday                                                    | `props_parser_float`                   |
| `ERR`       | `error_code`                        | Error code                                                                 | `props_parser_error_code`              |
| `CS`        | `state_operation`                   | State of operation                                                         | `props_parser_state_operation`         |
| `BMV`       | `model_description`                 | Model description (deprecated)                                             | `props_parser_model_description`       |
| `FW`        | `firmware_version`                  | Firmware version (16 bit)                                                  | `props_parser_fw16`                    |
| `FWE`       | `firmware_version`                  | Firmware version (24 bit)                                                  | `props_parser_fw24`                    |
| `PID`       | `product_id`                        | Product ID                                                                 | `props_parser_none`                    |
| `SER#`      | `serial_number`                     | Product Serial number                                                      | `props_parser_none`                    |
| `HSDS`      | `day_sequence_number`               | Day sequence number (0..364)                                               | `props_parser_int`                     |
| `MODE`      | `device_mode`                       | Device mode                                                                | `props_parser_mode`                    |
| `AC_OUT_V`  | `ac_output_voltage`                 | AC output voltage                                                          | `props_parser_float`                   |
| `AC_OUT_I`  | `ac_output_current`                 | AC output current                                                          | `props_parser_float`                   |
| `AC_OUT_S`  | `ac_output_apparent_power`          | AC output apparent power                                                   | `props_parser_float`                   |
| `WARN`      | `warning_reason`                    | Warning reason                                                             | `props_parser_alarm_or_warning_reason` |
| `MPPT`      | `tracker_operation_mode`            | Tracker operation mode (MPPT)                                              | `props_parser_mode_mppt`               |
| `MON`       | `dc_monitor_mode`                   | DC monitor mode                                                            | `props_parser_mode_monitor`            |
| `DC_IN_V`   | `dc_input_voltage`                  | DC input voltage                                                           | `props_parser_float`                   |
| `DC_IN_I`   | `dc_input_current`                  | DC input current                                                           | `props_parser_float`                   |
| `DC_IN_P`   | `dc_input_power`                    | DC input power                                                             | `props_parser_float`                   |

Parser methods are defined into [ve_parsers.py](/fw_victron/victron/_parsers.py) file.
Depending on which DBus property's they are mapped for, they can return
different value's types.<br/>
Custom types are defined into
the [ve_definitions.py](/fw_victron/victron/_definitions.py) file.

### Calculated

Calculated properties are special values that can be elaborated starting from
other properties (also other calculated properties). When a property is updated,
the script checks if there is some calculated property that depends on it. If
any, then the script calculate the dependant property.

For each calculated property are defined following fields:

* `KEY`: calculated property name on DBus
* `name`: calculated property name (not used)
* `desc`: human-readable description of the property
* `depends_on`: the list of properties on which the current property depends
* `calculator`: the method to use to elaborate the property

| Prop.'s Name on DBus      | Description                                   | Depends on                                                        | Calculator method                   |
|---------------------------|-----------------------------------------------|-------------------------------------------------------------------|-------------------------------------|
| `battery_voltage_min`     | Battery minimal voltage allowed in milliVolts | ['product_id']                                                    | `calculate_battery_voltage_min`     |
| `battery_voltage_max`     | Battery maximal voltage allowed in milliVolts | ['product_id']                                                    | `calculate_battery_voltage_max`     |
| `battery_voltage_percent` | Battery charge percentage                     | ['battery_voltage', 'battery_voltage_min', 'battery_voltage_max'] | `calculate_battery_voltage_percent` |
| `load_voltage`            | Load voltage in milliVolts                    | ['product_id', 'load_current']                                    | `calculate_load_voltage`            |
| `load_power`              | Load power consumption in milliWatts          | ['load_current', 'load_voltage']                                  | `calculate_load_power`              |
| `load_power_percent`      | Load power consumption percentage             | ['load_power', 'load_power_max']                                  | `calculate_load_power_percent`      |
| `load_power_max`          | Maximum load power consumption in milliWatts  | ['load_power']                                                    | `calculate_load_power_max`          |
| `panel_power_percent`     | Panel power generation percent                | ['panel_power', 'panel_power_max']                                | `calculate_panel_power_percent`     |
| `panel_power_max`         | Maximum power generation by solar panels      | ['panel_power']                                                   | `calculate_panel_power_max`         |

All methods used to elaborate the properties, receives the properties cache as
param. So they can use that list to get all properties read from the device (
also other calculated properties).

## Properties by DBus Object description

This is the table containing all properties handled by this script. For each
property, the table define if it will be exported by the column's device type.

| Prop.'s Name on DBus                | Type    | SmartSolar MPPT | Other DBus obj description |
|-------------------------------------|---------|-----------------|----------------------------|
| `battery_voltage`                   | double  | Yes             | ?                          |
| `battery_voltage_ch2`               | double  | No              | ?                          |
| `battery_voltage_ch3`               | double  | No              | ?                          |
| `battery_voltage_aux`               | double  | No              | ?                          |
| `mid_point_voltage`                 | double  | No              | ?                          |
| `mid_point_deviation`               | double  | No              | ?                          |
| `panel_voltage`                     | double  | Yes             | ?                          |
| `panel_power`                       | double  | Yes             | ?                          |
| `battery_current`                   | double  | Yes             | ?                          |
| `battery_current_ch2`               | double  | No              | ?                          |
| `battery_current_ch3`               | double  | No              | ?                          |
| `load_current`                      | double  | Yes             | ?                          |
| `load_state`                        | boolean | Yes             | ?                          |
| `battery_temperature`               | double  | No              | ?                          |
| `instantaneous_power`               | double  | No              | ?                          |
| `consumed_amp_hours`                | double  | No              | ?                          |
| `state_of_charge`                   | double  | No              | ?                          |
| `time_to_go`                        | double  | No              | ?                          |
| `alarm_condition`                   | boolean | No              | ?                          |
| `relay_state`                       | boolean | No              | ?                          |
| `alarm_reason`                      | string  | No              | ?                          |
| `off_reason`                        | string  | Yes             | ?                          |
| `depth_deepest_discharge`           | double  | No              | ?                          |
| `depth_last_discharge`              | double  | No              | ?                          |
| `depth_average_discharge`           | double  | No              | ?                          |
| `number_charge_cycles`              | int32   | No              | ?                          |
| `number_full_discharges`            | int32   | No              | ?                          |
| `cumulative_mp_drawn`               | double  | No              | ?                          |
| `min_battery_voltage`               | double  | No              | ?                          |
| `max_battery_voltage`               | double  | No              | ?                          |
| `seconds_since_last_full_charge`    | int32   | No              | ?                          |
| `number_automatic_synchronizations` | int32   | No              | ?                          |
| `number_low_voltage_alarms`         | int32   | No              | ?                          |
| `number_high_voltage_alarms`        | int32   | No              | ?                          |
| `number_low_voltage_alarms_aux`     | int32   | No              | ?                          |
| `number_high_voltage_alarms_aux`    | int32   | No              | ?                          |
| `min_battery_voltage_aux`           | double  | No              | ?                          |
| `max_battery_voltage_aux`           | double  | No              | ?                          |
| `discharged_energy`                 | double  | No              | ?                          |
| `charged_energy`                    | double  | No              | ?                          |
| `yield_total`                       | double  | Yes             | ?                          |
| `yield_today`                       | double  | Yes             | ?                          |
| `max_power_today`                   | double  | Yes             | ?                          |
| `yield_yesterday`                   | double  | Yes             | ?                          |
| `max_power_yesterday`               | double  | Yes             | ?                          |
| `error_code`                        | string  | Yes             | ?                          |
| `state_operation`                   | string  | Yes             | ?                          |
| `model_description`                 | string  | No              | ?                          |
| `firmware_version`                  | string  | Yes             | ?                          |
| `product_id`                        | string  | Yes             | ?                          |
| `serial_number`                     | string  | Yes             | ?                          |
| `day_sequence_number`               | int32   | Yes             | ?                          |
| `device_mode`                       | string  | No              | ?                          |
| `ac_output_voltage`                 | double  | No              | ?                          |
| `ac_output_current`                 | double  | No              | ?                          |
| `ac_output_apparent_power`          | double  | No              | ?                          |
| `warning_reason`                    | string  | No              | ?                          |
| `tracker_operation_mode`            | string  | Yes             | ?                          |
| `dc_monitor_mode`                   | string  | No              | ?                          |
| `dc_input_voltage`                  | double  | No              | ?                          |
| `dc_input_current`                  | double  | No              | ?                          |
| `dc_input_power`                    | double  | No              | ?                          |
| `battery_voltage_min`               | double  | Yes             | ?                          |
| `battery_voltage_max`               | double  | Yes             | ?                          |
| `battery_voltage_percent`           | double  | Yes             | ?                          |
| `load_voltage`                      | double  | Yes             | ?                          |
| `load_power`                        | double  | Yes             | ?                          |
| `load_power_percent`                | double  | Yes             | ?                          |
| `load_power_max`                    | double  | Yes             | ?                          |
| `panel_power_percent`               | double  | Yes             | ?                          |
| `panel_power_max`                   | double  | Yes             | ?                          |
