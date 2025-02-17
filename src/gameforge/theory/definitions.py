"""

"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class GameTheoryConcept:
    """
    Represents a game theory concept with it term(s), definition and related metadata
    """
    term: str
    definition: str
    examples: List[str] = field(default_factory=list)
    origin: Optional[str] = None
    related_terms: List[str] = field(default_factory=list)

    def __str__(self):
        return self.term


class GameTheoryGlossary:
    """"""
    def __init__(self):
        self.concepts: Dict[str, GameTheoryConcept] = {}

    def add_concept(self, concept: GameTheoryConcept) ->  None:
        """

        :param concept:
        :return:
        """

        self.concepts[concept.term.lower()] = concept


    def get_concept(self, term: str) -> Optional[GameTheoryConcept]:
        return self.concepts[term.lower()]

    def search(self, query: str) -> List[GameTheoryConcept]:
        query_lower = query.lower()
        results = []
        for concept in self.concepts.values():
            if query_lower in concept.term.lower() or query_lower in concept.definition:
                results.append(concept)

        return results


