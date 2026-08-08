from collections import Counter
from src.base import SimilarityMetric


class TSimilarity(SimilarityMetric):
    """T similarity (Tanimoto with frequencies): sum of minimums / sum of maximums."""
    def calculate(self, s1: str, s2: str) -> float:
        c1 = Counter(s1)
        c2 = Counter(s2)
        all_keys = set(c1) | set(c2)
        num = sum(min(c1.get(k, 0), c2.get(k, 0)) for k in all_keys)
        den = sum(max(c1.get(k, 0), c2.get(k, 0)) for k in all_keys)
        if den == 0:
            return 1.0
        return num / den
