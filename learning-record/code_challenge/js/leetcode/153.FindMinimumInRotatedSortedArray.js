// 153. Find Minimum in Rotated Sorted Array (Medium)
// Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

// [4,5,6,7,0,1,2] if it was rotated 4 times.
// [0,1,2,4,5,6,7] if it was rotated 7 times.
// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

// Given the sorted rotated array nums of unique elements, return the minimum element of this array.

// You must write an algorithm that runs in O(log n) time.

// Example 1:
// Input: nums = [3,4,5,1,2]
// Output: 1
// Explanation: The original array was [1,2,3,4,5] rotated 3 times.

// Example 2:
// Input: nums = [4,5,6,7,0,1,2]
// Output: 0
// Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

// Example 3:
// Input: nums = [11,13,15,17]
// Output: 11
// Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    if (nums.length === 1) return nums[0];
    
    let left = 0;
    let right = nums.length - 1;
    
    // If array is not rotated
    if (nums[right] > nums[left]) {
        return nums[0];
    }
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        // Check if mid element is the minimum
        if (nums[mid] > nums[mid + 1]) {
            return nums[mid + 1];
        }
        
        // Check if element before mid is greater than mid
        if (nums[mid - 1] > nums[mid]) {
            return nums[mid];
        }
        
        // If mid element is greater than first element,
        // minimum lies in right half
        if (nums[mid] > nums[0]) {
            left = mid + 1;
        } else {
            // Minimum lies in left half
            right = mid - 1;
        }
    }
    
    return nums[0];
};

// Test cases
console.log(findMin([3,4,5,1,2])); // 1
console.log(findMin([4,5,6,7,0,1,2])); // 0
console.log(findMin([11,13,15,17])); // 11
