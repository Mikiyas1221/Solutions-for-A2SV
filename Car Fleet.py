class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p) / s for p, s in zip(position, speed)]
        cars = [[p, t] for p, t in zip(position, time)]
        cars.sort(reverse = True)
        stack = []
        for car in cars:
            stack.append(car)
            if len(stack) >= 2 and stack[-1][1] <= stack[-2][1]:
                stack.pop()
        return len(stack)
