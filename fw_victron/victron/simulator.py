#!/usr/bin/python3

import random

from fw_victron.victron.device import Device
from fw_victron.base.commons import regenerateValueMaxMin


class DeviceSimulator(Device):

    def __init__(self, device, speed):
        super().__init__(device, speed, auto_refresh=False)
        self._data = {
            'FW': '',
            'SER#': '',
            'V': "12000.0",
            'I': '0.0',
            'VPV': '0',
            'PPV': '0',
            'CS': '0',
            'MPPT': '0',
            'OR': '0',
            'ERR': '0',
            'LOAD': "OFF",
            'IL': '0',
            'H19': '0',
            'H20': '0',
            'H21': '0',
            'H22': '0',
            'H23': '0',
            'HSDS': '0',
            'PID': '0xA060'
        }
        self._is_connected = True

    def refresh(self, reset_data=False) -> bool:
        self._data = {
            'FW': '161',
            'SER#': 'HQ221234567',
            'V': str(regenerateValueMaxMin(self._data['V'], 200, 10000, 15000)),
            'I': str(regenerateValueMaxMin(self._data['I'], 200, 0, 4000)),
            'VPV': str(regenerateValueMaxMin(self._data['VPV'], 200, 0, 15000)),
            'PPV': str(regenerateValueMaxMin(self._data['PPV'], 5, 0, 200)),
            'CS': '0',
            'MPPT': '0',
            'OR': '0x00000001',
            'ERR': '0',
            'LOAD': "ON" if random.randint(0, 1) else "OFF",
            'IL': str(regenerateValueMaxMin(self._data['IL'], 200, 0, 4000)),
            'H19': '230',
            'H20': '0',
            'H21': '0',
            'H22': '0',
            'H23': '0',
            'HSDS': '25',
            'PID': '0xA060'
        }
        return True


if __name__ == '__main__':
    v = DeviceSimulator()
    print("{}/{}# [{}CONNECTED]: {}".format(v.device_model, v.device_serial,
                                            "" if v.is_connected else "NOT ", v.latest_data["V"]))
