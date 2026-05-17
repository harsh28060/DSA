strs = ["flower","flow","floight"]

def longestCommonPrefix(strs):
    if not strs:
        return ""
    res=""
    for i in range(len(strs[0])):
        for j in strs[1:]:
            if i == len(j) or j[i] != strs[0][i]:
                return(res)
        res += strs[0][i]
    return res

print(longestCommonPrefix(strs))