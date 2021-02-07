class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int>lr(s.size(),INT_MAX);
        vector<int>rl(s.size(),INT_MAX);
        vector<int>ret(s.size(), INT_MAX);
        int val1=INT_MAX;
        int val2=INT_MAX;
        for (int i=0; i<s.size();i++){
            char t =s[i];
            if (t==c) {
                lr[i]=0;
                val1=0;
            }
            else if (val1==INT_MAX) lr[i]=val1;
            else lr[i]=++val1;
            
            char g =s[s.size()-1-i];
            if (g==c) {
                rl[s.size()-1-i] = 0;
                val2=0;
            }
            else if (val2==INT_MAX) rl[s.size()-1-i]=val2;
            else rl[s.size()-1-i]=++val2;
            
            ret[i]=min(lr[i],rl[i]);
            ret[s.size()-1-i]=min(lr[s.size()-1-i],rl[s.size()-1-i]);
            
        }
        return ret;
        
    }
};