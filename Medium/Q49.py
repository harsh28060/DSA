
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
def groupAnagrams(strs):
    hash = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in hash:
            hash[key] = []
        hash[key].append(word)
    
    return hash.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

# solve this again