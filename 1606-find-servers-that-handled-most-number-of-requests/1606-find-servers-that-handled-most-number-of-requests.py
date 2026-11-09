
import heapq
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Make completed servers available again
            while busy and busy[0][0] <= arrival[i]:
                end_time, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            target = i % k

            # Find the next available server
            idx = available.bisect_left(target)

            # Wrap around if necessary
            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            # Count the handled request
            count[server] += 1

            # Add server to busy heap
            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]

