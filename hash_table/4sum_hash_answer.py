"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 4:
            return None
        return self.four_sum(nums, target)

    def four_sum(self, nums, target):
        n = len(nums)  # size of the array
        ans = []

        # sort the given array:
        nums.sort()

        # calculating the quadruplets:
        for i in range(n):
            # avoid the duplicates while moving i:
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # avoid the duplicates while moving j:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # 2 pointers:
                k = j + 1
                l = n - 1
                while k < l:
                    _sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if _sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        k += 1
                        l -= 1

                        # skip the duplicates:
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif _sum < target:
                        k += 1
                    else:
                        l -= 1
        return ans


if __name__ == '__main__':

    s= Solution()

    nums = [2,2,2,2,2]
    target = 8

    print(s.four_sum(nums, target))

