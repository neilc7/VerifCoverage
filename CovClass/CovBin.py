from .CovBase import CovBase
import PrintTemplate

class CovBin(CovBase):
    
    def __init__(self, name, df, start, cross=False):
        super(CovBin, self).__init__(name, df, start)
        
        self.bin_expr = df.bin_expr[start]
        self.bin_opt  = df.bin_opt[start]
        self.bin_cond = df.bin_cond[start]
        self.bin_cmt  = df.comment[start]
        self.cross    = cross
        
    def print(self):
        
        if self.bin_opt == '':
            bin_ = 'bins'
        elif self.bin_opt == 'wildcard':
            bin_ = 'wildcard bins'
        elif self.bin_opt == 'illegal':
            bin_ = 'illegal_bins'
        elif self.bin_opt == 'ignore':
            bin_ = 'ignore_bins'
        
        # for cross coverage, there will be syntax like binsof, intersect, etc
        expr = self.adj_cross_expr() if self.cross else self.bin_expr
        
        # add comment if exists
        if self.bin_cmt != '':
            cmt = '// ' + self.bin_cmt
        else:
            cmt = ''
        
        str_ = PrintTemplate.bin_str.format(
            bin=bin_, name=self._name, expr=expr, cond=self.bin_cond, cmt=cmt)
        
        return str_
    
    def adj_cross_expr(self):
        # step 1: split into conditions separated by &&
        conds = self.bin_expr.split('&&')
        
        # step 2: for each condition, split by '=='
        conds = [x.split('==') for x in conds]
        
        # step 3: for every condition, [0] = name, [1] = value
        str_ = ''
        for c in conds:
            if len(c) == 2:
                str_ += 'binsof({}) intersect {}'.format(c[0].strip(), c[1].strip())
            else:
                str_ += 'binsof({})'.format(c[0].strip())
            str_ += ' && '
        
        # delete the last '&&'
        return str_[:-4]
            
        