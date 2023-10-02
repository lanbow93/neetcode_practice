# Solution attempt before watching video (Lintcode)
# Results: Runtime 499ms - Beat UNKNOWN | Memory 5.15MB - Beat UNKOWN %
key = "@uth3ntic@t3K3y"
def encode(strs):
    return key.join(strs)

def decode(str):
    return str.split(key)