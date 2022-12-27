class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {} #Creating an empty dictionary called seen

        for i, num in enumerate(nums): #loop through it while enumerating nums
            if (target - num) in seen: #Check to see if the target value - current num is stored in seen
                return [seen[target - num], i] #If so then return that num and its index

            seen[num] = i #If not then add that num to the seen dictionary with num key and i value

        return[] #if the array of integers is empty then just return nothing





#Things to learn: 

    #---------------Dictionaries:---------------
        # Dictionaries are unordered collections of key-value pairs. 
            # While the items in a list/array have a specific order which is maintained whenever it is modified. 
            # Key-value pairs in dictionaries are not orderd, which means the order of the pairs can change whenever the dictionary is modified.

        # ----------To create a dictionary,----------
            # You can either create the dictionary using
                # | dictionary_name = {} | and add to the dictionary later using
                # | dictionary_name[key] = value |
            # Or populate it when initializing the dictionary
                # | dictionary_name = {'key': value, 'key': value, 'key': value} |

        # ----------To delete a key-value pair,----------
            # You can do | del dictionary_name['key'] |

        # ----------To check if key is in dictionary,----------
            # | 'key' in dictionary_name |

        # ----------To iterate through a dictionary,----------
            # | for key_iterator, value_iterator in dictionary_name.items():
            #       print(key_iterator, value_iterator) |
        # ----------you could also try,----------
            # | for key_iterator, in dictionary_name:
            #       print(key_iterator, dictionary_name(key_iterator)) |

        # ----------To iterate through keyes,----------
            # | for key_iterator, in dictionary_name.keys():
            #       print(key_iterator, dictionary_name[key_iterator]) |
        # ----------To iterate through values,----------
            # | for key_iterator, in dictionary_name.values():
            #       print(key_iterator) |


    #---------------Enumerate:---------------
        # Enumerate is a built-in function in Python that takes an iterable object, such as a list, and returns an iterator that produces tuples containing the index and the element of the object.
            # EXAMPLE:
                # | for index, key in enumerate(iterable_object):
                #       print(index, iterable_object) |
        # This can be useful when you need to keep track of the index of an element while iterating through a list.


    #---------------Mutable vs Immutable:---------------

        # An object is mutable if it can be modified after it is created, and it is immutable if it cannot be modified.
        
        # Mutable : Lists, Dictionaries
        # Imutable: Numbers, Strings, Tuples (basically a list but cannot be edited because it uses fixed sizes) representation in memory)

