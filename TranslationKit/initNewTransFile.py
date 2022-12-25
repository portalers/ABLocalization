#Can't not handle the 'translate [TranslationFile] strings' text block, manual work.
#And both old and new files need to exclude additional comment(s) and space(s) afterwards. eg. #YourTODOs or #YourRemindings. Because of using the row number as data index.
import findDiff, re

fNew = 'new_nikroute3.rpy'
fOld = 'old_nikroute3.rpy'
diffResult = 'diff_result.txt'
initResult = 'init_result.rpy'


diffHash = findDiff.findDiff(fNew, fOld, diffResult, 0)

with open(fNew, 'r') as fn, open(fOld, 'r') as fo, open(initResult, 'w') as r:
    fnlOrigin = fn.readlines()
    fnl = [line for line in fnlOrigin if not line.isspace()]
    fol = [line for line in fo.readlines() if not line.isspace()]
    newUpdateTime = fnl.pop(0)
    oldUpdateTime = fol.pop(0)
    manualPart = fnlOrigin[fnlOrigin.index('translate Schinese strings:\n'):]

    fnl.index('translate Schinese strings:\n')
    fol.index('translate Schinese strings:\n')
    for i in range(1, fnl.index('translate Schinese strings:\n'), 4):
        try:
            fnl[i+2] = fol[fol.index(fnl[i])+2]
        except:
            pass
    
    for i in range(fnl.index('translate Schinese strings:\n'), 0, -2):
        fnl.insert(i, '\n')

    
    fnl.insert(0, '\n')
    fnl.insert(0, newUpdateTime)
    
    initResult_tmp = fnl[:fnl.index('translate Schinese strings:\n')]
    initResult_tmp.extend(manualPart)
    for line in initResult_tmp:
        r.write(line)