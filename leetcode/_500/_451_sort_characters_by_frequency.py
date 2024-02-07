from typing import Dict
from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        dict = self.invert_dict(self.get_occurrence(s))
        keys = list(dict.keys())
        keys.sort(reverse=True)
        
        ans = ""
        for k in keys:
            for v in dict[k]:
                ans += k*v

        return ans
    
    def get_occurrence(self, s: str) -> Dict[str,int]:
        dict = defaultdict(int)
        for c in s:
            dict[c] +=1
        return dict
        
    def invert_dict(self, dict: Dict[str, int]) -> Dict[str, int]:
        inverted_dict = defaultdict(list)
        for k,v in dict.items():
            inverted_dict[v].append(k)
        return inverted_dict


if __name__ == '__main__':
    print(Solution().frequencySort("tree"))