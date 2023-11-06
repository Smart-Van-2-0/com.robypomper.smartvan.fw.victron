# FW Victron

Simple Python module that read data from Victron devices and share them on
the local DBus.<br />
This repository is part of
the [Smart Van Project](https://smartvan.johnosproject.org/).

**FW Name:** FW Victron<br />
**FW Group:** com.robypomper.smartvan.fw.victron<br />
**FW Version:** 1.0.2-DEV

[README](README.md) | [CHANGELOG](CHANGELOG.md) | [TODOs](TODOs.md) | [LICENCE](LICENCE.md)

Once ran, this script **reads data from the serial specified port then notify
the DBus with updated values**. The DBus service and his properties depends on
the PID get from the device. More info
on [Supported devices](/docs/supported_devices.md)
and [value mapping](/docs/values_mapping.md).

## Run

This is a Python script, so `python` is required to run it.

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

or specify DBus params

$ python run.py  --dbus-name com.custom.bus --dbus-obj-path /custom/path --dbus-iface com.custom.IFace
```

For script's [remote usage](docs/remote_usage.md) please see the dedicated page.

Defaults DBus params are:

* DBus Name: `com.victron`
* DBus Obj Path: DEV_TYPE_* (eg: `smartsolar_mppt`,
  see [Supported devices](/docs/supported_devices.md))
* DBus Interface: DEV_IFACE_* (eg: `com.victron.SmartSolarMPPT`,
  see [Supported devices](/docs/supported_devices.md))

### Script's arguments

The `run.py` script accept following arguments:

* `-h`, `--help`: show this help message and exit
* `-v`, `--version`: show version and exit
* `--port PORT`: serial port
* `--speed SPEED`: serial port speed
* `--simulate`: Simulate a VEDevice with id `0xA060`
* `--dbus-name DBUS_NAME`: DBus name
* `--dbus-obj-path DBUS_OBJ_PATH`: DBus object path (if None, the device type
  will be used, if empty nothing will be used)
* `--dbus-iface DBUS_IFACE`: DBus interface (if None, the device interface will
  be used, if empty nothing will be used)
* `--dev`: enable development mode, increase logged messages info
* `--debug`: Set log level to debug
* `--quiet`: Set log level to error and

## Develop

The main goal for this script is to link the VE.Direct protocol to the DBus.
So, in addition to the main script, all other files are related to the VE Direct
or to the DBus protocols.
