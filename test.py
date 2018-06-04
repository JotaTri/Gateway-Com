from core.formula import Formula
class C(object):
    """docstring for C."""
    def __init__(self, *argv):
        for arg in argv[0]:
            print arg

Formula('MED_T(1,,[3])')
# a = [[1,2,7]]
# C(arg for arg in a[0])
