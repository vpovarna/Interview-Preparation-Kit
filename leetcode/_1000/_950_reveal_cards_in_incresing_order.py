from ast import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        queue = deque(range(0, len(deck)))
        
        for n in deck:
            i = queue.popleft()
            res[i] = n
            
            if queue:
                queue.append(queue.popleft())
        
        return res