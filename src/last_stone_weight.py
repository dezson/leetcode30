class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return
        for _ in range(len(stones) -1):
            stones.sort()
            stones.append(stones.pop() - stones.pop())
        return stones[0]

    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return
        while len(stones) != 1:
            srtd = sorted(stones, reverse=True)
            fst, snd = srtd[:2]
            if fst-snd == 0:
                if len(srtd) > 2:
                    stones = srtd[2:]
                else: return 0
            else:
                stones = srtd[2:] + [fst-snd]
        return stones[0]
