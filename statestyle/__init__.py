from data import CROSSWALK


def get(string):
    """
    Accepts a string and tries to match it a U.S. state or territory.
    
    Works with postal abbreviations, full names, AP abbreviations and FIPS codes.
    
    Return an object with metadata about the state.
    """
    try:
        return State(**CROSSWALK[string.strip().lower()])
    except KeyError:
        raise ValueError("The state you requested does not exist")


class State(object):
    """
    One of America's states or territories.
    """
    def __init__(self, postal, name, fips, ap, type):
        self.postal = postal
        self.name = name
        self.fips = fips
        self.ap = ap
        self.type = type
    
    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)
    
    def __str__(self):
        return self.__unicode__().encode("utf-8")
    
    def __unicode__(self):
        return self.name
