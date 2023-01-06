def writeChToFile(chPath, paragraphs):
    with open(chPath, 'w', newline='', encoding="utf-8") as f:
        #line = 'A righteous, honest man and a hard-worker. Though he comes from a common background, he is of extraordinary character and talent. As a genius who made his name known in the military academy, he possesses a sense of justice and other upright characteristics befitting a hero. He carries a special secret that he hasn’t revealed to anyone. "i want to explode." [asdoiaj;d] 1231231 [2342324]1231' 
        for p in paragraphs:
            line = p.text
            charCounter = 0
            numQuote = 0
            numAltQuote = 0
            endLine = False
            altActivated = False
            activated = False
            while charCounter < len(line):
                char = line[charCounter]
                f.write(char)
                if char == '"':
                    activated = True
                    numQuote += 1
                    if numQuote == 2:
                        f.write("\n")
                        activated = False
                        numQuote = 0
                if char == "'":
                    altActivated = True
                    numAltQuote += 1
                    if numAltQuote == 2:
                        f.write("\n")
                        altActivated = False
                        numAltQuote = 0
                if endLine: 
                    f.write("\n")
                    numAltQuote = 0
                    endLine = False
                if charCounter <= (len(line) - 2) and line[charCounter + 1] == " " and char == ".":
                    if not activated or not altActivated:
                        endLine = True
                if charCounter <= (len(line) - 2) and line[charCounter + 1] == '"' and char == "." and not activated:
                    endLine = True
                    if numQuote == 1:
                        endLine = False
                if charCounter <= (len(line) - 2) and line[charCounter + 1] == "'" and char == "." and not altActivated:
                    endLine = True
                    if numAltQuote == 1:
                        endLine = False   
                if charCounter <= (len(line) - 2) and line[charCounter + 1] == " " and char == "]":
                    endLine = True
                elif charCounter <= (len(line) - 2) and line[charCounter + 1] == "," and char == "]":
                    endLine = False 
                    #does nothing
                elif char == "]":
                    f.write('\n')
                if charCounter <= (len(line) - 2) and line[charCounter + 1] == "[" and char == " ":
                    f.write('\n')
                if charCounter == len(line) - 1:
                    f.write('\n')
                charCounter += 1
#chPath = 'C:/Users/CREEP/Downloads/python/novelRip/test'
#paragraphs = ''
