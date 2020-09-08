import dbus


class SystemBus(object):
    def __init__(self):
        self.bus = dbus.SystemBus()

    def method_call(self, name, object_path, interface, member, *args):
        obj = self.bus.get_object(bus_name=name, object_path=object_path)
        interf = dbus.Interface(object=obj, dbus_interface=interface)

        method = getattr(interf, member)

        res = method(*args)

        return res

    def call(self, obj):
        return self.method_call(obj.name, obj.object_path, obj.interface,
                                obj.member, *obj.args)

    def __getattr__(self, item):
        bus_item = getattr(self.bus, item)

        if bus_item is None:
            return super().__getattribute__(item)
        return bus_item
