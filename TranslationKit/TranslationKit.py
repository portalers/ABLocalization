import os, re

class TransFileHandler:

    def __init__(self, sourcePath, destinationPath, resultPath, fileName, tranlationName='Tchinese') -> None:
        self.sourcePath = sourcePath
        self.destinationPath = destinationPath
        self.resultPath = resultPath
        self.fileName = fileName
        with open(self.destinationPath+self.fileName, 'r') as fn, open(self.sourcePath+self.fileName, 'r') as fo:
            self.rawDestinationFile = fn.readlines()
            self.rawSourceFile = fo.readlines()
        self.findHashPattern = 'translate '+tranlationName
        self.stringsBlockPattern = self.findHashPattern+' strings:\n'

    def findDiff(self, followOrginOrder=True) -> None:
        diffPath = 'diff/'
        diffPrefix = 'diff_'
        fnl = [line for line in self.rawDestinationFile if not line.isspace() and '#' not in line]
        fol = [line for line in self.rawSourceFile if not line.isspace() and '#' not in line]
        fnlHash = [re.sub(r"\s*"+re.escape(self.findHashPattern+' '), '' ,line)[:-2] for line in fnl if self.findHashPattern in line]
        folHash = [re.sub(r"\s*"+re.escape(self.findHashPattern+' '), '' ,line)[:-2] for line in fol if self.findHashPattern in line]
        fnlHashSet = set(fnlHash)
        folHashSet = set(folHash)
        diffResult = fnlHashSet-folHashSet
        followOriginOrderDiffResult = [fH for fH in fnlHash if fH in diffResult]

        if not os.path.isdir(self.resultPath+diffPath):
            os.makedirs(self.resultPath+diffPath, mode=0o777)
        if not os.path.isdir(self.resultPath+diffPath):
            os.makedirs(self.resultPath+diffPath, mode=0o777)

        with open(self.resultPath+diffPath+diffPrefix+self.fileName, 'w') as r:
            if followOrginOrder:
                for line in followOriginOrderDiffResult:
                    r.write(line+'\n')
            else:
                for line in sorted(list(diffResult)):
                    r.write(line+'\n')

    def initNewTransFile(self, stringsBlockOverride=False, dupHashOverride=True) -> None:
        fnRefinedDict = self.normalizeFile(self.rawDestinationFile, dupHashOverride)
        foRefinedDict = self.normalizeFile(self.rawSourceFile, dupHashOverride)
        
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

        with open(self.resultPath+self.fileName, 'w') as r:
            for l in outputContent:
                r.write(l)

    def normalizeFile(self, smudgyFile, dupHashOverride=True) -> dict:
        localRawFile = smudgyFile[:]
        newOriginDict = {'headerWords':[], 'orderedHash':[], 'content':[], 'duplicateHash':False, 'cotainStringsBlock':False, 'errorLog':{}}
        rawFileHash = [line for line in localRawFile if self.findHashPattern in line]
        newOriginDict['headerWords'].extend(localRawFile[:localRawFile.index(rawFileHash[0])])
        tmpContent = []

        #merge and condense 'translate [TranslationFile] strings' text blocks to the bottom of the file
        #there is still a chance that duplicate content in the block after merging, so a manual check is needed
        if rawFileHash.count(self.stringsBlockPattern):
            newOriginDict['cotainStringsBlock'] = True
        while rawFileHash.count(self.stringsBlockPattern) > 0:
            startPositionHash = rawFileHash.index(self.stringsBlockPattern)
            startPositionContent = localRawFile.index(self.stringsBlockPattern)
            try:
                while rawFileHash[startPositionHash+1] == self.stringsBlockPattern:
                    rawFileHash.pop(startPositionHash+1)
                    localRawFile.pop(startPositionContent)
                    nextPatterPosAtLocalRaw = localRawFile.index(self.stringsBlockPattern)+1
                    localRawFile.insert(startPositionContent, self.stringsBlockPattern)
                    localRawFile.pop(nextPatterPosAtLocalRaw)
                endPositionContent = localRawFile.index(rawFileHash[startPositionHash+1])
            except:
                endPositionContent = len(localRawFile)

            temLineCount = endPositionContent-startPositionContent
            tmpContent.extend(localRawFile[startPositionContent+1:endPositionContent])

            for i in range(temLineCount):
                localRawFile.pop(startPositionContent)
            rawFileHash.pop(startPositionHash)

        if tmpContent:
            rawFileHash.append(self.stringsBlockPattern)
            localRawFile.append('\n')
            localRawFile.append(self.stringsBlockPattern)
            for l in tmpContent:
                localRawFile.append(l)

        if len(rawFileHash) == len(set(rawFileHash)):
            for i in range(len(rawFileHash)-1):
                newOriginDict['content'].append({ rawFileHash[i]:localRawFile[localRawFile.index(rawFileHash[i]):localRawFile.index(rawFileHash[i+1])] })
            newOriginDict['content'].append({ rawFileHash[-1]:localRawFile[localRawFile.index(rawFileHash[-1]):] })
            newOriginDict['orderedHash'].extend(rawFileHash)
        else:
            newOriginDict['duplicateHash'] = True
            dupHash = [str(rawFileHash.count(dh))+'* '+dh[:-2] for dh in rawFileHash if rawFileHash.count(dh)>1]
            newOriginDict['errorLog'] = set(dupHash)

            #Only keep the lastest hash content.
            if dupHashOverride:
                print("You're using the 'dupHashOverride' mode, it will only keep the lastest updated content.")
                print(set(dupHash))
                print('All of the above are the dups you might want to clean from '+self.sourcePath+self.fileName)

                currentHash = rawFileHash[0]
                temData = []
                for line in newOriginDict['headerWords']:
                    localRawFile.pop(0)
                localRawFile.pop(0)
                for line in localRawFile:
                    if  self.findHashPattern in line:
                        temData.insert(0, currentHash)
                        newOriginDict['content'].append({currentHash:temData})
                        newOriginDict['orderedHash'].append(currentHash)
                        temData = []
                        currentHash = line
                        if line == self.stringsBlockPattern:
                            break
                    else:
                        temData.append(line)
                if not newOriginDict['cotainStringsBlock']:
                    temData.insert(0, currentHash)
                    newOriginDict['content'].append({currentHash:temData})
                    newOriginDict['orderedHash'].append(currentHash)
                    temData = []

                alreadyPopped = []
                for dh in rawFileHash:
                    if rawFileHash.count(dh)>1 and dh not in alreadyPopped:
                        alreadyPopped.append(dh)
                        while newOriginDict['orderedHash'].count(dh)>1:
                            popPosition = newOriginDict['orderedHash'].index(dh)
                            newOriginDict['orderedHash'].pop(popPosition)
                            newOriginDict['content'].pop(popPosition)
            else:
                print("Error, there are duplicate contents in this file and might cause malfunction(s) into renpy")
                print(set(dupHash))
                print("The dups are from "+self.sourcePath+self.fileName)
                print("Before cleaning them or choosing which line(s) to remain, the result is wrong.")
                newOriginDict['content'] = []
                newOriginDict['orderedHash'] = []
                newOriginDict['headerWords'] = []
                
        return newOriginDict