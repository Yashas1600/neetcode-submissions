class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        for p,s in pairs:
            time = (target - p)/s
            if not stack:
                stack.append(time)
            elif time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)

        