from __future__ import absolute_import, unicode_literals
from .data import CROSSWALK


def get(value):
    """
    Accepts a value and tries to match it a U.S. state or territory.

    Works with postal codes, full names, AP abbreviations and FIPS codes.

    Return an object with metadata about the state.
    """
    # Strip leading zeroes of any fips that come in as strings
    try:
        value = int(value)
    except ValueError:
        pass
    # Clean up any strings
    if _is_string(value):
        value = value.strip().lower()
    # Convert numbers back to strings
    elif isinstance(value, (int, float)):
        value = str(value)
    try:
        return State(**CROSSWALK[value])
    except KeyError:
        raise ValueError("The state you requested does not exist")


class State(object):
    """
    One of America's states or territories.
    """
    def __init__(self, postal, name, fips, ap, type, stateface):
        self.postal = postal
        self.name = name
        self.fips = fips
        self.ap = ap
        self.type = type
        self.stateface = stateface

    def __iter__(self):
        return iter(self.__dict__.items())

    def __getitem__(self, key):
        return getattr(self, key)

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return self.__dict__


def _is_string(possible_string):
    """
    Checks if an object is a string.
    Works with Python2 and Python3.
    """
    try:
        return isinstance(possible_string, basestring)
    except NameError:
        return isinstance(possible_string, str)
