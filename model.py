__author__ = 'saravanakumar'

from jsonobject import *

class File(JsonObject):
    name = StringProperty()
    size = IntegerProperty()

class DiskUsage(JsonObject):
    files = ListProperty(File)
