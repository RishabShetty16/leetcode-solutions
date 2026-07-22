class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lastIndex = [-1] * 256

        left = 0
        maxLen = 0

        for right in range(len(s)):

            if lastIndex[ord(s[right])] != -1:
                left = max(left, lastIndex[ord(s[right])] + 1)

            maxLen = max(maxLen, right - left + 1)

            lastIndex[ord(s[right])] = right

        return maxLen