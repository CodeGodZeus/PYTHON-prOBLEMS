class Solution:
    def frequencySort(self, s: str) -> str:
        res=""
        dict={}
        for char in s:
            if char not in dict:
                dict[char]=1
            else:
                dict[char]+=1
        s=sorted(dict,key=lambda x:dict[x],reverse=True)
        for i in s:
            res+=i*dict[i]
        return res
        
