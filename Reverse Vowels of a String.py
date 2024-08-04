class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        str_list = [chr for chr in s]
        l = 0
        r = len(s) - 1
        while l < r:
            while str_list[l].lower() not in vowels and l < r:
                l += 1
            current_left_vowel = str_list[l]
            while str_list[r].lower() not in vowels and l < r:
                r -= 1
            current_right_vowel = str_list[r]
            if l <= r:
                str_list[r], str_list[l] = str_list[l], str_list[r]
                l += 1
                r -= 1
        return "".join(str_list)
