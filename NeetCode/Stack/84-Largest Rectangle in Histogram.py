heights = [2,4]
max_area = 0
index_height = list()
for index, height in enumerate(heights):
    if index_height:
        pre_index, pre_height = index_height[-1]
        if height > pre_height:
            index_height.append((index, height))
        elif height == pre_height:
            pass
        else:
            while index_height and index_height[-1][1] > height:
                pre_index, pre_height = index_height.pop()
                area = (index - pre_index) * pre_height
                max_area = max(area, max_area)
            index = pre_index
            index_height.append((index, height))
    else:
        index_height.append((index, height))

while index_height:
    index, height = index_height.pop()
    max_area = max(max_area, (len(heights) - index) * height)

print(max_area)