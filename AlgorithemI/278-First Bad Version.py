n = 5
bad = 4
ans = 2
def isBadVersion(num):
    pass
def firstBadVersion(self, n: int) -> int:
    head, tail = 1, n
    while head <= tail:
        if isBadVersion(head):
            return head
        elif isBadVersion(tail) and (not isBadVersion(tail - 1)):
            return tail

        mid = (head + tail) // 2
        if isBadVersion(mid):
            if not isBadVersion(mid - 1):
                return mid
            else:
                tail = mid - 1
        else:
            head = mid + 1
