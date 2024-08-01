class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        old = [char for char in words[0]]
        for word in words:
            temp = []
            for char in word:
                if char in old:
                    temp.append(char)
                    old.remove(char)
            old = temp
        return old        
