import re

def findDiff(fNew, fOld, result, S0T1):
    pattern = ['translate Schinese ', 'translate Tchinese ']
    with open(fNew, 'r') as fn, open(fOld, 'r') as fo, open(result, 'w') as r:
        fnl = [line for line in fn.readlines() if not line.isspace() and '#' not in line]
        fol = [line for line in fo.readlines() if not line.isspace() and '#' not in line]
        fnlHash = set([re.sub(r"\s*"+re.escape(pattern[S0T1]), '' ,line)[:-2] for line in fnl if pattern[S0T1] in line])
        folHash = set([re.sub(r"\s*"+re.escape(pattern[S0T1]), '' ,line)[:-2] for line in fol if pattern[S0T1] in line])
        for line in sorted(list(fnlHash-folHash)):
            r.write(line+'\n')
    return sorted(list(fnlHash-folHash))