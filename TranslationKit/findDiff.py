import re

def findDiff(fNew, fOld, diffResult, S0T1, followOrginOrder=True):

    pattern = ['translate Schinese ', 'translate Tchinese ']

    with open(fNew, 'r') as fn, open(fOld, 'r') as fo, open(diffResult, 'w') as r:

        fnl = [line for line in fn.readlines() if not line.isspace() and '#' not in line]
        fol = [line for line in fo.readlines() if not line.isspace() and '#' not in line]
        fnlHash = [re.sub(r"\s*"+re.escape(pattern[S0T1]), '' ,line)[:-2] for line in fnl if pattern[S0T1] in line]
        folHash = [re.sub(r"\s*"+re.escape(pattern[S0T1]), '' ,line)[:-2] for line in fol if pattern[S0T1] in line]
        fnlHashSet = set(fnlHash)
        folHashSet = set(folHash)
        diffResult = fnlHashSet-folHashSet
        followOriginOrderDiffResult = [fH for fH in fnlHash if fH in diffResult]

        if followOrginOrder:
            for line in followOriginOrderDiffResult:
                r.write(line+'\n')
        else:
            for line in sorted(list(diffResult)):
                r.write(line+'\n')
