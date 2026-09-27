class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque([("0000", 0)])
        visited = set(deadends)
        visited.add("0000")

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns

            for i in range(4):
                digit = int(lock[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    next_lock = lock[:i] + str(new_digit) + lock[i+1:]
                    if next_lock not in visited:
                        visited.add(next_lock)
                        q.append((next_lock, turns + 1))

        return -1
                
                
            
