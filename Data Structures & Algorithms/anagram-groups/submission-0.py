from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list) # automatically creates an empty list if the key is not there

        for word in strs:
            count = [0] * 26 # Refers to the 26 letters

            for letter in word:
                count[ord(letter) - ord('a')] += 1 # 0 to a, 1 to b, 2 to c....
            key = tuple(count)
            
            result[key].append(word)
        
        return list(result.values())
