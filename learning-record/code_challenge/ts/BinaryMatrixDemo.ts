// Interface representing the BinaryMatrix's methods for TypeScript type checking
interface BinaryMatrix {
    get(row: number, col: number): number;
    dimensions(): number[];
}

/**
 *  
 * @param binaryMatrix [[0,1,1],
 *                      [1,1,1],
 *                      [0,0,1]]
 * @returns 
 */
function leftMostColumnWithOne(binaryMatrix: BinaryMatrix) {
    const [m, n] = binaryMatrix.dimensions();
    let ans = n;
    for (let i = 0; i < m; ++i) {
        let [l, r] = [0, n];
        while (l < r) {
            const mid = (l + r) >> 1;
            if (binaryMatrix.get(i, mid) === 1) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        ans = Math.min(ans, l);
    }
    return ans >= n ? -1 : ans;
}

