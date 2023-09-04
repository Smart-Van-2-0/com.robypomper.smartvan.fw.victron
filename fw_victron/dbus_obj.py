#!/usr/bin/python3

import logging
from pydbus.generic import signal

from .mappings import *

logger = logging.getLogger()


class DBusObject:
    PropertiesChanged = signal()

    def __init__(self, dbus_name, obj_path, pid):
        if pid not in PID:
            raise NotImplementedError("Device with '{}' PID not implemented."
                                      .format(pid))

        self._cached_properties = {}

        self.dbus_name = dbus_name
        self.obj_path = obj_path

        dbus_obj_definition = PID[pid]['dbus_desc']
        if dbus_obj_definition is None:
            raise NotImplementedError("Device model '{}' with '{}' PID not implemented."
                                      .format(PID[pid].model, pid))
        self.dbus = dbus_obj_definition.format(dbus_name=self.dbus_name)

    def publish(self, dbus):
        logger.info(
            "Publish DBus '{}'.".format(self.dbus_name + ("@" + self.obj_path if self.obj_path is not None else "")))
        dbus_obj_pub = self.obj_path, self, self.dbus
        dbus.publish(self.dbus_name, dbus_obj_pub)

    def update_property(self, property_name, value):
        if property_name in self._cached_properties:
            if self._cached_properties[property_name] == value:
                return
        logger.debug("Property update '{} = {}'.".format(property_name, value))
        self._cached_properties[property_name] = value
        self.PropertiesChanged(self.dbus_name, {property_name: value}, [])
