class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        # Step 1: count frequency
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        

        freq = {}
        for i in range(len(nums)+1):
            freq[i] = []
        

        for num in count:
            freq[count[num]].append(num)
        
        print(freq)
        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res







        


# {1:[1,2,3],
# 2:[2,3],
# 3:[] }
        # hm = {}
        # for num in nums:
        #     if num in hm:
        #         hm[num]+=1
        #     else:
        #         hm[num] =1
        

        # res = sorted(hm, key=hm.get, reverse = True)
        
        
        # return res[:k]