s = "abcabcbb"
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