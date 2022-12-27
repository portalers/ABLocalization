def normalizeFile(rawFile, S0T1):
    localRawFile = rawFile[:]
    pattern = ['translate Schinese ', 'translate Tchinese ']
    tmpContent = []
    newOriginDict = {'headerWords':[], 'orderedHash':[], 'content':[], 'duplicateHash':False, 'cotainStringsBlock':False}

    rawFileHash = [line for line in localRawFile if pattern[S0T1] in line]
    if rawFileHash.count(pattern[S0T1]+'strings:\n'):
        newOriginDict['cotainStringsBlock'] = True
    newOriginDict['headerWords'].extend(localRawFile[:localRawFile.index(rawFileHash[0])])

    #merge and condense 'translate [TranslationFile] strings' text blocks to the bottom of the file
    #there is still a chance that duplicate content in the block after merging, so a manual check is needed
    while rawFileHash.count(pattern[S0T1]+'strings:\n') > 0:
        startPositionHash = rawFileHash.index(pattern[S0T1]+'strings:\n')
        startPositionContent = localRawFile.index(pattern[S0T1]+'strings:\n')
        try:
            while rawFileHash[startPositionHash+1] == pattern[S0T1]+'strings:\n':
                rawFileHash.pop(startPositionHash+1)
                localRawFile.pop(startPositionContent)
                nextPatterPosAtLocalRaw = localRawFile.index(pattern[S0T1]+'strings:\n')+1
                localRawFile.insert(startPositionContent, pattern[S0T1]+'strings:\n')
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
        rawFileHash.append(pattern[S0T1]+'strings:\n')
        localRawFile.append('\n')
        localRawFile.append(pattern[S0T1]+'strings:\n')
        for l in tmpContent:
            localRawFile.append(l)

    for i in range(len(rawFileHash)-1):
        newOriginDict['content'].append({ rawFileHash[i]:localRawFile[localRawFile.index(rawFileHash[i]):localRawFile.index(rawFileHash[i+1])] })
    newOriginDict['content'].append({ rawFileHash[-1]:localRawFile[localRawFile.index(rawFileHash[-1]):] })

    newOriginDict['orderedHash'].extend(rawFileHash)
    if len(rawFileHash) != len(set(rawFileHash)):
        newOriginDict['duplicateHash'] = True
        dupHash = [str(rawFileHash.count(dh))+'* '+dh[:-2] for dh in rawFileHash if rawFileHash.count(dh)>1]
        print("Error, there is/are duplicate content in this file and might cause malfunction(s) into renpy")
        print(set(dupHash))
        print("Before cleaning them or choosing which line(s) to keep, the initial file is not correct.")

    return newOriginDict
