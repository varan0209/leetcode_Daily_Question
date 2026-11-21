
class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # New parent array
        new_parent = parent[:]

        # Latest ancestor for each character
        last = [-1] * 26

        # Store previous last value for backtracking
        prev_last = [-1] * n

        # First DFS: determine new parents using original tree
        stack = [(0, False)]

        while stack:
            node, exiting = stack.pop()
            c = ord(s[node]) - ord('a')

            if exiting:
                # Restore ancestor information
                last[c] = prev_last[node]
                continue

            # Save the previous ancestor with the same character
            prev_last[node] = last[c]

            # Find closest matching ancestor
            if last[c] != -1:
                new_parent[node] = last[c]

            # Current node becomes latest ancestor of its character
            last[c] = node

            # Exit event for backtracking
            stack.append((node, True))

            # Visit original children
            for child in children[node]:
                stack.append((child, False))

        # Build the modified tree
        new_children = [[] for _ in range(n)]

        for node in range(1, n):
            new_children[new_parent[node]].append(node)

        # Second DFS: calculate subtree sizes
        answer = [1] * n

        stack = [(0, False)]

        while stack:
            node, exiting = stack.pop()

            if not exiting:
                stack.append((node, True))

                for child in new_children[node]:
                    stack.append((child, False))

            else:
                for child in new_children[node]:
                    answer[node] += answer[child]

        return answer
