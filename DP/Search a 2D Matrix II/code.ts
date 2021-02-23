// https://leetcode.com/problems/search-a-2d-matrix-ii/
function searchMatrix(matrix: number[][], target: number): boolean {
    const m = matrix.length;
    const n = matrix[0].length;
    
    let j=n-1;
    let i=0;
    while(i>=0 && j>=0 && j<n && i<m){
        if (matrix[i][j]===target) return true;
        else if (matrix[i][j]<target) i+=1;
        else j-=1;
    }
    return false;
};