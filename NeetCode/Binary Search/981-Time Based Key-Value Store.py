class TimeMap:

    def __init__(self):
        self.data = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = self.data.get(key, list())
        val.append([timestamp, value])
        self.data[key] = val

    def get(self, key: str, timestamp: int) -> str:
        val = self.data.get(key, "")
        if val == "":
            return ""
        def bs(head, tail):
            while head <= tail:
                mid = (head + tail) // 2
                if val[mid][0] == timestamp:
                    return mid
                elif val[mid][0] > timestamp:
                    tail = mid - 1
                else:
                    head = mid + 1
            return tail
        ind = bs(0, len(val) - 1)
        if ind == -1:
            return ""
        return val[ind][1]