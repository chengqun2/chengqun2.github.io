/**
 * Matching parenthesis. please write a function to check if the input string which may contain parenthesis is regular. return true if it is, otherwise false.
 * @param input
 * @returns {boolean}
 */
function isRegular(input) {
    console.log(input)
    const stack = [];

    for (let i = 0; i < input.length; i++) {
        const char = input[i];
        if (char === '(' || char === '[' || char === '{') {
            stack.push(char);
        } else if (char === ')' || char === ']' || char === '}') {
            // pop: Removes the last element from an array and returns it.
            // let lastElemetnt = stack.pop();
            // console.log('stack0:', stack);
            // console.log('lastElemetnt:',lastElemetnt)
            // console.log('char:',char)
            if (stack.length === 0 || !isMatchingPair(stack.pop(), char)) {
                return false; // Unbalanced parentheses
            }
        }
        console.log(stack);
    }

    return stack.length === 0; // If the stack is empty, all parentheses are balanced
}

function isMatchingPair(opening, closing) {
    return (opening === '(' && closing === ')') ||
        (opening === '[' && closing === ']') ||
        (opening === '{' && closing === '}');
}

// Example usage:
const input1 = "()";
// const input2 = "{[a + b] * (c - d)}";
// const input3 = "((a + b) * (c - d)";
// const input4 = "a + b) * (c - d)";
console.log(isRegular(input1)); // true
// console.log(isRegular(input2)); // true
// console.log(isRegular(input3)); // false
// console.log(isRegular(input4)); // false

// const stack2 = [1,2,3,4,5,6,7]
// let lastElemetnt = stack2.pop();
// console.log(lastElemetnt)
// console.log(stack2)