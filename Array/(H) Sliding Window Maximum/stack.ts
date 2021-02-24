// https://leetcode.com/problems/sliding-window-maximum/
function maxSlidingWindow(nums: number[], k: number): number[] {
    let ret=[];
    let lst=[];
    for(let i=0; i <nums.length; i++){
        while (lst.length >0 && lst[0]<=i-k){
            lst.shift();
        }
        while (lst.length >0 && nums[lst[lst.length-1]]<=nums[i]){
            lst.pop();
        }
        lst.push(i);
        // console.log(lst);
        if (i>=k-1) ret.push(nums[lst[0]]);
    }
    return ret;
};