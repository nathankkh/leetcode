class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def get_nums():
            arr=[] # array to hold all powers of 2
            for i in range(31):
                arr.append(sorted(str(1<<i)))
            return arr
        s=sorted(str(n))
        return s in get_nums()            
        
