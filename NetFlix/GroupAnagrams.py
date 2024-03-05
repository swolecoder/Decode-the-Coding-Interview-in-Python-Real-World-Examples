from collections import defaultdict

class Solution:
    def group_anagrams(self, strs):
        """
        Group anagrams from the input list of strings.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            List[List[str]]: A list of lists of strings, where each sublist contains anagrams.
        """
        hashMap = defaultdict(list)

        # Iterate through each string in the input list
        for s in strs:
            # Initialize a count array for each character in the alphabet
            count = [0] * 26  # For each letter in the alphabet

            # Increment the count for each character in the string
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            
            # The count array serves as a key to group anagrams
            hashMap[tuple(count)].append(s)

        # Convert the hash map values to a list
        return list(hashMap.values())

# Test the function
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
test1 = Solution()
print(test1.group_anagrams(strs))
