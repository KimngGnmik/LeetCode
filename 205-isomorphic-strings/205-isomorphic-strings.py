class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)): #Check to see if the two lengths are the same. If not then cant be Isomorphic by definition
            return False
        
        hashtable = {} # Creating an empty dictionary 

        for i in range(len(s)):
    
            if(s[i] not in hashtable.keys()):
            
                if (t[i] in hashtable.values()):
                    keys = [k for k, v in hashtable.items() if v == t[i]]
                    if(keys != t[i]):
                        return False
                    
                hashtable[s[i]] = t[i]
            else:
                
                keyvalue = hashtable[s[i]]
                if (keyvalue != t[i]):
                    return False
                    
            print(hashtable)
            
        return True






# Here I learned about key value pairs that can be used to match up values at certain indexes of two different variables.For Future Refrences: https://www.pythontutorial.net/python-basics/python-dictionary/ 
        
        # Here I learned about key value pairs that can be used to match up values at certain indexes of two different variables.For Future Refrences: https://www.pythontutorial.net/python-basics/python-dictionary/ 
