from collections import Counter
from typing import List


def build_occurrence_map(tasks: List[int]) -> dict[int, int]:
    dic = dict()
    for t in tasks:
        dic[t] = dic.get(t, 0) + 1
    return dic


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # counter is building an occurrence map; Similar with: build_occurrence_map
        cnt = Counter(tasks)
        rounds = 0

        for v in cnt.values():
            if v == 1:
                return -1

            rounds += v // 3 if v % 3 == 0 else 1 + v // 3
            # equivalent with:
            # if v % 3 == 0:
            # rounds += v // 3
            # else:
            # rounds += 1 + v // 3

        return rounds


if __name__ == '__main__':
    print(Solution().minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
