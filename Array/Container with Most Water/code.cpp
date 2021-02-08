class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0;
        int r=height.size()-1;
        int max_val=0;
        while(l<r){
            max_val=max(min(height[l],height[r])*(r-l),max_val);
            if (height[l]<height[r]) l++;
            else r--;
        }
        return max_val;
    }
};