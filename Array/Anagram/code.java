class Solution {
    public boolean isAnagram(String s, String t) {
        int [] arr = new int[26];
        int count =0;
        for (char x: s.toCharArray()) {
            arr[x-97]+=1;
            count+=1;
        }
        
        for (char x: t.toCharArray()){
            if (count==0 || arr[x-97]==0) return false;
            arr[x-97] -=1;
            count-=1;
        } 
        return (count==0);
    }
}