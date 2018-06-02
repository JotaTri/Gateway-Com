
class Formula(object):
    def __init__(self, formula):
        self.formula = formula
        self.master_formula = self.get_master_formula(formula)
        #self.sub_formulas = self.get_sub_formulas(formula.split('(')[1:])
        pass

    def get_master_formula(self, formula):
        array_formulas = []
        formula_composition = {'name': '', 'args':[]}
        for idx, char in enumerate(formula):
            if char == ')':
                formula_composition['name'] = ''
            elif char != '(':
                formula_composition['name'] += char
            else:
                print('NOME ACHADO:' + formula_composition['name'])
                argumento = ''
                insub = False
                for item in formula[idx+1:]:
                    if item == '(':
                        insub = True
                        argumento += item
                    elif item == ')':
                        argumento += item
                        formula_composition['args'].append(argumento)
                        argumento = ''
                        if insub:
                            insub = False
                            print('ARGUMENTO ADICIONADO: ' + str(formula_composition['args']))
                        else:
                            print 'APPENDED:' + str(formula_composition)
                            array_formulas.append(formula_composition.copy())
                            formula_composition = {'name': '', 'args':[]}
                            break
                    elif item == ',':
                        if insub:
                            argumento += item
                            pass
                        else:
                            formula_composition['args'].append(argumento)
                            argumento = ''
                            print('ARGUMENTO ADICIONADO: ' + str(formula_composition['args']))
                    else:
                        argumento += item

        for item in array_formulas:
            print 'item=' + str(item)
        # master_formula = formula.split('(')[0]
        # master_formula_args = []
        # for item in formula[len(master_formula):].split(','):
        #     print item

    def get_sub_formulas(self, splitted_formula):
        sub_formulas = {}
        for item in splitted_formula:
            if ')' in item:
                item.split(',')
                sub_formulas
