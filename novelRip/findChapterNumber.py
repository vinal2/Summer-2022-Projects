#string = "chapter 12: odfa;difa;idjo;aj;oaf"
#string2 = "chapter 1: odfa;difa;idjo;aj;oaf"

def findChNum(string):
    for n in range(len(string)):
        if string[n] == ":":
            substring = string[:n]
            chNum = substring[8:]
            return chNum

#print(findChNum(string))
#print(findChNum(string2))

