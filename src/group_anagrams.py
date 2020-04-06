class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            buckets = {}
            for w in strs:
                sorted_w = ''.join(sorted(w))
                if sorted_w not in buckets:
                    buckets[sorted_w] = [w]
                else:
                    buckets[sorted_w].append(w)


            return buckets.values()
