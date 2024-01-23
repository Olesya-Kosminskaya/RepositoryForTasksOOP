class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str) or not isinstance(author, str):
            raise TypeError("Название книги и фамилия автора должны быть строкового типа")
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть целым положительным числом")
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть целым положительным числом")
        self._pages = pages


class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть числом")
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть больше нуля")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть числом")
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть больше нуля")
        self._duration = duration
