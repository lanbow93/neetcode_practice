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

isPalindrome(test1)