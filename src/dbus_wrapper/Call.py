class Call(object):
    def __init__(self, name=None, object_path=None, interface=None, member=None, *args):
        self._name = name
        self._object_path = object_path
        self._interface = interface
        self._member = member
        self._args = args

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def object_path(self):
        return self._object_path

    @object_path.setter
    def object_path(self, value):
        self._object_path = value

    @property
    def interface(self):
        return self._interface

    @interface.setter
    def interface(self, value):
        self._interface = value

    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        self._member = value

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, value):
        self._args = value

    def __call__(self, bus):
        if self._args is None:
            self._args = ()
        return bus.call(self)
