class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            # for each word, store in format "length#(delimiter)word"
            # e.g. ["Hello","World"] --> 5#Hello5#World
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result,i = [],0 # create result array and a pointer
        while i < len(s): # go over every letter in the string and separate each word
            j = i # second pointer to find out the length
            while s[j] != "#":
                j += 1 # while not reach delimiter, it's the integer -> length of the word
            length = int(s[i:j]) # e.g. 5#Hello, j = 1, length = s[0:1] = 5
            result.append(s[j + 1:j + length + 1]) # append the word, s[3:7] = Hello
            i = j + length + 1 # Start from the next index, which is the integer
        return result