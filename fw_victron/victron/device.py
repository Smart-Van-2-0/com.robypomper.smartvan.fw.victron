#!/usr/bin/python3

from fw_victron.victron.mappings import *
from fw_victron.device_serial import DeviceSerial


class Device(DeviceSerial):
    """
    Device class for Victron devices communicating via Serial port
    """

    def __init__(self, device: str = '/dev/ttyUSB0', speed: int = 19200, auto_refresh=True):
        super().__init__(device, speed, "PID", auto_refresh)

        self.cached_pid = None
        self.cached_model = None
        self.cached_type = None
        self.cached_serial = None

    def _parse_pdu(self, frames):
        for frame in frames:
            if frame.startswith(b'Checksum'):
                # This entry is useless
                continue
            key, value = frame.strip().decode('utf-8').split('\t')
            self._data[key] = value

    @property
    def device_serial(self) -> "str | None":
        """ Returns the device serial number """
        if self.cached_serial is None:
            self.cached_serial = self._data['SER#']

        return self.cached_serial

    @property
    def device_pid(self) -> "str | None":
        """ Returns the device PID """
        if self.cached_pid is None:
            self.cached_pid = self._data['PID']

        return self.cached_pid

    @property
    def device_model(self) -> "str | None":
        """ Returns the device model """
        if self.cached_model is None:
            if self.device_pid is not None:
                self.cached_model = PID[self.device_pid]['model']

        return self.cached_model

    @property
    def device_type(self) -> str:
        """ Returns the device type """
        if self.cached_type is None:
            model = self.device_model
            if model is not None:
                try:
                    self.cached_type = PID[self.device_pid]['type']
                except KeyError as err:
                    raise SystemError("Unknown PID '{}' read from device".format(self.device_pid)) from err

        return self.cached_type if self.cached_type is not None else DEV_TYPE_UNKNOWN


if __name__ == '__main__':
    v = Device()
    print("{}/{}# [{}CONNECTED]: {}".format(v.device_model, v.device_serial,
                                            "" if v.is_connected else "NOT ", v.latest_data["V"]))
