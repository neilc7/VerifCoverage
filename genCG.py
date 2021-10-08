import pandas as pd
import sys
import CovClass


def main(ifile, ofile):
    df = pd.read_excel(ifile, engine = 'openpyxl', na_filter = False)
    cgdict = {}
    
    for row, cg in enumerate(df.cg_name) :
        if cg != '':
            u_cg = CovClass.CovGroup(cg, df, row)
            u_cg.buildCG()
            cgdict[cg] = u_cg
    
    fh = open(ofile, 'w')
    for cg in cgdict:
        print(cgdict[cg].print(), file=fh)
    print("done")
        

def print_help():
    print('Usage: ./genCG.py [input_file] [output_file]')
    print('e.g  : ./genCG.py xls/FuncCov.xlsx output/out.sv')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_help()
    else:
        main(sys.argv[1], sys.argv[2])