class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> currentList;
        dfs(res, s, 0, currentList);
        return res;
        
    }
    
    void dfs(vector<vector<string>> &result, string &s, int start, vector<string>&currentList){
        if (start >= s.length()) result.push_back(currentList);
        for (int end = start; end < s.length(); end++){
            if (isPalindrome(s, start, end)){
                 currentList.push_back(s.substr(start, end - start + 1));
                 dfs(result, s, end + 1, currentList);
                 currentList.pop_back();
            }
            
        }
    }
        
    
    bool isPalindrome(string &s, int i, int j){
       
        while(i<j){
            if(s[i++]!=s[j--]){
                return false;
            }
        }
        return true;
    }
};