# https://leetcode.com/problems/roman-to-integer/
class Solution {
    
     HashMap<Character,Integer> map = new HashMap<Character,Integer>();
    
    public Solution() {
        map.put('h',0);
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
    }
    
    public int romanToInt(String s) {
        int ret=0;
        Character prev='h';
        for (int i=0; i<s.length(); i++){
            Character t = s.charAt(i);
            if (prev.equals('h')) {
                prev=t;
            }
            else if ((prev.equals('I') && (t.equals('V') || t.equals('X'))) || (prev.equals('X') && (t.equals('L') || t.equals('C'))) || (prev.equals('C') && (t.equals('D') || t.equals('M')))) {
                ret+=(-1*map.get(prev)+map.get(t));
                prev='h';
            }
            else {
                ret+=map.get(prev);
                prev=t;
            }
        }
        
        ret+=map.get(prev);
        return ret;
    }
}