"""Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0

        # Iterate over each element as the first element of the triplet
        for i in range(len(arr)):
            # XOR of elements from index i to j
            xor = 0
            # Iterate over remaining elements as the second element of the triplet
            for j in range(i, len(arr)):
                # Update the XOR by XORing the current element with the current XOR
                # If the XOR becomes 0, it means the XOR of elements between i and j
                # is 0. So, increment the count by the number of elements between i
                # and j.
                xor ^= arr[j]
                if xor == 0:
                    count += j - i

        return count