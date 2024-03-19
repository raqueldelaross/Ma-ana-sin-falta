from typing import TypeVar, Generic

T = TypeVar('T')


class Character(Generic[T]):
    def __init__(self,
                 character_name: str,
                 image: str,
                 description: str,
                 comic: list,
                 serie: list):
        self.character_name = character_name
        self.image = image
        self.description = description
        self.comic = comic
        self.serie = serie
