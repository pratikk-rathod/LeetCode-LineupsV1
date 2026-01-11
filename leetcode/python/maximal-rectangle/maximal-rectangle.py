class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def NSL(arr):
            s = []
            res = []
            for i in range(len(arr)):
                if len(s) == 0:
                    res.append(-1)
                if len(s) > 0 and arr[i] > s[-1][0]:
                    res.append(s[-1][1])
                if len(s) > 0 and arr[i] <= s[-1][0]:
                    while len(s) > 0 and arr[i] <= s[-1][0]:
                        s.pop()
                    if len(s) == 0:
                        res.append(-1)
                    else:
                        res.append(s[-1][1])
                s.append([arr[i], i])
            return res


        def NSR(arr):
            s = []
            res = []
            j = len(arr) - 1
            while j >= 0:
                if len(s) == 0:
                    res.append(len(arr))
                if len(s) > 0 and arr[j] > s[-1][0]:
                    res.append(s[-1][1])
                if len(s) > 0 and arr[j] <= s[-1][0]:
                    while len(s) > 0 and arr[j] <= s[-1][0]:
                        s.pop()
                    if len(s) == 0:
                        res.append(len(arr))
                    else:
                        res.append(s[-1][1])
                s.append([arr[j], j])
                j -= 1
            res.reverse()
            return res


        def width(l, r):
            w = []
            for i in range(len(l)):
                Width = r[i] - l[i] - 1
                w.append(Width)
            return w


        def Area(arr,w):
            maxArea = 0
            for i in range(len(arr)):
                a = arr[i] * w[i]
                maxArea = max(maxArea,a)
            return maxArea


        def MAH(arr):
            left = NSL(arr)
            right = NSR(arr)
            Width = width(left,right)
            mxArea = Area(arr,Width)
            return mxArea


        def main(arr):
            row = [0] * len(arr[0])
            areaMax = 0
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if int(arr[i][j]) == 0:
                        row[j] = 0
                    row[j] = row[j] + int(arr[i][j])
                areaMax = max(areaMax,MAH(row))
            return areaMax

        return main(matrix)