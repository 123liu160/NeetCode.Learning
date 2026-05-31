# 发推文：记录谁发了什么，按时间排序
# 关注 / 取关：用字典 + 集合存关系
# 获取首页10条最新：把关注的人的推文全部拿出来，用最大堆取最新10条
import heapq
from collections import defaultdict
from typing import List
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
         # 发推时自动关注自己（永远不会丢自己的推文）
        self.following[userId].add(userId)
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        #只遍历关注的人（里面已经包含自己）
        for user in self.following[userId]:
            for t in self.tweets[user]:
                heapq.heappush(heap, (-t[0], t[1]))

        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 不能取关自己
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)