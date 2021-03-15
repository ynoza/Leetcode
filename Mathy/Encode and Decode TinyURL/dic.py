https://leetcode.com/problems/encode-and-decode-tinyurl/
class Codec:
    def __init__(self):
        self.s={}
        self.l={}
        self.alp="abcdefghijklmnopqrstuvwxyz"
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        s=""
        for i in range(len(longUrl)-1,-1,-8):
            val="".join(choices(self.alp,k=2))
            while(val in self.s):
                val="".join(choices(self.alp,k=2))
            self.s[val]=longUrl[max(i-7,0):i+1]
            s= val + s
        # print(s)
        return s
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        ret=""
        for i in range(len(shortUrl)-1,-1,-2):
            ret=self.s[shortUrl[max(0,i-1):i+1]] + ret
        return ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))