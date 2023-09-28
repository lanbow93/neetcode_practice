# Solution attempt before watching video
# Results: Runtime 103ms - Beat 46.15% | Memory 16.98 MB - Beat 97.91%
def group_anagrams(strs):
    str_dictionary = {}
    
    for str in strs:
        currentSort = "".join(sorted(str))
        if currentSort in str_dictionary:
            str_dictionary[currentSort].append(str)
        else:
            str_dictionary[currentSort] = [str]
    sorted_list = []
    for key in str_dictionary:
        sorted_list.append(str_dictionary[key])
    return(sorted_list)

test1 = ["eat","tea","tan","ate","nat","bat"]
test2 = [""]
test3 = ["a"] 

group_anagrams(test3)

# Solution attempt after watching video
# Results: Runtime 97ms - Beat 69.08% | Memory 19.86 MB - Beat 65.00%

def post_group_anagrams(strs):
    str_dictionary = {}
    
    for str in strs:
        currentSort = "".join(sorted(str))
        if currentSort in str_dictionary:
            str_dictionary[currentSort].append(str)
        else:
            str_dictionary[currentSort] = [str]
    return str_dictionary.values()   # Realized I didn't need to iterate through 