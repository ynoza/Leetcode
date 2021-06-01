# https://leetcode.com/problems/search-suggestions-system/
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # products.sort()
        # print(products)
        dic=defaultdict(list)
        for prod in products:
            at=dic
            for c in prod:
                if c in at:
                    at=at[c]
                else:
                    at[c]=defaultdict(list)
                    at=at[c]
                at['word'].append(prod)
                
        # print(dic)
        ret=[]
        for i,c in enumerate(searchWord):
            if c in dic:
                dic=dic[c]
                ret.append(sorted(dic['word'])[:3])
            else:
                temp = [[] for j in range (len(searchWord)-i)]
                ret.extend(temp)
                return ret
        return ret