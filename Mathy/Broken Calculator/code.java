# https://leetcode.com/problems/broken-calculator/
class Solution {
    public int brokenCalc(int X, int Y) {
        int count =0;
        while(Y>X){
            if (Y%2==1) {
                count+=2;
                Y+=1;
                Y/=2;
            }
            else{
                count+=1;
                Y/=2;
            }
        }
        return count + X-Y;
    }
}

// 3 4 2
// 8 4 5
// 10 5 6 3 
// 1 2 3 4 5 6 7 ... 1024