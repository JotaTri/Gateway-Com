"MED(MAX_T(1,,[1]),MED(MAX_T(1,,[1]),MIX_T(1,,[2])),MIX_T(1,,[2]))"
def parse_formulass(self, string, flag = True):
    coisa = ''
    dicti = {'args' : []}
    for idx, char in enumerate(string):
        if char == ')':
            print 'coisa' + coisa
            return coisa.split(',')
        elif char != '(':
            coisa += char
        else:
            args = self.parse_formulas(string[len(coisa)+1:], flag=False)
            # args, idx2 = self.parse_formulas(string[idx+1:])
            dicti['args'].append(args)
            dicti['nome'] = coisa
            print dicti
            # if :
            return dicti


def parse_formulass(self, formula):
    array_formulas = []
    formula_composition = {'name': '', 'args':[]}
    for idx, char in enumerate(formula):
        if char == ')' or char == ',':
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
                    if insub:
                        insub = False
                        argumento += item
                        formula_composition['args'].append(argumento)
                        argumento = ''
                        print('ARGUMENTO ADICIONADO: ' + str(formula_composition['args']))
                    else:
                        formula_composition['args'].append(argumento)
                        argumento = ''
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
    return list(reversed(array_formulas))
    # master_formula = formula.split('(')[0]
    # master_formula_args = []
    # for item in formula[len(master_formula):].split(','):
    #     print item
