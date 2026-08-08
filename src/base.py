from abc import ABC, abstractmethod

class SimilarityMetric(ABC):
    """Base abstraction on which all high-level modules depend.
    Complies with the Dependency Inversion Principle (DIP) of SOLID.
    """
    @abstractmethod
    def calculate(self, s1: str, s2: str):
        """Returns a numeric value or None if the input is invalid."""
        pass

