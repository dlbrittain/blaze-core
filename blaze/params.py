from collections import Mapping, OrderedDict

defaults = {
    'clevel'        : 5,
    'shuffle'       : False,
    'format_flavor' : 'chunked',
    #'storage'       : None,
}

class params(Mapping):
    """
    Container for parameters

    Usage:

    >>> params(clevel=4)
    params(shuffle=False, clevel=4, format_flavor=chunked)
    >>> params(clevel=4, storage='tmpdir')
    params(shuffle=False, clevel=4, format_flavor=chunked, storage=tmpdir)

    """
    __slots__ = ['cls', '__internal']

    def __init__(self, **kw):
        self.__internal = dict(defaults, **kw)

        if not params.cls:
            params.cls = frozenset(dir(self))

    def __setattr__(self, key, value):
        if key == 'cls' or key == '__internal' or '_params' in key:
            super(params, self).__setattr__(key, value)
        else:
            self.__internal[key] = value
        return value

    def __getattr__(self, key):
        if key in self.cls:
            super(params, self).__getattr__(key)
        else:
            return self.__internal[key]

    def __getitem__(self, key):
        return self.__internal[key]

    def __contains__(self, key):
        return key in self.__internal

    def __len__(self):
        return len(self.__internal)

    def __iter__(self):
        return self.__internal.iterkeys()

    def iteritems(self):
        return self.__internal.items()

    def __repr__(self):
        return 'params({keys})'.format(
            keys=''.join('%s=%s, ' % (k,v) for k,v in self.__internal.items())
        )

    @classmethod
    def empty(cls, header):
        return cls(dct=dict(header))
