# Solution attempt before watching video
# Results: Runtime 58ms - Beat 38.47% | Memory 17.57 - Beat 13.31%
def isAnagram(s, t):
    if(len(s) != len(t)):
        return False
    return sorted(s) == sorted(t)

# Solution attempt after watching video
# Results: Runtime 46ms - Beat 88.67% | Memory 16.66 MB - Beat 96.73%
def postIsAnagram(s,t):
    if(len(s) != len(t)):
        return False
    sTable, tTable = {}, {}
    for i in range(len(s)):
        sTable[s[i]] = 1 + sTable.get(s[i], 0)
        tTable[t[i]] = 1 + tTable.get(t[i], 0)
    for key in sTable:
        if(sTable.get(key) != tTable.get(key)):
            return False
    return True
postIsAnagram("anagram", "nagaram")
postIsAnagram("rat", "car")