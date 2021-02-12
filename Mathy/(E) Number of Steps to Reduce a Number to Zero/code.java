// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
class Solution {
    public int recur (int num, int count){
        if (num == 1) return count;
        else if (num == 2) return count+1;
        else if (Math.log(num) % Math.log(2) == 0) return count + (int) (Math.log(num) / Math.log(2));
        else if (num % 2 == 0) return recur(num/2,count+1);
        else return recur(num-1,count+1);
    }
    public int numberOfSteps (int num) {
        if (num==0) return 0;
        int count = 1;
        while(num>1){
            if (Math.log(num) % Math.log(2) == 0) return count + (int) (Math.log(num) / Math.log(2));
            else if (num % 2 == 0) {
                num/=2;
                count+=1;
            }
            else{
                num-=1;
                count+=1;
            }
        }
        return count;
    }
}