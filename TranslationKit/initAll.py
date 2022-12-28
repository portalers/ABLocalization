import os ,findDiff, initNewTransFile

sysFiles = ['.DS_Store', '.AppleDouble', '.LSOverride', 'Thumbs.db', 'Thumbs.db:encryptable', 'ehthumbs.db', 'ehthumbs_vista.db', 'Desktop.ini', 'desktop.ini']

newOriginSCPath = './SourceFile/TSR/newRawOriginSC/'
newOriginTCPath = './SourceFile/TSR/newRawOriginTC/'
oldSCPath = './SourceFile/TSR/rawOldSC/'
oldTCPath = './SourceFile/TSR/rawOldTC/'
resultSCPath = './Results/TSR/rawResultSC/'
resultTCPath = './Results/TSR/rawResultTC/'

diffPath = 'diff/'
diffPrefix = 'diff_'

if __name__ == "__main__":
    
    onlyfiles = [f for f in os.listdir(oldSCPath) if os.path.isfile(os.path.join(oldSCPath, f)) and f not in sysFiles and not f.startswith('~') and not f.startswith('.') and not f.endswith('.bak')]

    for f in onlyfiles:
        print(f)
        findDiff.findDiff(fNew=newOriginSCPath+f, fOld=oldSCPath+f, diffResult=resultSCPath+diffPath+diffPrefix+f, S0T1=0, followOrginOrder=True)
        findDiff.findDiff(fNew=newOriginTCPath+f, fOld=oldTCPath+f, diffResult=resultTCPath+diffPath+diffPrefix+f, S0T1=1, followOrginOrder=True)
        initNewTransFile.initNewTransFileHiTole(fNew=newOriginSCPath+f, fOld=oldSCPath+f, initResult=resultSCPath+f, S0T1=0, stringsBlockOverride=False)
        initNewTransFile.initNewTransFileHiTole(fNew=newOriginTCPath+f, fOld=oldTCPath+f, initResult=resultTCPath+f, S0T1=1, stringsBlockOverride=False)
