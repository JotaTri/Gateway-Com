import os
import glob
import inspect
import importlib


class Formula(object):

    def __init__(self, formula):
        self.known_formulas = self.get_known_formulas()
        self.formula = formula
        parsed_formulas, lixo = self.parse_formulas(formula)
        self.master_formula = self.get_master_formula(parsed_formulas)
        print self.master_formula.time_delta
        print type(self.master_formula.time_delta)
        print self.master_formula.service_type
        print type(self.master_formula.service_type)
        print self.master_formula.service_ids
        print type(self.master_formula.service_ids)

    def get_known_formulas(self):
        known_formulas = {}
        current_dir = os.path.join(os.path.dirname(os.path.abspath('formulas/*.py')))
        current_module_name = os.path.splitext(os.path.basename(current_dir))[0]
        for file in glob.glob(current_dir + "/*.py"):
             name = os.path.splitext(os.path.basename(file))[0]
             # Ignore __ files
             if name.startswith("__"):
                 continue
             module = importlib.import_module("." + name,package=current_module_name)
             for member in dir(module):
                 handler_class = getattr(module, member)
                 if handler_class and inspect.isclass(handler_class):
                     known_formulas[member] = handler_class
        return known_formulas

    def parse_formulas(self, formula):
        # print 'FORMULA=' + formula
        diciti = {'args':[]}
        args = ''
        temp = 1
        tempc = '('
        flag = False
        abrir = formula.find('(')
        fechar = formula.find(')')
        if abrir < fechar and abrir > 0:
            diciti['name'] = formula[:formula.find('(')]
            # print 'NOME ECONTRADO=' + diciti['name']
            formula = formula[abrir+temp:]
            while not flag:
                args, flag = self.parse_formulas(formula)
                # print '[' + diciti['name'] + ']' +'ARGS=' + str(args)
                if args and not isinstance(args, str):
                    diciti['args'].append(args)
                # print '[' + diciti['name'] + ']' +'DICIONANIO SO FAR = ' + str(diciti)
                temp = 2
                #formula = formula[formula.find(')')+temp:]
                try:
                    for arg in args['args']:
                        # print 'len'
                        # print(len(args['args']))
                        formula = formula[formula.find(')')+temp:]
                except:
                    formula = formula[formula.find(')')+temp:]

                if not args:
                    # print '[' + diciti['name'] + ']' + ' NOT ARGS'
                    flag = True
            return diciti, False
        else:
            # print formula
            if formula[fechar+1:].find(')') == -1:
                return formula[:formula.find(')')].split(','), True
            if formula[fechar:].find(')') == fechar + 1 or len(formula) == 1:
                print('FOIIII') #Entra aqui?
                return formula[formula.find(')'):], True
            if formula[formula.find(')')+1] == ',':
                return formula[:formula.find(')')].split(','), True
            else:
                return formula[:formula.find(')')].split(','), False
        # for char in formula:
        #     pass

    def get_master_formula(self, parsed_formulas):
        name = parsed_formulas['name']
        if len(parsed_formulas['args']) > 1:
            master_formula = self.known_formulas[name]()
            master_formula_sub_formuals = self.create_sub_formula(master_formula, parsed_formulas['args'])
        else:
            master_formula = self.known_formulas[name](parsed_formulas['args'][0])
        return master_formula


    def create_sub_formula(master_formula, args):
        array_formulas = []
        formula = {}
        for arg in args:
            formula['name'] = arg['name']
            if len(arg['args'])>0:
                formula = self.known_formulas[formula['name']]()
                sub_formula = create_sub_formula(formula, arg['args'])
            else:
                master_formula.values.append(sub_formula)
