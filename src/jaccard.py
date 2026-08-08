from src.base import SimilarityMetric


class JaccardSimilarity(SimilarityMetric):
    """Jaccard similarity: |intersection| / |union| (set-based)."""
    def calculate(self, s1: str, s2: str) -> float:
        set1 = set(s1)
        set2 = set(s2)
        inter = len(set1 & set2)
        union = len(set1 | set2)
        if union == 0:
            return 1.0  # both empty
        return inter / union
