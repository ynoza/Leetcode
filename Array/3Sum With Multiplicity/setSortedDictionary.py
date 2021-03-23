# https://leetcode.com/problems/3sum-with-multiplicity/submissions/
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter=Counter(arr)
        arr=set(arr)
        dp=defaultdict(list)
        lst=list(arr)
        lst.sort()
        # print(lst)
        ret=0
        for i in range(len(lst)):
            for j in range(i,len(lst)):
                val= target - lst[i]-lst[j]
                if val <lst[i] or val <lst[j]: continue
                elif val not in arr: continue 
                
                if val==lst[i] and val==lst[j]:
                    if counter[val]<3: continue
                    ret+=math.comb((counter[val]),3)
                elif val==lst[i]:
                    if counter[val]<2: continue
                    ret+=math.comb((counter[val]),2)*counter[lst[j]]
                elif val==lst[j]:
                    if counter[val]<2: continue
                    ret+=math.comb((counter[val]),2)*counter[lst[i]]
                elif lst[j]==lst[i]:
                    ret+=math.comb((counter[lst[i]]),2)*counter[val]
                else:
                    ret+=counter[lst[i]]*counter[lst[j]]*counter[val]

                
                # print(lst[i],lst[j],val)
                
            # arr.remove(lst[i])
        return ret %(10**9+7)
            
        