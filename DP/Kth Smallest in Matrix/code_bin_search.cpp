class Solution {
public:
    int getcount(vector<vector<int>> &matrix,int mid)
{
	int i=matrix.size()-1,j=0,count=0;
	while(i>=0&j<matrix.size())
	{
		if(matrix[i][j]>mid)
			i--;
		else
		{
			count=count+i+1;
			j++;
		}
	}
	return count;
} 
int kthSmallest(vector<vector<int>>& matrix, int k) {
	int n=matrix.size();
	int low=matrix[0][0],high=matrix[n-1][n-1],ans=low;
	while(low<=high)
	{
		int mid=low+(high-low)/2;
		if(getcount(matrix,mid)>=k)
		{
			ans=mid;
			high=mid-1;
		}
		else
			low=mid+1;
	}
	return ans;
}
};