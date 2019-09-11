from collections import defaultdict


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_table = defaultdict(lambda: defaultdict(bool))
        self.time_line = {}
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.time_line[self.t] = (userId, tweetId)
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        cnt = 0
        feed = []
        for t in range(self.t - 1, -1, -1):
            if userId == self.time_line[t][0] or self.follow_table[userId][
                    self.time_line[t][0]]:
                feed.append(self.time_line[t][1])
                cnt += 1
                if cnt == 10:
                    break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follow_table[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follow_table[followerId][followeeId] = False


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)