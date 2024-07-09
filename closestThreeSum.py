"""Given an array, arr of integers, and another number target, find three integers in the array such that their sum is closest to the target. Return the sum of the three integers.

Note: If there are multiple solutions, return the maximum one.

Examples :

Input: arr[] = [-7, 9, 8, 3, 1, 1], target = 2
Output: 2
Explanation: There is only one triplet present in the array where elements are -7,8,1 whose sum is 2.
Input: arr[] = [5, 2, 7, 5], target = 13
Output: 14
Explanation: There is one triplet with sum 12 and other with sum 14 in the array. Triplet elements are 5, 2, 5 and 2, 7, 5 respectively. Since abs(13-12) ==abs(13-14) maximum triplet sum will be preferred i.e 14.
Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)

Constraints:
3 ≤ arr.size() ≤ 103
-105 ≤ arr[i] ≤ 105
1 ≤ target ≤ 105

"""
class Solution:
    def threeSumClosest(self, arr, target):
        n = len(arr)
        arr.sort()
        diff = float('inf')
        ans = None
        
        for i in range(n):
            first = arr[i]
            start = i + 1
            end = n - 1

            while start < end:
                current_sum = first + arr[start] + arr[end]
                if current_sum == target:
                    return target

                current_diff = abs(current_sum - target)

                if current_diff < diff or (current_diff == diff and current_sum > ans):
                    diff = current_diff
                    ans = current_sum

                if current_sum > target:
                    end -= 1
                else:
                    start += 1

        return ans
