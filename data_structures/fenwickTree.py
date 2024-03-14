

class FenwickTree:
    # def __init__(self, nums: list):
    #     """
    #     O(NLogN)
    #     """
    #     self.nums = [0] * len(nums)
    #     self.bit = [0] * len(nums)
    #     for i, num in enumerate(nums):
    #         self.update(i, num)
    #     print(self.bit)

    def __init__(self, nums: list):
        """
        O(N)
        """
        self.nums = nums.copy()
        self.bit = [0] * len(nums)
        for i, num in enumerate(nums):
            self.bit[i] += num
            r = i | (i + 1)
            if r < len(nums):
                self.bit[r] += self.bit[i]

    def update(self, idx: int, val: int) -> None:
        if idx >= len(self.nums):
            return
        diff = val - self.nums[idx]
        self.nums[idx] = val
        while idx < len(self.nums):
            self.bit[idx] += diff
            idx = idx | (idx + 1)

    def updateRange(self, left: int, right: int, val: int) -> None:
        self.update(left, val)
        self.update(right + 1, -val)

    def add(self, idx: int, val: int) -> None:
        if idx >= len(self.nums):
            return
        self.nums[idx] += val
        while idx < len(self.nums):
            self.bit[idx] += val
            idx = idx | (idx + 1)

    def query(self, idx: int) -> int:
        """
        returns sum(nums[:idx])
        """
        res = 0
        while idx > 0:
            res += self.bit[idx - 1]
            idx = idx & (idx - 1)
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left)