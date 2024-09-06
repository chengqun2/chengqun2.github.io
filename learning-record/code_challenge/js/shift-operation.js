/**
 * Why Use >> 1 Instead of / 2?
    Performance: In some low-level languages, bitwise operations are faster than arithmetic division.
    Integer Arithmetic: It ensures the result is an integer without needing to handle the fractional part, which is crucial in binary search or similar algorithms.
 */

//  right shift operator means divide
//  >> 1 means divide by 2, >> 2 means divide by 4 (2*2), >> 3 means divide by 8 (2*2*2) etc.
const mid = -10 >> 1
console.log(mid)


//  left shift operator means multiply(times)
//  << 1 means times 2, << 2 means times 4 (2*2), << 3 means times 8 (2*2*2) etc.
const double = 10 << 3
console.log(double)