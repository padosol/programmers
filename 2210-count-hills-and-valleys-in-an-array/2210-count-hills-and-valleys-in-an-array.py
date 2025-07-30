class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        size = len(nums)

        left = nums[0]
        right = nums[2]
        hill = 0
        valleys = 0
        for i in range(1, size - 1):
            num = nums[i]
            num_left = nums[i-1]
            num_right = nums[i+1]

            if num_left != num:
                left = num_left
            if num_right != num:
                right = num_right

            if left < num and right < num:
                hill += 1
            if right > num and left > num:
                valleys += 1


        return hill + valleys