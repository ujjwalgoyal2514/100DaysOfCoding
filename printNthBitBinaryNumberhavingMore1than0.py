"""Given a positive integer n. Your task is to generate a string list of all n-bit binary numbers where, for any prefix of the number, there are more or an equal number of 1's than 0's. The numbers should be sorted in decreasing order of magnitude.

Example 1:

Input:  
n = 2
Output: 
"11, 10"
Explanation: Valid numbers are those where each prefix has more 1s than 0s:
11: all its prefixes (1 and 11) have more 1s than 0s.
10: all its prefixes (1 and 10) have more 1s than 0s.
So, the output is "11, 10".
Example 2:

Input:  
n = 3
Output: 
"111, 110, 101"
Explanation: Valid numbers are those where each prefix has more 1s than 0s.
111: all its prefixes (1, 11, and 111) have more 1s than 0s.
110: all its prefixes (1, 11, and 110) have more 1s than 0s.
101: all its prefixes (1, 10, and 101) have more 1s than 0s.
So, the output is "111, 110, 101".
User Task:
Your task is to complete the function NBitBinary() which takes a single number as input n and returns the list of strings in decreasing order. You need not take any input or print anything.

Expected Time Complexity: O(|2n|)
Expected Auxiliary Space: O(2n)

"""
class Solution:
    
    def NBitBinary(self, n):
        position = 0
        # Initialize the list with an empty string and counts of 0s and 1s
        binary_numbers = [["", 0, 0]]
        
        while position < n:
            new_binary_numbers = []
            # Iterate over each binary number in the list
            for binary, count_0, len_of_binary in binary_numbers:
                # Append '1' to the binary number and increment the count of 1s
                new_binary_numbers.append([binary + "1", count_0, len_of_binary + 1])
                # If the count of 0s is less than half the total length, append '0' and increment the count of 0s
                if count_0 * 2 < len_of_binary:
                    new_binary_numbers.append([binary + "0", count_0 + 1, len_of_binary + 1])
            position += 1
            binary_numbers = new_binary_numbers[:]
        
        # Return only the binary numbers without counts
        return [binary for binary, _, _ in binary_numbers]
