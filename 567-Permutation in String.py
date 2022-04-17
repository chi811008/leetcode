s1 = "ab"
s2 = "eidbaooo"

right = 0
left = 0
s1_dic = dict()
s2_dic = dict()

for c1 in s1:
    s1_dic[c1] = (s1_dic.get(c1, 0) + 1) 
print(s1_dic)
while right < len(s2):
    if s1_dic.get(s2[right]):
        s2_dic[s2[right]] = (s2_dic.get(s2[right], 0) + 1)
        i = 0
        for k, v in s2_dic.items():
            print(k, v)
            if s1_dic.get(k, 0) != v:
                break
            i += 1
            print(i)
        if i == len(s2_dic) and i >= len(s1_dic):
            print(True)
            print(s2[left:right])

    else:
        left += 1
    right += 1
    print(s2_dic)