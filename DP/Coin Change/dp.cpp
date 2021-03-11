# https://leetcode.com/problems/coin-change/
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount==0) return 0;
        vector <int> dp(amount+1,INT_MAX);
        dp[0]=0;
        for (int i=0; i <= amount;i++){
            for (auto v: coins){
                if (i-v>=0 && dp[i-v]!=INT_MAX && dp[i]> dp[i-v]+1){
                    dp[i]=dp[i-v]+1;
                }
            }
        }
        return ((dp[amount] == INT_MAX) ? -1 : dp[amount]);
    }
};
        