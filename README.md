# FW Victron

Simple Python module that read data from Victron devices and share them on
the local DBus.<br />
This repository is part of
the [Smart Van Project](https://smartvan.johnosproject.org/).

**FW Name:** FW Victron<br />
**FW Group:** com.robypomper.smartvan.fw.victron<br />
**FW Version:** 1.0.3

[README](README.md) | [CHANGELOG](CHANGELOG.md) | [TODOs](TODOs.md) | [LICENCE](LICENCE.md)

Once ran, this script **reads data from the serial specified port then notify
the DBus with updated values**. The DBus service and his properties depends on
the PID get from the device. More info
on [Supported devices](/docs/supported_devices.md)
and [value mapping](/docs/values_mapping.md).

## Run

This is a Python script, so `python` is required to run it.

```shell
$ python --version
# if not installed, then run
$ sudo apt-get install python3 python3-pip 
```

In addition, some other package must be installed in order to configure
python's dependencies like `PyGObject` or `pydbus`. If you are using a
debian/ubuntu based distribution, then you can run:

```shell
$ sudo apt-get install libcairo2-dev libgirepository1.0-dev dbus-x11
```

Once Python was installed on your machine, you can install the script's
requirements globally or create a dedicated `venv`.

```shell
# Init venv (Optional)
$ python -m venv venev
$ source venv/bin/activate

# Install script's requirements
$ pip install -r requirements.txt
```

Now, you are ready to run the script with the command:

```shell
$ python run.py

or alternative options
$ python run.py --quiet
$ python run.py --debug --simulate
$ python run.py  --dbus-name com.custom.bus --dbus-obj-path /custom/path --dbus-iface com.custom.IFace
```

For script's [remote usage](docs/remote_usage.md) please see the dedicated page.

Defaults DBus params are:

* DBus Name: `com.victron`
* DBus Obj Path: `DEV_TYPE_*` as device code (eg: `SmartSolar MPPT` become
  `/smartsolar_mppt`, see [Supported devices](/docs/supported_devices.md) for
  the full list of `DEV_TYPE_*` values)
* DBus Interface: `DEV_IFACE_*` (eg: `com.victron.SmartSolarMPPT`,
  see [Supported devices](/docs/supported_devices.md) for the full list of
  `DEV_IFACE_*` values)

### Script's arguments

The `run.py` script accept following arguments:

* `-h`, `--help`: show this help message and exit
* `-v`, `--version`: show version and exit
* `--port PORT`: Serial port name (default: `/dev/ttyUSB0`)
* `--speed SPEED`: Serial port speed (default: `19200`)
* `--simulate`: Simulate a VEDevice with id `0xA060` (default: `False`)
* `--dbus-name DBUS_NAME`: DBus name to connect to (Default: `com.victron`)
* `--dbus-obj-path DBUS_OBJ_PATH`: DBus object path to use for object
  publication (Default: the `device_type_code` string)
* `--dbus-iface DBUS_IFACE`: DBus object's interface (Default: current device's
  `dbus_iface`)
* `--dev`: enable development mode, increase log messages
* `--debug`: Set log level to debug
* `--quiet`: Set log level to error and

## Develop

The main goal for this script is to link the VE.Direct protocol to the DBus.
So, in addition to the main script, all other files are related to the device
or to the DBus protocols.

Module's files can be grouped in 2 categories:

**Definitions:**

* [victron/mappings.py](/fw_victron/victron/mappings.py):
  definition of `PID`, `PROPS_CODES` and `CALC_PROPS_CODES` tables
* [victron/_definitions.py](/fw_victron/victron/_definitions.py):
  definitions of supported devices, DUbus ifaces and custom properties types
* [victron/_parsers.py](/fw_victron/victron/_parsers.py):
  custom properties parsers
* [victron/_calculated.py](/fw_victron/victron/_calculated.py):
  custom properties calculators and data generator methods for simulator
* [victron/_dbus_descs.py](/fw_victron/victron/_dbus_descs.py):
  definition of DBus iface's descriptors

**Operations:**

* [run.py](run.py):
  main firmware script
* [victron/device.py](/fw_victron/victron/device.py):
  class that represent the device
* [victron/simulator.py](/fw_victron/victron/simulator.py):
  class that represent the simulated device
* [dbus/obj.py](/fw_victron/dbus/obj.py):
  class that represent aDBus object to publish
* [dbus/daemon.py](/fw_victron/dbus/daemon.py):
  methods to handle the DBus daemon
* [base/commons.py](/fw_victron/base/commons.py):
  commons properties parsers and simulator methods
* [base/device.py](/fw_victron/base/device.py):
  base class for devices
* [base/device_serial.py](/fw_victron/base/device_serial.py):
  base implementation for serial devices
