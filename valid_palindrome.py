# A-Z: ASCII values 65 to 90
# a-z: ASCII values 97 to 122
# 0-9: ASCII values 48 to 57
# Solution attempt before watching video 
# Results: Runtime 78ms - Beat 5.15% | Memory 27.98 - Beat 7.59%
test1 = "A man, a plan, a canal: Panama"
def isPalindrome(s):
    strippedArray = []
    s = s.lower()
    reversedArray = ['' for i in s]
    for index, letter in enumerate(s):
        ascii_value = ord(letter)
        if (97 <= ascii_value <= 122) or (48 <= ascii_value <= 57):
            strippedArray.append(letter)
            reversedArray[(len(s)-1) - index] = letter
        else:
            strippedArray.append("")
    return "".join(reversedArray) == "".join(strippedArray)

# Solution attempt after watching video 
# Results: Runtime 75ms - Beat 6.40% | Memory 17.04 - Beat 76.19%
def postIsPanindrome(s):
    l_pointer = 0
    r_pointer = len(s) -1
    
    def isAlphaNumeric(char):
        return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')
    while(l_pointer < r_pointer):
        while (not isAlphaNumeric(s[l_pointer]) and l_pointer < r_pointer):
            l_pointer += 1
        while (not isAlphaNumeric(s[r_pointer]) and l_pointer < r_pointer):
            r_pointer -= 1
        if(s[l_pointer].lower() != s[r_pointer].lower()):
            return False
        l_pointer += 1
        r_pointer -= 1
        
    return True
print(postIsPanindrome(test1))
# Altered Solution Attempt
# Results: Runtime 66ms - Beat 12.17% | Memory 17.04 - Beat 76.19%
def isPalindrome(s):
    l_pointer = 0
    r_pointer = len(s) - 1

    while l_pointer < r_pointer:
        while l_pointer < r_pointer and not ('a' <= s[l_pointer] <= 'z' or 'A' <= s[l_pointer] <= 'Z' or '0' <= s[l_pointer] <= '9'):
            l_pointer += 1

        while l_pointer < r_pointer and not ('a' <= s[r_pointer] <= 'z' or 'A' <= s[r_pointer] <= 'Z' or '0' <= s[r_pointer] <= '9'):
            r_pointer -= 1

        if s[l_pointer].lower() != s[r_pointer].lower():
            return False

        l_pointer += 1
        r_pointer -= 1

    return True