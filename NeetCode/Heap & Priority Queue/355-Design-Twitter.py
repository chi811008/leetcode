from collections import defaultdict
from heapq import heapify, heappush, heappop
class Twitter:

    def __init__(self):
        self.postNum = -1
        self.userToPost = defaultdict(list) # userId -> list of (self.postNum, tweetId)
        self.followerToFollowees = defaultdict(set) # userId -> set of followeedId
        self.followeeToFollowers = defaultdict(set) # userId -> set of followerId
        # user's feed map: 10 most recent -> top 10 postNum 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToPost[userId].append((self.postNum, tweetId))
        self.postNum -= 1

        

    def getNewsFeed(self, userId: int) -> list[int]:
        res = [] # ordered: starting from recent
        minHeap = []
        
        # get followees
        postUsers = self.followerToFollowees[userId]
        postUsers.add(userId)
        for userId in postUsers:
            if userId in self.userToPost:
                posts = self.userToPost[userId]
                idx = len(posts) - 1
                postNum, tweetId = posts[idx]
                minHeap.append((postNum, tweetId, userId, idx - 1))
        heapify(minHeap)

        while minHeap and len(res) < 10:
            postNum, tweetId, userId, idx = heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                postNum, tweetId = self.userToPost[userId][idx]
                heappush(minHeap, (postNum, tweetId, userId, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerToFollowees[followerId].add(followeeId)
        self.followeeToFollowers[followeeId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerToFollowees[followerId]:
            self.followerToFollowees[followerId].remove(followeeId)
        if followerId in self.followeeToFollowers[followeeId]:
            self.followeeToFollowers[followeeId].remove(followerId)
        
def runTest():
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]

if __name__ == "__main__":
    runTest()