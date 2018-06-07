from core.formula import Formula
class C(object):
    """docstring for C."""
    def __init__(self, *argv):
        for arg in argv[0]:
            print arg
formula = Formula().getFormula('MED_T(5;;[3])')
formula.topico = 'recepcao/topico'
# Formula('MED_T(5,,[3])')
# A = {'C':C}
# a = {'b':[[1,2,7]]}
# A['C'](arg for arg in a['b'][0])
while True:
    pass
