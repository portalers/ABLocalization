import os, TranslationKit

oldSCPath = './SourceFile/TSR/rawOldSC/'
oldTCPath = './SourceFile/TSR/rawOldTC/'
newOriginSCPath = './SourceFile/TSR/newRawOriginSC/'
newOriginTCPath = './SourceFile/TSR/newRawOriginTC/'
resultSCPath = './Results/TSR/rawResultSC/'
resultTCPath = './Results/TSR/rawResultTC/'

if __name__ == "__main__":
    onlyfiles = [f for f in os.listdir(oldSCPath) if f.endswith('.rpy') and os.path.isfile(os.path.join(oldSCPath, f))]
    for f in onlyfiles:
        print(f)

        tmpTC = TranslationKit.TransFileHandler(sourcePath=oldTCPath, destinationPath=newOriginTCPath, resultPath=resultTCPath, fileName=f, tranlationName='Tchinese')
        tmpTC.findDiff(followOrginOrder=True)
        tmpTC.initNewTransFile(stringsBlockOverride=False, dupHashOverride=True)
        
        tmpSC = TranslationKit.TransFileHandler(sourcePath=oldSCPath, destinationPath=newOriginSCPath, resultPath=resultSCPath, fileName=f, tranlationName='Schinese')
        tmpSC.findDiff(followOrginOrder=True)
        tmpSC.initNewTransFile(stringsBlockOverride=False, dupHashOverride=True)
