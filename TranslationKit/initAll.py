import os, TranslationKit

pathResource = './TSR/resources(old)/'
pathDestination = './TSR/destination(new)/'
# resultTCPath = './TSR/results/'
resultTCPath = './TSR/results_MTenable/'

not2TransFile = ['define.rpy', 'options.rpy', 'screens.rpy']

if __name__ == "__main__":
    resourceFiles = [f for f in os.listdir(pathResource) if f.endswith('.rpy') and os.path.isfile(os.path.join(pathResource, f)) and f not in not2TransFile]
    destinationFiles = [f for f in os.listdir(pathDestination) if f.endswith('.rpy') and os.path.isfile(os.path.join(pathDestination, f)) and f not in not2TransFile]
    matchFiles = set(resourceFiles) & set(destinationFiles)

    for f in matchFiles:
        print(f)
        tmpTC = TranslationKit.TransFileHandler(sourcePath=pathResource, destinationPath=pathDestination, resultPath=resultTCPath, fileName=f, tranlationName='Tchinese')
        tmpTC.findDiff(followOrginOrder=True)
        # tmpTC.initNewTransFile(stringsBlockOverride=False, dupHashOverride=True, editFullwidthPunctuation=True, useMT=False)
        tmpTC.initNewTransFile(stringsBlockOverride=False, dupHashOverride=True, editFullwidthPunctuation=True, useMT=True)
        del tmpTC
