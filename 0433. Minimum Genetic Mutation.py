class Solution:
    def compareGenes(self, g1: str, g2: str) -> bool:
        diff = False
        for i in range(8):
            if g1[i] != g2[i]:
                if diff:
                    return False
                diff = True
        return True
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        # end gene not in bank; unsolvable
        if endGene not in bank:
            return -1

        try:
            bank.remove(startGene)
        except KeyError:
            pass

        q = deque([startGene])
        ans = 0
        while q:
            # since the end gene must be in bank (as confirmed above),
            # and the gene bank is empty, then the end gene must
            # be in the queue and will be popped on the current iteration
            if not bank:
                return ans

            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endGene:
                    return ans

                for gene in list(bank):
                    if self.compareGenes(cur, gene):
                        q.append(gene)
                        bank.remove(gene)
                
            ans += 1

        return -1
