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

    def initNewTransFile(self, stringsBlockOverride=False, dupHashOverride=True, editFullwidthPunctuation=True) -> None:
        fnRefinedDict = self.normalizeFile(self.rawDestinationFile, dupHashOverride, editFullwidthPunctuation)
        foRefinedDict = self.normalizeFile(self.rawSourceFile, dupHashOverride, editFullwidthPunctuation)
        
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

    def normalizeFile(self, smudgyFile, dupHashOverride=True, editFullwidthPunctuation=True) -> dict:
        localRawFile = smudgyFile.copy()
        newOriginDict = {'headerWords':[], 'orderedHash':[], 'content':[], 'duplicateHash':False, 'cotainStringsBlock':False, 'errorLog':{}}
        errorWords = [
            "You're using the 'dupHashOverride' mode, it will only keep the lastest updated content.",
            'All of the above are the dups you might want to clean from '+self.sourcePath+self.fileName,
            "Error, there are duplicate contents in this file and might cause malfunction(s) into renpy.",
            "The dups are from "+self.sourcePath+self.fileName,
            "Before cleaning them or choosing which line(s) to remain, the result is empty."
            ]

        temData = []
        currentHash = ""
        for line in localRawFile:
            if  self.findHashPattern in line:
                if currentHash == "":
                    newOriginDict['headerWords'] = temData
                else:
                    temData.insert(0, currentHash)
                    newOriginDict['content'].append({currentHash:temData})
                    newOriginDict['orderedHash'].append(currentHash)
                temData = []
                currentHash = line
            else:
                temData.append(line)
        temData.insert(0, currentHash)
        newOriginDict['content'].append({currentHash:temData})
        newOriginDict['orderedHash'].append(currentHash)
        temData = []

        while newOriginDict['orderedHash'].count(self.stringsBlockPattern) > 0:
            pos = newOriginDict['orderedHash'].index(self.stringsBlockPattern)
            temData.extend(newOriginDict['content'].pop(pos)[self.stringsBlockPattern])
            newOriginDict['orderedHash'].pop(pos)
        if temData:
            newOriginDict['cotainStringsBlock'] = True
            newOriginDict['content'].append({self.stringsBlockPattern:temData})
            newOriginDict['orderedHash'].append(self.stringsBlockPattern)
        del temData
        del currentHash
        
        if len(newOriginDict['orderedHash']) != len(set(newOriginDict['orderedHash'])):
            dupHashMsg = str(set([str(newOriginDict['orderedHash'].count(hh))+'* '+hh for hh in newOriginDict['orderedHash'] if newOriginDict['orderedHash'].count(hh)>1]))
            if dupHashOverride:
                for hh in newOriginDict['orderedHash'].copy():
                    while newOriginDict['orderedHash'].count(hh) > 1:
                        pos = newOriginDict['orderedHash'].index(hh)
                        newOriginDict['content'].pop(pos)
                        newOriginDict['orderedHash'].pop(pos)
                print(errorWords[0], dupHashMsg, errorWords[1], sep='\n')
            else:
                newOriginDict['duplicateHash'] = True
                print(errorWords[2], dupHashMsg, errorWords[3], errorWords[4], sep='\n')
                newOriginDict['headerWords'] = [errorWords[2]+'\n', dupHashMsg+'\n', errorWords[3]+'\n', errorWords[4]+'\n']
                newOriginDict['orderedHash'] = []
                newOriginDict['content'] = []

        if not newOriginDict['duplicateHash'] and editFullwidthPunctuation:
            for i in range(len(newOriginDict['orderedHash'])-1):
                newOriginDict['content'][i][newOriginDict['orderedHash'][i]] = self.editFuwiPunc(newOriginDict['content'][i][newOriginDict['orderedHash'][i]])
        return newOriginDict

    def editFuwiPunc(self, contentLines):
        # '!':'！', ':':'：', ',':':'、', hash tag(#) without following-a-space can't easily replace cuz of the syntax below, manually check please.
        # define earned_points_info = _("[points]{image=points.png} 贏得點數")
        # g "我很高興看到你 [earned_points_info!ti] "
        # $ percent = 100.0 * points / max_points
        # g "我百分之 [percent:.2] 喜歡你！"
        # "{color=#f00}紅色{/color}, {color=#00ff00}綠色{/color}, {color=#0000ffff}藍色{/color}"
        # 角色是???的也要人工看一下
        contentLines = contentLines.copy()
        targetPairs = {'...':'……',
            '-':'──',
            ',':'，',
            '．':'。',
            ':':'：',
            '!':'！',
            ':':'：',
            '?':'？'
        }
        hardToFind = {'..':'……',
        '.':'。',
        '…':'……',
        '—':'──',
        }
        mayDupPunc = ['…', '—', '─']

        nearestUpSideComment = []
        validLineCount = []
        addDoubleQuotes = False
        ncPos = -1
        for i in range(len(contentLines)):
            if not contentLines[i].isspace() and contentLines[i].lstrip().startswith('#') and '# TODO' not in contentLines[i] and '# game' not in contentLines[i]:
                nearestUpSideComment.append(i)
            if not contentLines[i].isspace() and not contentLines[i].lstrip().startswith('#') and '$ ' not in contentLines[i] and '[' not in contentLines[i] and self.findHashPattern not in contentLines[i]:
                validLineCount.append(i)
                for targ in targetPairs.keys():
                    contentLines[i] = contentLines[i].replace(targ, targetPairs[targ])

                #hardToFind
                contentLines[i] = contentLines[i].replace('..', hardToFind['..'])
                contentLines[i] = contentLines[i].replace('？？？', '???', 1)

                try:
                    endPos = contentLines[i].rindex('"')
                    if contentLines[i][endPos-1] == '.':
                        contentLines[i] = contentLines[i][:endPos-1]+hardToFind['.']+contentLines[i][endPos:]
                except:
                    pass
                
                for mdp in mayDupPunc:
                    contentLines[i] = self.findDupPunc(mdp, contentLines[i])
                
        if nearestUpSideComment and validLineCount:
            for nc in nearestUpSideComment:
                if nc < validLineCount[0]:
                    ncPos = nc
        if ncPos != -1:
            try:
                if contentLines[ncPos].index('\\"') != contentLines[ncPos].rindex('\\"'):
                    addDoubleQuotes = True
            except:
                pass
        if addDoubleQuotes:
            try:
                if '“' in contentLines[validLineCount[0]]  or '”' in contentLines[validLineCount[0]]:
                    tmplist = list(contentLines[validLineCount[0]])
                    itsPos = []
                    popCounter = ''.join(tmplist).count('\\"')
                    for i in range(popCounter):
                        popPos = ''.join(tmplist).index('\\"')
                        itsPos.append(popPos+i)
                        tmplist.pop(popPos)
                        tmplist.pop(popPos)

                    tmplist.reverse()

                    if tmplist[tmplist.index('"')+1] == '“' or tmplist[tmplist.index('"')+1] == '\\':
                        tmplist[tmplist.index('"')+1] = '”'
                    elif tmplist[tmplist.index('"')+1] != '”' and tmplist[tmplist.index('"')+1] != ' ' :
                        tmplist.insert(tmplist.index('"')+1, '”')

                    tmpPopPos = tmplist.index('"')
                    tmplist.pop(tmpPopPos)

                    if tmplist[tmplist.index('"')-1] == '”' or tmplist[tmplist.index('"')-1] == '\\':
                        tmplist[tmplist.index('"')-1] = '“'
                    elif tmplist[tmplist.index('"')-1] != '“' and tmplist[tmplist.index('"')-1] != ' ' :
                        tmplist.insert(tmplist.index('"'), '“')
                        insertPosOffset = True

                    tmplist.insert(tmpPopPos, '"')
                    tmplist.reverse()

                    if insertPosOffset:
                        itsPos = [itps+1 for itps in itsPos]

                    for itps in itsPos:
                        itsPos.insert(itps, '\\')
                        itsPos.insert(itps, '"')
                        
                    contentLines[validLineCount[0]] = ''.join(tmplist)
                else:
                    if contentLines[validLineCount[0]].index('\\"') != contentLines[validLineCount[0]].rindex('\\"'):
                        contentLines[validLineCount[0]] = contentLines[validLineCount[0]][:contentLines[validLineCount[0]].index('\\"')]+'“'+contentLines[validLineCount[0]][contentLines[validLineCount[0]].index('\\"')+2:contentLines[validLineCount[0]].rindex('\\"')]+'”'+contentLines[validLineCount[0]][contentLines[validLineCount[0]].rindex('\\"')+2:]
                    else:
                        tmplist = list(contentLines[validLineCount[0]])
                        itsPos = []
                        popCounter = ''.join(tmplist).count('\\"')
                        for i in range(popCounter):
                            popPos = ''.join(tmplist).index('\\"')
                            itsPos.append(popPos+i)
                            tmplist.pop(popPos)
                            tmplist.pop(popPos)

                        tmplist.reverse()
                        tmplist.insert(tmplist.index('"')+1, '”')

                        tmpPopPos = tmplist.index('"')
                        tmplist.pop(tmpPopPos)

                        tmplist.insert(tmplist.index('"'), '“')

                        tmplist.insert(tmpPopPos, '"')
                        tmplist.reverse()

                        itsPos = [itps+1 for itps in itsPos]
                        for itps in itsPos:
                            itsPos.insert(itps, '\\')
                            itsPos.insert(itps, '"')
                            
                        contentLines[validLineCount[0]] = ''.join(tmplist)
            except:
                pass
        return contentLines

    def findDupPunc(self, puncPattern, puncSourceLine):

        allMatches = [(m.start(0), m.end(0)) for m in re.finditer(puncPattern, puncSourceLine)]
        if allMatches:
            preMarked = ()
            singleMarks = []
            counter = 0
            tmplist = list(puncSourceLine)
            for p in allMatches:
                if not preMarked or counter == 2:
                    preMarked = p
                    counter = 1
                elif p[0] == preMarked[1] and counter < 2:
                    preMarked = p
                    counter += 1
                else:
                    singleMarks.append(preMarked)
                    preMarked = p
            if counter < 2:
                singleMarks.append(allMatches[-1])
            singleMarks.reverse()
            for sm in singleMarks:
                tmplist.insert(sm[1], puncPattern)

            return ''.join(tmplist)
        else:
            return puncSourceLine
