from collections import defaultdict
from typing import List, Dict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def build_word_char_map(s: str) -> Dict[str, List[int]]:
            s_map = defaultdict(list)
            for i, c in enumerate(s):
                s_map[c].append(i)
            return s_map
        
        s_map = build_word_char_map(s)
        t_map = build_word_char_map(t)
        
        return list(s_map.values()) == list(t_map.values())
                

if __name__ == "__main__":
    print(Solution().isIsomorphic("egg", "add"))        
