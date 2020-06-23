"""
判断是否为字符重排
"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)


print(Solution().CheckPermutation(s1='abc', s2='bca'))


class Solution2:
    def checkpermutation2(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        s2 = list(s2)
        for i in s1:
            if i not in s2:
                return False
            else:
                s2.remove(i)  # remove 避免重复
        # s1 = list(s1)
        # print(set(s1))
        # s2 = list(s2)
        # print(set(s2))
        # 这里不能用集合

        # return set(s1) == set(s2)
        return True


print(Solution2().checkpermutation2("abacdaa", "baacdad"))