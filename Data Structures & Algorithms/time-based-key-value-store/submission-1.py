class TimeMap:

    def __init__(self):
        self.timeMap = {} # alice: [happy, 1], [sad, 3]

    # All the timestamps of set are strictly increasing.
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []

        self.timeMap[key].append([timestamp, value])
        
    # Return the latest value for key, not exceeding the timestamp
    def get(self, key: str, timestamp: int) -> str:

        arr = self.timeMap.get(key, [])

        # 1 3 4 5 6 8 .... given: 7

        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:

            m = (l + r) // 2

            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1

            else:
                r = m - 1

        return res