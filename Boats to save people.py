class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        bound_index = -1
        boats = 0
        people.sort()
        for i in range(n):
            if people[i] >= limit:
                bound_index = i
                break
        l = 0
        r = n - 1
        if bound_index != -1:
            boats = n - bound_index
            r = bound_index - 1
        while l <= r:
            if people[r] + people[l] <= limit:
                boats = boats + 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1
        return boats
