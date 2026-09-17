class TimeMap:

    def __init__(self):
        self.stamps = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.stamps:
            self.stamps[key].append((timestamp, value))
        else:
            self.stamps[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stamps:
            return ""

        keyList = self.stamps[key]
        l,r = 0, len(keyList) - 1

        while l<=r:
            m = (l + r)//2
            if keyList[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
            
        if r >= 0:
            return keyList[r][1]
        return ""


        
        
