from .CovBase import CovBase
from .CovPoint import CovPoint

import PrintTemplate

class CovGroup(CovBase):

    def __init__(self, name, df, start):
        super(CovGroup, self).__init__(name, df, start)
        
        self.cg_param = df.cg_param[start]
        self.cg_trigger = df.cg_trigger[start]
        self.cp_dict = {}
    
    '''
    buildCG will build the entire covergroup, iterating over the coverpoints,
    which internally will iterate over the bins
    '''
    def buildCG(self):
        for i in range(self._start, self._len):
            
            # if we found another covergroup, the current covergroup has finished
            if self.cg_exist(i): return
            
            elif self._df.cp_name[i] != '':
                name = self._df.cp_name[i]
                u_cp = CovPoint(name, self._df, i)
                u_cp.buildCP()
                self.cp_dict[name] = u_cp
    
    '''
    Print the covergroup.
    This will also go into each coverpoints and print them
    '''
    def print(self):
        
        if self.cg_param != '':
            param = '({})'.format(self.cg_param)
        else:
            param = ''
            
        try:
            # event trigger
            if (self.cg_trigger[0:2] == 'at'):
                trigger = '@' + self.cg_trigger[2:]
            # function
            elif (self.cg_trigger[0:4] == 'func'):
                trigger = 'with function sample' + self.cg_trigger[4:]
            else:
                trigger = ''
        except IndexError:
            trigger = '' 
        
        # iterate over the coverpoints and accumulate to a string
        cp_str = [self.cp_dict[cp].print() for cp in self.cp_dict]
        cp_str = ''.join(cp_str)
        
        str_ = PrintTemplate.cg_str.format(
            name=self._name, param=param, trigger=trigger, cp=cp_str)
        
        return str_
        
                