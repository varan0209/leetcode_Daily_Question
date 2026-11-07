import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        free = [(w, i) for i, w in enumerate(servers)]   # (weight, index)
        heapq.heapify(free)
        busy = []                                        # (free_time, weight, index)
        ans = [0] * len(tasks)
        t = 0
        for j, dur in enumerate(tasks):
            t = max(t, j)                                # task j can't start before second j
            while busy and busy[0][0] <= t:              # release servers that are done
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            if not free:                                 # wait for the earliest server to finish
                t = busy[0][0]
                while busy and busy[0][0] <= t:
                    _, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            ans[j] = i
            heapq.heappush(busy, (t + dur, w, i))
        return ans