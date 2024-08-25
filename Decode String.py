class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            num = 0
            decoded_str = ""

            while index < len(s):
                char = s[index]
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == "[":
                    index, decoded_part = helper(index + 1)
                    decoded_str += num * decoded_part
                    num = 0
                elif char == "]":
                    return index, decoded_str
                else:
                    decoded_str += char
                
                index += 1
            return index, decoded_str
        return helper(0)[1]
