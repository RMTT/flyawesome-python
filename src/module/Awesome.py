from config.awesome import names
from config.awesome import signals
import subprocess


class Awesome(object):
    _awesomewm_client = names.AWESOMEWM_CLIENT_BINARY

    @staticmethod
    def emit_signal_geoinfo(latitude, longitude):
        lua_code = "awesome.emit_signal('%s',%s,%s)" % (signals.GEOINFO_UPDATED, latitude, longitude)
        cmd = names.AWESOMEWM_CLIENT_BINARY + " \"%s\"" % lua_code
        print(cmd)
