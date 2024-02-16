"""Lab6.3-5"""

def raise_func():
    raise IndexError
    # raise KeyError
def except_func():
    try:
        raise_func()
    except (KeyError, IndexError):
        pass

