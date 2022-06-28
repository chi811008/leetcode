image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1
heigh = len(image)
width = len(image[0])
color = image[sr][sc]

if color == newColor: return image
def adjacent(k, l):
    if image[k][l] == color:
        image[k][l] = newColor
        if k < (heigh - 1):
            adjacent(k + 1, l)
        if k >= 1:
            adjacent(k - 1, l)
        if l < (width - 1):
            adjacent(k, l + 1)
        if l >= 1:
            adjacent(k, l - 1)
adjacent(sr, sc)
print(image)


oldColor = image[sr, sc]
if oldColor == newColor: return image
m = len(image)
n = len(image[0])

def dfs(i, j):
    if image[i, j] == oldColor:
        image[i, j] = newColor
        if i + 1 < m: dfs(i + 1, j)
        if i - 1 >= 0: dfs(i - 1, j)
        if j + 1 < n: dfs(i, j + 1)
        if j - 1 >= 0: dfs(i, j - 1)
dfs(sr, sc)
return image

