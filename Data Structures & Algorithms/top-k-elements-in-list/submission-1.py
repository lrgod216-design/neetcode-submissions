class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else: 
                seen[num] += 1
            
        
        seen_sorted = dict(sorted(seen.items(), key = lambda x:x[1], reverse = True))

        # print(seen_sorted)
        result = list(seen_sorted.keys())
        return result[0:k]










        