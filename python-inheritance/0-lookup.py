#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Args:
        obj: Any Python object to inspect
        
    Returns:
        list: A sorted list of attribute and method names
    """
    return sorted(dir(obj))
