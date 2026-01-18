"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        is_common_prefix = True
        char_index = 0
        common_prefix = ""
        common_char = ""

        for i, word in enumerate(strs):
            print(i, word)
            if char_index == len(word) - 1 or i == len(strs) - 1:
                break
            next_word = strs[i + 1]
            next_word_char = next_word[char_index]

            char = word[char_index]
            print(word, next_word, char, next_word_char)
            if char == next_word_char:
                common_char = char
            else:
                is_common_prefix = False
                break

        if is_common_prefix:
            common_prefix += common_char

        return common_prefix


s = Solution()
strs = ["flower", "flow", "flight"]
print(f"The common prefix is {s.longestCommonPrefix(strs)}")
