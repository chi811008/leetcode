height = [0,1,0,2,1,0,1,3,2,1,2,1]
l, r = 0, len(height) - 1
maxl, maxr = height[l], height[r]
total_water = 0
while l < r:
    if height[l] <= height[r]:
        print(f"pointer now is {l}")
        print(f"min height: {min(maxl, maxr)}")
        print(f"now height: {height[l]}")
        trap_water = (min(maxl, maxr) - height[l])
        print(f"trap water {trap_water}")
        total_water += trap_water if trap_water > 0 else 0
        print(f"total water {total_water}")
        l += 1
        maxl = max(maxl, height[l])
    else:
        print(f"pointer now is {r}")
        print(f"min height: {min(maxl, maxr)}")
        print(f"now height: {height[r]}")
        trap_water = min(maxl, maxr) - height[r]
        print(f"trap water: {trap_water}")
        total_water += trap_water if trap_water > 0 else 0
        print(f"total water: {total_water}")
        r -= 1
        maxr = max(maxr, height[r])
print(total_water)

height = [1]
l, r = 0, len(height) - 1
maxl, maxr = height[l], height[r]
total_water = 0
while l < r:
    if height[l] <= height[r]:
        trap_water = (min(maxl, maxr) - height[l])
        total_water += trap_water if trap_water > 0 else 0
        l += 1
        maxl = max(maxl, height[l])
    else:
        trap_water = min(maxl, maxr) - height[r]
        total_water += trap_water if trap_water > 0 else 0
        r -= 1
        maxr = max(maxr, height[r])
print(total_water)
