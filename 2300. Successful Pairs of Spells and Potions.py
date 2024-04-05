# max( O(m log m), O(n log m) ) time and O(n) space complexity,
# where n = len(spells) and m = len(potions)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # O(n) space complexity
        ret = []

        # O(m log m) time complexity
        potions = sorted(potions)
        n = len(potions)
        
        # O(n log m) time complexity
        for spell in spells:

            # normalize success strength with the potion's strength
            limit = math.ceil(success / spell)

            L = bisect.bisect_left(potions, limit)
            ret.append(n - L)

        return ret
