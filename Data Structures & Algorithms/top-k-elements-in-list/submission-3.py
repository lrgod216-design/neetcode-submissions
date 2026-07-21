class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # count frequency of each number
        
        # bucket_sort list, where index is frequency and list holds 
        # number that appear i times
        freq = [[] for i in range(len(nums)+ 1)]

        # mapping numbers with their counts
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # fill the bucket array by frequency
        for n,c in count.items():
            freq[c].append(n)
        
        # creating result array for the top k number
        result = []
        for i in range(len(freq) - 1, 0, -1): #starting from the most frequent num
            for n in freq[i]:
                result.append(n) # append each item in the list
                if len(result) == k:
                    return result

        