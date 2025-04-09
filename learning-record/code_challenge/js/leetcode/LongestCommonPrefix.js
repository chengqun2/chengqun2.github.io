/**
 * Write a function to find the longest common prefix string amongst an array of strings.

 If there is no common prefix, return an empty string "".



 Example 1:

 Input: strs = ["flower","flow","flight"]
 Output: "fl"
 Example 2:

 Input: strs = ["dog","racecar","car"]
 Output: ""
 Explanation: There is no common prefix among the input strings.


 Constraints:

 1 <= strs.length <= 200
 0 <= strs[i].length <= 200
 strs[i] consists of only lowercase English letters.

 */
/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = function (strings) {
    if (strings.length === 0) {
        return "";
    }
    console.log(strings)
    // Sort the array to easily find the common prefix
    strings.sort();
    console.log(strings)
    // Take the first and last strings in the sorted array
    const firstStr = strings[0];
    const lastStr = strings[strings.length - 1];

    // Find the common prefix between the first and last strings
    let commonPrefix = "";
    for (let i = 0; i < firstStr.length; i++) {
        if (firstStr[i] === lastStr[i]) {
            commonPrefix += firstStr[i];
        } else {
            break;
        }
    }

    return commonPrefix;
};

// Example usage:
const stringsArray = ["cafdd", "ccaadfee", "cbafeee"];
const result = longestCommonPrefix(stringsArray);
console.log("Longest Common Prefix:", result);
