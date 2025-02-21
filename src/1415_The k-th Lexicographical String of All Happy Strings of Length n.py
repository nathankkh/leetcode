class Solution:
    # recursion optimisation: early termination
    # Since we start from 'a' and subsequent `next_chars` are in lexicographical order,
    # the generated lst is already sorted.
    # keep a count of generated strings, return once k is hit 

    # math optimisation:
    # sum of possible strings -> 3* (2^(n-1))
    # 
    def getHappyString(self, n: int, k: int) -> str:
        '''
        happy string -> no repeating chars in strings
        letters in the string ['a','b','c']

        Construct all possible happy strings of length n, sort lexicographically, return the kth element
        '''

        lst=[]

        def inner(curr_string, add, n):
            new_string = curr_string + add

            if len(new_string) == n:
                lst.append(new_string)
                return
            
            
            match add:
                case "a":
                    next_char = ['b','c']
                case "b":
                    next_char = ['a','c']
                case 'c':
                    next_char = ['a','b']
            
            for char in next_char:
                inner(new_string, char, n)
            
        for c in ['a','b','c']:
            inner('', c, n)
        

        if k > len(lst):
            return ''
        else:
            lst.sort()
            return lst[k-1]
        
    