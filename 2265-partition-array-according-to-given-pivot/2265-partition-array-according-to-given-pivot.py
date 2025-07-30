class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        pivot_list = []
        more_than = []
        for num in nums:
            if pivot == num:
                pivot_list.append(num)
            elif pivot < num:
                more_than.append(num)
            else:
                less_than.append(num)

        return less_than + pivot_list + more_than