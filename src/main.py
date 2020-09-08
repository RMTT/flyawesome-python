from dbus_wrapper.SystemBus import SystemBus
from dbus.mainloop.glib import DBusGMainLoop
import gi
from module.GeoInfo import GeoInfo
from module.Awesome import Awesome

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

DBusGMainLoop(set_as_default=True)

bus = SystemBus()
awesome = Awesome()

geoinfo = GeoInfo(bus=bus)
geoinfo.start()

Gtk.main()
