import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.user_posts = defaultdict(list) # userId -> posts: list() [time, tweetId]
        self.user_followee = defaultdict(set) # userId -> followees: set() {userId}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append([self.time, tweetId])
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> list[int]:
        res = list()
        posts = list()
        self.user_followee[userId].add(userId)
        followees = self.user_followee[userId]
        for followee_id in followees:
            if followee_id in self.user_posts:
                latest_post_index = len(self.user_posts[followee_id]) - 1
                time, tweet_id = self.user_posts[followee_id][latest_post_index]
                posts.append([time, tweet_id, followee_id, latest_post_index - 1])
        heapq.heapify(posts)
        while posts and len(res) < 10:
            time, tweet_id, followee_id, latest_post_index = heapq.heappop(posts)
            res.append(tweet_id)
            time, tweet_id = self.user_posts[followee_id][latest_post_index]
            if latest_post_index >= 0:
                heapq.heappush(posts, [time, tweet_id, followee_id, latest_post_index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_followee[followerId]:
            self.user_followee[followerId].remove(followeeId)