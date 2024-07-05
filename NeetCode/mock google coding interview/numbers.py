from random import choice
class OperaterWithoutDuplicateNumber:
    def __init__(self):
        self.numHashMap = {}
        self.numList = []
        self.lastIndex = 0

    def insertNumber(self, n: int) -> None:
        if n in self.numHashMap:
            return

        self.numHashMap[n] = self.lastIndex
        self.numList.append(n)
        self.lastIndex += 1
        return

    def removeNumber(self, n: int) -> None:
        if n not in self.numHashMap:
            return

        index = self.numHashMap.pop(n)
        lastNum = self.numList.pop()
        if n != lastNum:
            self.numList[index]=lastNum
            self.numHashMap[lastNum] = index
        self.lastIndex -= 1
        return

    def getRandomNumber(self) -> int:
        return choice(self.numList)


# [insert 3, insert 4, inset4 , insert 5 , remove 4, getRandom]
# self.numHashMap ={3: 0, 5:1}
# self.numList = [3, 5]
# self.lastIndex = 2

# n = 4
# index = 1
# latNum = 5


from collections import defaultdict
class OperatorWithDuplicate:
    def __init__(self):
        self.numHashMap = defaultdict(list) #{4: [0, 2], 3:[1]}
        self.numList = []
        self.lastIndex = 0

    def insertNumber(self, n: int) -> None:
        self.numHashMap[n].append(self.lastIndex)
        self.numList.append(n)
        self.lastIndex += 1
        return

    def removeNumber(self, n: int) -> None:
        if (n not in self.numHashMap) or (not self.numHashMap[n]):
            return

        index = self.numHashMap[n].pop()
        lastNum = self.numList.pop()
        if n != lastNum:
            self.numList[index]=lastNum
            self.numHashMap[lastNum] = index
        self.lastIndex -= 1
        return

    def getRandomNumber(self) -> int:
        return choice(self.numList)


# self.numHashMap = {4: [], 3:[0]}
# self.numList = [3]
# self.lastIndex = 1


# remove 4
# n = 4
# index = 0
# lastNum = 3
