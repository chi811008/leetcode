s = "abcabcbb"
# method 1
mapping = dict()
max_len = slow = 0

for fast in range(len(s)):
    c_num = mapping.get(s[fast], 0)
    # put c in dict
    mapping[s[fast]] = c_num + 1
    # if c in mapping
    if c_num:
        while mapping[s[fast]] > 1:
            mapping[s[slow]] = mapping.get(s[slow]) - 1
            slow += 1
    # if c not in mapping
    else:
        # count len
        count = fast - slow + 1
        if count > max_len:
            max_len = count
print(max_len)

# method 2
right, left = 0, 0
ele = dict()
max_ele = 0

while right <= (len(s) - 1): #8
    print(f"left:{left}, right:{right}")
    if ele.get(s[right], 0) == 0:
        ele[s[right]] = ele.get(s[right], 0) + 1
        print(ele)

    else:
        ele[s[right]] = ele.get(s[right], 0) + 1
        print(ele)
        while s[right] != s[left]:
            ele[s[left]] -= 1
            left += 1
            print(ele)
            print(f"left:{left}, right:{right}")
        ele[s[left]] -= 1
        left += 1
        print(f"left:{left}, right:{right}")
        print(ele)
    right += 1

    tmp_len = right - left
    if tmp_len > max_ele:
        max_ele = tmp_len
    print(max_ele)