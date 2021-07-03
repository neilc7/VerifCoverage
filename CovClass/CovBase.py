class CovBase:
    
    def __init__(self, name, df, start):
        self._name  = name
        self._df    = df
        self._start = start
        self._len   = df.index.stop
        
    
    def cg_exist(self, line):
        if line == self._start: return False
        else:
            try: 
                return True if self._df.cg_name[line] != '' else False
            except KeyError:
                print("CovBase idx ERROR")
                return True
    
    
    def cp_exist(self, line):
        if line == self._start: return False
        else:
            try: 
                return True if self._df.cp_name[line] != '' else False
            except KeyError:
                print("CovBase idx ERROR")
                return True