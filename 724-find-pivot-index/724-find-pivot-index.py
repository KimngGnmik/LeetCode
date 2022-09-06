class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = sum(nums) # Creating an int veriable that equals the sum of the array (nums)
        
        leftsum = 0 # Leftsum = 0
        
        for i, x in enumerate(nums): # Iterating through the array (nums) 
            if leftsum == (s - leftsum - x): # If the leftsum is the same as sum of the array - leftsum - value at current index, then return the index 
                return i
            leftsum += x # Else add the value of the array at current index with current value of leftsum, then save the value to left sum; variable += variable(or int) is the same as variable = variable + variable(or int)
        return -1
    
    

# This was a bit trickey because my original thought process was to create two variables (leftsum and right sum)
# got to the middle of the array (len(array)/2) and then sum left and right of that point. If the value of oneside
# is greater than the other then shift towards that side. Repeat this until the first or last index is reached.

# the problem with this approach was that it caused an infinite loop where shifting caused the pointer to go back an forth between two index.
# I was able to temp fix this where it kept track of the number of lefts and rights made.

# This revealed another problem where there were repeating values in two consecutive indexes then my code picked 
# the later index rather than the former. 


# There were alot of edge cases with my solution and I found myself continually adding to my code thus making it longer and less efficient. 


# I then learned about enumerate() which acts like a double forloop where it gets the index and value for each array value.
# Additionally, it made more sense to first take the sum of the whole array and subtract the current index value. 
# That eliminates the need to keep track of if the pointer reaches first or last index.


# My unoptimized code that still fails some tests:

"""
leftsum = 0
rightsum = 0
i = int(len(nums)/2)
prevmove = "none"
currentmove = "none"
while True:
    for x in range (0, i , 1):
        leftsum = leftsum + nums[x]
    for x in range (i + 1, len(nums), 1):
        rightsum = rightsum + nums[x]
    
    if ((leftsum == rightsum)):
        return i
    if ((i == 0) or (i == len(nums) -1)):
        return -1
    if (abs(leftsum) >= abs(rightsum)):
               i -= 1
               prevmove = currentmove
               currentmove = "left"
    else:
        i += 1
        prevmove = currentmove
        currentmove = "right"
        leftsum = 0
        rightsum = 0
            
    if((prevmove == "left" and currentmove == "right") or (prevmove == "right" and currentmove == "left")):
        return -1

"""