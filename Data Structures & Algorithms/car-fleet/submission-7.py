class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        given pos & speed 
        length n
        dest target

        *** sort by position descending so closes tot finish first

        (target - position) / speed = time it takes to get there
        so if time <= stack.top() then skip item else add the item to teh stack

        also you always want the slowest in teh top (i beleive) we can chnage thsi is its wrong

        stack problem
        return num of fleets ( so in the end return the number of items still in teh fleet)

        """

        stack = []
        pairs = list(zip(position,speed))
        pairs.sort(reverse=True)
        for p,s in pairs:
            time = (target-p)/s
            if not stack:
                stack.append(time)
            elif time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)



        