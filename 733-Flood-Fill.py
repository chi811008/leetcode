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