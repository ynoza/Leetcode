# https://leetcode.com/problems/reconstruct-original-digits-from-english/
class Solution:
    def originalDigits(self, s: str) -> str:
        d=Counter(s)
        dp=[0] * 10
            
        numbers = ["zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine"
                  ]
        
        lst=[[0,'z'],[2,'w'],[4,'u'],[6,'x'],[8,'g'],[1,'o'],[3,'h'],[5,'f'],[7,'v'],[9,'i']]
        
        for x,y in lst:
            val = d[y]
            dp[x]+=val
            for c in numbers[x]: d[c]-=val
        
        return "".join([str(i)*dp[i] for i in range(10)])     