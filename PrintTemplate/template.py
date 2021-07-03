# covergroup
cg_str = '''\
covergroup {name} {param} {trigger};
{cp}\
endgroup
'''

# coverpoint
cp_str = '''\
    {covp} {expr} {cond} {{ {bins} {opt}
    }}
'''

# options for coverpoint
cp_op_str = '''
        {opt}\
'''

# bins
bin_str = '''
        {bin} {name} = {expr} {cond}; {cmt}\
'''