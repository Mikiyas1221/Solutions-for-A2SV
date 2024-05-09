class Solution:
    def similarPairs(self, words: List[str]) -> int:
        mylist = []
        for i in range(len(words)):
            tolist = []
            for j in range(len(words[i])):
                if words[i][j] not in tolist:
                    tolist.append(words[i][j])
            mylist.append(tolist)
        for i in range(len(mylist)):
            mylist[i].sort()
        k = 0
        l = 0
        while l < len(mylist) - 1:
            r = l + 1
            while r < len(mylist):
                if mylist[l] == mylist[r]:
                    k += 1
                r += 1
            l += 1
        return k
        
