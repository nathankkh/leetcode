class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefixProduct=[1]
        self.lastZero = -1
        self.size = 0


    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.lastZero = len(self.nums) 
            self.prefixProduct.append(1)
        else:
            self.prefixProduct.append(self.prefixProduct[-1] * num)
        self.size += 1

    def getProduct(self, k: int) -> int:
        if self.size - k < self.lastZero:
            return 0

        if k == 1:
            return self.nums[-1]

        return self.prefixProduct[-1] // self.prefixProduct[-(k+1)]
    
    def __str__(self):
        return f"nums: {self.nums}\nprefix: {self.prefixProduct}\nlastZero: {self.lastZero}\nsize: {self.size}"

    def __repr__(self):
        return f"nums: {self.nums}\nprefix: {self.prefixProduct}\nlastZero: {self.lastZero}\nsize: {self.size}"

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


def driver(instructionArray, numArray, output):
    obj = ProductOfNumbers()
    res = [None]
    for i in range(len(instructionArray)):
        match instructionArray[i]:
            case "add":
                obj.add(numArray[i][0])
                res.append(None)
            case "getProduct": 
                res.append(obj.getProduct(numArray[i][0]))
    print(res)
    return res == output

print('tc1')
instruction1 = ["add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
num1 = [[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
out1 = [None,None,None,None,None,None,20,40,0,None,32]
driver(instruction1, num1, out1 )