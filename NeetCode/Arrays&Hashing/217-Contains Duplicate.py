nums = [1,2,3,1]
hashset = set()
for n in nums:
    if n in hashset:
        return True
    hashset.add(n)
return False