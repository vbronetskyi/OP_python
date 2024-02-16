"""all_prefixes.py"""
def all_prefixes(strin):
    """
    takes a string as an argument and returns the set
    of all lowercase substrings that start with the first letter
    """
    prefixes = set()
    if strin == "":
        return prefixes
    first_sumb = strin.strip()[0]
    for ind, sumb in enumerate(strin.strip()):
        if sumb == first_sumb:
            strin1 = "".join(strin.strip()[ind:])
            for i in range(len(strin)):
                prefix = strin1[:i+1].lower()
                if prefix[0] == strin1[0].lower():
                    prefixes.add(prefix)
    return prefixes
