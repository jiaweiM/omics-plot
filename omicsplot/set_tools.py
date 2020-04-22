def venn_set(a, b, c):
    """
    return count in (Abc, aBc, ABc, abC, AbC, aBC, ABC)
    :param a: a set
    :param b: a set
    :param c: a set
    :return: set intersection regions.
    """
    s37 = a & b
    s57 = a & c
    s67 = b & c
    s7 = s37 & s57

    c7 = len(s7)
    c6 = len(s67) - c7
    c5 = len(s57) - c7
    c4 = len(c) - len(s57) - c6
    c3 = len(s37) - c7
    c2 = len(b) - len(s67) - c3
    c1 = len(a) - len(s57) - c3

    return c1, c2, c3, c4, c5, c6, c7
