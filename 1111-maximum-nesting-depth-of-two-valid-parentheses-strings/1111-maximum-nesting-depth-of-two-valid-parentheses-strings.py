class Solution(object):
    def maxDepthAfterSplit(self, seq):
        l=len(seq)
        res=[]
        count=0
        for i in range(l):
            if seq[i]=='(':
                count=count+1
                res.append(count%2)
            else:
                res.append(count%2)
                count=count-1
        return res
        # """
        # :type seq: str
        # :rtype: List[int]
        # """