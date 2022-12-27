#Low tolerance, High efficiency, Low memory, Less cumulative error
#Can't not handle the 'translate [TranslationFile] strings' text block, manual work.
#And both old and new files need to exclude additional comment(s) and space(s) afterwards. eg. #YourTODOs or #YourRemindings. Because of using the row number as data index.
import mergeStringsBlock

def initNewTransFile(fNew, fOld, initResult, S0T1):

    pattern = ['translate Schinese strings:\n', 'translate Tchinese strings:\n']

    with open(fNew, 'r') as fn, open(fOld, 'r') as fo, open(initResult, 'w') as r:

        fnlOrigin = fn.readlines()
        fnl = [line for line in fnlOrigin if not line.isspace()]
        fol = [line for line in fo.readlines() if not line.isspace()]
        newUpdateTime = fnl.pop(0)
        fol.pop(0)
        manualPart = fnlOrigin[fnlOrigin.index(pattern[S0T1]):]
        fnl.index(pattern[S0T1])
        fol.index(pattern[S0T1])

        for i in range(1, fnl.index(pattern[S0T1]), 4):
            try:
                fnl[i+2] = fol[fol.index(fnl[i])+2]
            except:
                pass

        for i in range(fnl.index(pattern[S0T1]), 0, -2):
            fnl.insert(i, '\n')

        fnl.insert(0, '\n')
        fnl.insert(0, newUpdateTime)
        initResult_tmp = fnl[:fnl.index(pattern[S0T1])]
        initResult_tmp.extend(manualPart)

        for line in initResult_tmp:
            r.write(line)

#High tolerance, Low efficiency, High memory, High cumulative error
#For lazy tails, but still need to do a manual check to the 'translate [TranslationFile] strings' text block at the bottom
def initNewTransFileHiTole(fNew, fOld, initResult, S0T1, stringsBlockOverride=False):
    with open(fNew, 'r') as fn, open(fOld, 'r') as fo, open(initResult, 'w') as r:
        fnOrigin = fn.readlines()
        foOrigin = fo.readlines()
        fnRefinedDict = mergeStringsBlock.normalizeFile(fnOrigin, S0T1)
        foRefinedDict = mergeStringsBlock.normalizeFile(foOrigin, S0T1)

        if fnRefinedDict['cotainStringsBlock'] and not stringsBlockOverride:
            workScope = len(fnRefinedDict['orderedHash'])-1
        else:
            workScope = len(fnRefinedDict['orderedHash'])

        for i in range(workScope):
            try:
                pos = foRefinedDict['orderedHash'].index(fnRefinedDict['orderedHash'][i])
                fnRefinedDict['content'][i][fnRefinedDict['orderedHash'][i]] = foRefinedDict['content'][pos][foRefinedDict['orderedHash'][pos]]
            except:
                pass

        outputContent = []
        outputContent.extend(fnRefinedDict['headerWords'])

        for i in range(len(fnRefinedDict['orderedHash'])):
            outputContent.extend(fnRefinedDict['content'][i][fnRefinedDict['orderedHash'][i]])
        for l in outputContent:
            r.write(l)
