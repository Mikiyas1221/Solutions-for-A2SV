class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        new_team = []
        skill.sort()
        l = 0
        r = len(skill)-1
        the_sum = 0
        ans = -1
        while l < r:
            new_team.append([skill[l], skill[r]])
            the_sum = skill[l] + skill[r]
            l += 1
            r -= 1
        chemistry = 0
        for i in range(len(new_team)):
            chemistry += new_team[i][0] * new_team[i][1]
        for i in range(len(new_team)):
            if new_team[i][0] + new_team[i][1] != the_sum:
                ans = -1
                break
            else:
                ans = chemistry
        return ans
                
