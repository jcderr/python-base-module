class Manager(object):
    resource_class = None

    def __init__(self, something):
        self.something = something

    def _list(self):
        pass

    def _get(self, *args, **kwargs):
        pass

    def _put(self, *args, **kwargs):
        pass

    def _post(self, *args, **kwargs):
        pass

    def _create(self):
        pass

    def _delete(self, *args, **kwargs):
        pass

    def _update(self):
        pass

    def find(self, **kwargs):
        pass

    def findall(self, **kwargs):
        pass

class Resource(object):
    """
    This is pretty much just a bag for attributes.
    """
    def __init__(self, manager, info):
        self.manager = manager
        self._info = info
        self._add_details(info)

    def _add_details(self, info):
        for (k, v) in info.iteritems():
            if k == 'manager':
                print k, v
            setattr(self, k, v)

    def __getattr__(self, k):
        # self.get()
        if k not in self.__dict__:
            raise AttributeError(k)
        else:
            return self.__dict__[k]

    def __repr__(self):
        reprkeys = sorted(k for k in self.__dict__.keys() if k[0] != '_' and k != 'manager')
        info = ", ".join("%s=%s" % (k, getattr(self, k)) for k in reprkeys)
        return "<%s %s>" % (self.__class__.__name__, info)

    def get(self):
        new = self.manager.get(self.name)
        self._add_details(new._info)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if hasattr(self, 'id') and hasattr(other, 'id'):
            return self.id == other.id
        return self._info == other._info

def getid(obj):
    try:
        return obj.id
    except AttributeError:
        return int(obj)