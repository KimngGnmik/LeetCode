class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tempArray = [] # Create an empty array called tempArray
        sum = 0 # Create an int variable that has the value of 0
        
        for i in range (len(nums)): # Iterate through the array from 0 to end of original array (nums)
            
            sum = sum + nums[i] # Add the current value of sum with the value of array at current index
            tempArray.append(sum) # Append the sum to the array (tempArray)
        
        return tempArray # Return the array (tempArray)
            
        
        