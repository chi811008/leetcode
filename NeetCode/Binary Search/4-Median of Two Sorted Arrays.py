class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        merge_length = len(A) + len(B)
        median = merge_length // 2
        if len(A) > len(B):
            A, B = B, A
        # search smaller list A
        l, r = 0, len(A) - 1
        while True:
            ind_A = (l + r) // 2
            ind_B = median - (ind_A + 1) - 1
            Aleft = A[ind_A] if ind_A >= 0 else float("-infinity")
            Aright = A[ind_A + 1] if ind_A + 1 < len(A) else float("infinity")
            Bleft = B[ind_B] if ind_B >= 0 else float("-infinity")
            Bright = B[ind_B + 1] if ind_B + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if merge_length % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                r = ind_A - 1
            else:
                l = ind_A + 1
