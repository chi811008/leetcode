l = ["neet", "cod#e"]
def encode(l):
    res = ""
    for s in l:
        res += str(len(s)) + "#" + s
    return res
print(encode(l))

string = "4#neet5#cod#e"
def decode(string):
    i = 0
    ans = list() 
    while i < len(string):
        j = i
        if string[j] != "#":
            j += 1
        s_len = int(string[i:j])
        ans.append(string[j + 1: j + 1 + s_len])
        i += (j + 1 + s_len)
    return ans
print(decode(string))
