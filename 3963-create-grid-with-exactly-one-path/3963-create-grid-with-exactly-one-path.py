class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        # free cells: the whole top row and the whole right column
        return ["." * n if i == 0 else "#" * (n - 1) + "." for i in range(m)]