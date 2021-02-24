// https://leetcode.com/problems/sliding-window-maximum/
function maxSlidingWindow(nums: number[], k: number): number[] {
    let ret=[];
    let left=[];
    let right=[];
    for(let i=0; i <nums.length; i++){
        if (i==0 || i%k == 0){
            left[i]=nums[i];
        }
        else{
            left[i]=Math.max(left[i-1],nums[i]);
        }
        
        let rhs = nums.length-i-1;
        if (i==0 || rhs%k==0){
            right[rhs]=nums[rhs];
        }
        else{
            right[rhs]=Math.max(nums[rhs],right[rhs+1]);
        }
    }
    // console.log(left);
    // console.log(right);
    for (let i=0; i<nums.length-k+1; i++){
        ret[i]=Math.max(left[i+k-1],right[i]);
    }
    return ret;
};