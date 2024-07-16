class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        solutions = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            
            end = nums[i]
            
            if start == end:
                solutions.append(f"{start}")
            else:
                solutions.append(f"{start}->{end}")
            
            i += 1

        return solutions
#end
