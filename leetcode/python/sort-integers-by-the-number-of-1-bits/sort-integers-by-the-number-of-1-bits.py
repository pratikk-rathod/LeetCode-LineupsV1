class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        dictr={}

        for i in arr:
            binn = bin(i)[2:]
            c = binn.count("1")
            print(binn)
            if c in dictr:
                dictr[c].append(i)
            else:
                dictr[c] = [i]
        sorted_dict = dict(sorted(dictr.items()))
        print(sorted_dict)
        arr=[]

        for key,value in sorted_dict.items():
            
            arr.extend(value)
        return arr