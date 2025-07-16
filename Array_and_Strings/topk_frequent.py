def topKFrequent(nums, k):
        count = {}
        for num in nums:
            count[num] = 0
        count[num] += 1
        print("line6",count)
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        print("line12 arr",arr)
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        print(res)
        return res

topKFrequent([1,1,1,2,2,3], 2) # -> [1, 2]
topKFrequent([1], 1) # -> [1]
