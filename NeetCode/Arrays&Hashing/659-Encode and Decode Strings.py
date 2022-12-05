l = ["neet", "cod#e"]
def encode(l):
    string = ""
    for item in l:
        string += (str(len(item)) + "#" + item)

    return string

res = encode(l)
print(res)

def decode(string):
    i = 0
    ans = list()
    while i < len(string):
        j = i
        while string[j] != "#":
            j += 1
        s_len = int(string[i:j])
        ans.append(string[j + 1: j + 1 + s_len])
        i = j + 1 + s_len

    return ans

print(decode(res))


