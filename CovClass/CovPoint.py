from .CovBase import CovBase
from .CovBin import CovBin

import PrintTemplate

class CovPoint(CovBase):
    
    def __init__(self, name, df, start):
        super(CovPoint, self).__init__(name, df, start)
        
        self.cp_expr = df.cp_expr[start]
        self.cp_cond = df.cp_cond[start]
        self.cp_opt  = df.cp_opt[start]
        self.bin_dict = {}
        
        
    '''
    buildCP will build the coverpoint, iterating over the bins
    '''
    def buildCP(self):
        for i in range(self._start, self._len):
            
            # if we found another covergroup, the current covergroup has finished
            if self.cp_exist(i): return
            
            elif self._df.bin_name[i] != '':
                name = self._df.bin_name[i]
                # indicate cross coverage bin accordingly
                u_bin = CovBin(name, self._df, i, self._name == 'cross')
                self.bin_dict[name] = u_bin
                
    '''
    Prints the coverpoint.
    This will also go into each bins and print them
    '''
    def print(self):
        
        if self.cp_cond != '':
            cond = 'iff ({})'.format(self.cp_cond)
        else:
            cond = ''
        
        if self.cp_opt != '':
            opt = PrintTemplate.cp_op_str.format(opt = 'option.' + self.cp_opt + ';')
        else:
            opt = ''
            
        # special keywords for cp_name
        if self._name == 'cross':
            covp = 'cross'
        else:
            covp = self._name + ': coverpoint'
            
        bin_str = [self.bin_dict[b].print() for b in self.bin_dict]
        bin_str = ''.join(bin_str)
        
        str_ = PrintTemplate.cp_str.format(
            covp=covp, expr=self.cp_expr, cond=cond, opt=opt, bins=bin_str)
        
        return str_
    