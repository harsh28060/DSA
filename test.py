def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(strs):
    res,i=[],0
    while i < len(strs):
        j = i
        while strs[j] != "#":
            j += 1
        lengh = int(strs[i:j])
        res.append(strs[j+1:j+1+lengh])
        i = j+1+lengh
    return res


strs = ["Hello","World"]
print(encode(strs))
print(decode(encode(strs)))
