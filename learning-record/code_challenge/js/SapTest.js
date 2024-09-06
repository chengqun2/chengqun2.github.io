/**
 *  Question prompt: Given the 2-d array that contains only 0s and 1s, and all 0s come before all 1s in any given row.
	Find the first column containing a 1. 

	A binary matrix means that all elements are 0 or 1. 
	For each individual row of the matrix, this row is sorted in non-decreasing order.

	Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. 
	If such index doesn't exist, return -1.

	You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

	BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
	BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
 */

/**
 *  Input: mat = [[0,0],
				  [1,1]]
	Output: 0

	Input: mat = [[0,0],
				  [0,1]]
	Output: 1


	Input: mat = [[0,0],
				  [0,0]]
	Output: -1

	BinaryMatrix.get(1,2) = 1
	mat[1][2] = 1

	Input: mat = [[0,0,0,1],	0th row
				  [0,0,1,1],	1st row
				  [0,0,1,1]]	2nd row
	Output: 2

	Input: mat=[[0,0,0,0,0,0],  infinity
				[0,0,1,1,1,1],  2
				[0,0,0,0,0,1],  5
				[0,0,0,1,1,1],  3 
				[0,1,1,1,1,1]]  1 

	Expected output: 1 


	BinaryMatrix.get(row, col) 0 or 1  


	mat[r][c] => mat[1][2] = 1
 */

let row = BinaryMatrix.getNumberRows(); 5
let col = BinaryMatrix.getNumberCols(); 6 

let eachRowReturn = [];
for(let i=0; i<row; i++){
	for(let j=0; j<col;j++){
  	eachRowReturn.push(BinaryMatrix.get(i, j));  // O2  O1
  } 
}
// loop the eachRowReturn array
let returnNumbers = eachRowReturn.length;
let min = -1;
for(let i=0; i<returnNumbers; i++){
	// find the minum number in the array
  if (min < returnNumbers[i]){
  	min = returnNumbers[i];
  }
}
return min;









