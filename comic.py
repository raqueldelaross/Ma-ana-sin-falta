from typing import TypeVar, Generic

T = TypeVar('T')


# crear objeto comic
# tipo de datos genericos
class Comic(Generic[T]):
    def __init__(self,
                 comics_title: str,
                 image: str,
                 description: str,
                 creators: list,
                 characters: list):
        self.comic_title = comics_title
        self.image = image
        self.description = description
        self.creators = creators
        self.characters = characters

