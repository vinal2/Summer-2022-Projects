

chPath = 'C:/Users/CREEP/Downloads/python/novelRip/test'
with open(chPath, 'w', newline='', encoding="utf-8") as f:
    line = "aiosdj;adijaodiaf;diajs;dfioasdf"
    x = 1
    for char in line:
        f.write(char)
        if x == 10:
            f.write('\n')
        x += 1
    line = 'A righteous, honest man and a hard-worker. Though he comes from a common background, he is of extraordinary character and talent. As a genius who made his name known in the military academy, he possesses a sense of justice and other upright characteristics befitting a hero. He carries a special secret that he hasn’t revealed to anyone. "i want to explode." [asdoiaj;d] 1231231 [2342324]1231' 
    charCounter = 0
    numQuote = 0
    endLine = False
    
    while charCounter < len(line):
        char = line[charCounter]
        f.write(char)
        activated = False
        if char == '"':
            numQuote += 1
            if numQuote == 2:
                f.write("\n")
                activated = True
                numQuote = 0
        if endLine: 
            f.write("\n")
            endLine = False
        if charCounter <= (len(line) - 2) and line[charCounter + 1] == " " and char == ".":
            endLine = True
        elif charCounter <= (len(line) - 2) and line[charCounter + 1] == '"' and char == ".":
            endLine = True
            if numQuote == 1:
                endLine = False
        elif char == ".":
            f.write("\n")
        if charCounter <= (len(line) - 2) and line[charCounter + 1] == " " and char == "]":
            endLine = True
        elif charCounter <= (len(line) - 2) and line[charCounter + 1] == "," and char == "]":
            endLine = False 
            #does nothing
        elif char == "]":
            f.write('\n')
        if charCounter <= (len(line) - 2) and line[charCounter + 1] == "[" and char == " ":
            f.write('\n')
        charCounter += 1
def writeToFile(chPath, paragraphs, lineSize, line):
    with open(chPath, 'w', newline='', encoding="utf-8") as f:
        #for p in paragraphs:
            #line = p.text
            for char in line:
                f.write(char)
                if char == '.':
                    f.write('\n')
            f.write('\n')

def findPeriod(line):
    for char in line:
        if char == '.':
            f.write('\n')
#line = 'A righteous, honest man and a hard-worker. Though he comes from a common background, he is of extraordinary character and talent. As a genius who made his name known in the military academy, he possesses a sense of justice and other upright characteristics befitting a hero. He carries a special secret that he hasn’t revealed to anyone.' 
#writeToFile(chPath, 0, 0, line)       

'''             charCounter = 0
                numQuote = 0
                numAltQuote = 0
                endLine = False
                
                while charCounter < len(line):
                    char = line[charCounter]
                    f.write(char)
                    activated = False
                    altActivated = False
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
                        endLine = True
                    elif charCounter <= (len(line) - 2) and line[charCounter + 1] == '"' and char == "." and not activated:
                        endLine = True
                        if numQuote == 1:
                            endLine = False
                    elif char == ".":
                        f.write("\n")
                    if charCounter <= (len(line) - 2) and line[charCounter + 1] == " " and char == ".":
                        endLine = True
                    elif charCounter <= (len(line) - 2) and line[charCounter + 1] == "'" and char == "." and not altActivated:
                        endLine = True
                        if numAltQuote == 1:
                            endLine = False
                    elif char == ".":
                        f.write("\n")    
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
                    charCounter += 1'''