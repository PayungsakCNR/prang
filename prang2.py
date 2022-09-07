name1 = "Poramest"
name2 = "Nipon"
name3 = "Udomchai"

nameList = [name1,name2,name3]


def findLongestLenNameVal () :
    return len(max(nameList,key=len))

print(findLongestLenNameVal())

if(len(name1) != findLongestLenNameVal()):
    i = 0
    while i < (findLongestLenNameVal() - len(name1)):
        nameList[0] = nameList[0] + "\b"
        i += 1
if(len(name2) != findLongestLenNameVal()):
    i = 0
    while i < (findLongestLenNameVal() - len(name2)):
        nameList[1] = nameList[1] + "\b"
        i += 1
if(len(name3) != findLongestLenNameVal()):
    i = 0
    while i < (findLongestLenNameVal() - len(name3)):
        nameList[2] = nameList[2] + "\b"
        i += 1

#print(len(nameList[0]))
#print(len(nameList[1]))
#print(len(nameList[2]))

for i in range(findLongestLenNameVal()):
    for j in range(0,3):
        print(nameList[j][i])
    
