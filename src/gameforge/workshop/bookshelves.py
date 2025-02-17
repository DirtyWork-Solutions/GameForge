from typing import Optional, List


class Shelves:  # TODO: Make global
    def __init__(self):
        self._shelves = {
            "theory": [
                Glossary("default")
            ]
        }


class Glossary:  # TODO: Make a dynamic singleton
    def __init__(self, name: str = ''):
        self._terms = []


def generate_default_glossary() -> Optional[Glossary]:
    """
    Populate (and get) the populated default glossary.
    :return: (*Glossary*) Glossary object populated with the unique label 'default'.
    """

    populated_glossary = Glossary("default")
    return populated_glossary