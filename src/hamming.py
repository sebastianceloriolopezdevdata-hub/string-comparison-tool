from src.base import SimilarityMetric


class HammingDistance(SimilarityMetric):
    """Hamming distance: counts different positions (strings of equal length)."""
    def calculate(self, s1: str, s2: str):
        if len(s1) != len(s2):
            return None  # invalid input
        return sum(1 for a, b in zip(s1, s2) if a != b)
