/**
 *
 * move all the 0 to the end of the given arry
 */
function moveZerosToEnd(arr) {
    // Filter out non-zero elements
    const nonZeroElements = arr.filter(element => element !== 0);

    // Count the number of zeros
    const zeroCount = arr.length - nonZeroElements.length;

    // Create a new array with non-zero elements followed by zeros
    const resultArray = [...nonZeroElements, ...Array(zeroCount).fill(0)];

    return resultArray;
}

// Example usage:
const inputArray = [0, 2, 0, 3, 4, 0, 1];
console.log("Original Array:", inputArray);
const result = moveZerosToEnd(inputArray);
console.log("Array with Zeros Moved to the End:", result);
