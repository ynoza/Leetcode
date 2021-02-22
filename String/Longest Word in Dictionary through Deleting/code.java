# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
class Solution {
    public String findLongestWord(String s, List<String> d) {
        String ret="";
        int max_val=0;
        int l=s.length();
        for(int i=0;i<d.size(); i++){
            int start=0;
            int at_l = d.get(i).length();
            if (at_l <max_val) continue;
            int check = 0;
            for (int j=0; j<l && start < at_l && l-j>=at_l-start; j++){
                if ((s.charAt(j))==(d.get(i).charAt(start))){
                    if (check==0 && start<max_val){
                        check = (int)(d.get(i).charAt(start))-(int)(ret.charAt(start));
                    } 
                    start+=1;
                }
            }
            if (start == at_l && (max_val<at_l || (max_val==at_l && check<0))) {
                ret=d.get(i);
                max_val=at_l;
            }
        }
        return ret;
    }
}