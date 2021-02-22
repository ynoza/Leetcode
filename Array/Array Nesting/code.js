/** https://leetcode.com/problems/array-nesting/
 * @param {number[]} nums
 * @return {number}
 */
var arrayNesting = function(nums) {
    var max_val=0;
    for(var i=0; i<nums.length; i++){
        var j = i;
        for(var count=0; nums[j]!==-1; count++){
            var temp = j;
            j=nums[j];
            nums[temp]=-1;
        } 
        max_val=Math.max(max_val,count);
    }
    return max_val;
};