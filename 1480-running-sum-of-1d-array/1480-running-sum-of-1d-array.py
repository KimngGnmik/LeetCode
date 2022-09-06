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
            
        

# My approach to this problem:

    # I initially wanted to create a temp array where I stored the first value of >nums< to the first index (index       0). Then I wanted to iterate through the entirity of >nums< starting from 1 to the len of nums. But it             then I realized that this current solution was simpiler because I could do everything in the for loop rather       than hard assigning a value