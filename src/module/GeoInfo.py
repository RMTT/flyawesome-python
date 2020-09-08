from dbus_wrapper.Call import Call
from config.dbus import names
import dbus
from module.Awesome import Awesome


class GeoInfo(object):

    def __init__(self, bus=None):
        self._bus = bus
        self._latitude = None
        self._longitude = None

    @property
    def bus(self):
        return self._bus

    @bus.setter
    def bus(self, value):
        self._bus = value

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def update(self, location_path):
        # get latitude and longitude
        call = Call()
        call.name = names.SERVICES_GEOCLUE2
        call.object_path = location_path
        call.interface = names.INTERFACES_DBUS_PROPERTIES
        call.member = names.MEMBER_DBUS_GET_ALL_PROPERTIES
        call.args = (dbus.String(names.INTERFACES_GEOCLUE2_LOCATION),)
        res = call(self._bus)
        self._latitude = res[names.PROPERTY_NAME_GEOCLUE2_LOCATION_LATITUDE]
        self._longitude = res[names.PROPERTY_NAME_GEOCLUE2_LOCATION_LONGITUDE]

        Awesome.emit_signal_geoinfo(self._latitude, self._longitude)

    def start(self):
        call = Call()

        # get client of geoclue2
        call.name = names.SERVICES_GEOCLUE2
        call.object_path = names.OBJECT_PATHS_GEOCLUE2_MANAGER
        call.interface = names.INTERFACES_GEOCLUE2_MANAGER
        call.member = names.MEMBER_GEOCLUE2_GETCLIENT
        geoclue2_client_path = call(self._bus)

        # set desktop id
        call.object_path = geoclue2_client_path
        call.interface = names.INTERFACES_DBUS_PROPERTIES
        call.member = names.MEMBER_DBUS_SET_PROPERTY
        call.args = (
            dbus.String(names.INTERFACES_GEOCLUE2_CLIENT), dbus.String(names.PROPERTY_NAME_GEOCLUE2_DESKTOP_ID),
            dbus.String(names.GEOCLUE2_DESKTOP_ID))
        call(self._bus)

        # register signal receiver
        self._bus.add_signal_receiver(lambda old, new: self.update(new),
                                      dbus_interface=names.INTERFACES_GEOCLUE2_CLIENT,
                                      signal_name=names.SIGNAL_GEOCLUE2_UPDATE_LOCATION)

        # start update location
        call.interface = names.INTERFACES_GEOCLUE2_CLIENT
        call.member = names.MEMBER_GEOCLUE2_START
        call.args = ()
        call(self._bus)
