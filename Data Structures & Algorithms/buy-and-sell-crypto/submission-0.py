class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0

        for p in prices:
            min_price = min(min_price, p)      # meilleur prix d'achat jusqu'ici
            best = max(best, p - min_price)    # profit si je vends aujourd'hui

        return best