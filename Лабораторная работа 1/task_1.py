# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Cat:
    def __init__(self, name_: str, age_: int, weight_: int):

        """
                Создание и подготовка к работе объекта "Кот"

                :param name_: Имя кота
                :param age_: Возраст кота
                :param weight_: Вес кота

                :raise TypeError: Если имя написано не буквами, вызываем ошибку
                :raise TypeError: Если возраст не является целым числом, вызываем ошибку
                :raise ValueError: Если возраст не является положительным числом, вызываем ошибку
                :raise TypeError: Если вес не является целым числом, вызываем ошибку
                :raise ValueError: Если вес не является положительным числом, вызываем ошибку

                Примеры:
                >>> cat = Cat("Barsik", 8, 5)  # инициализация экземпляра класса
        """

        self.name = name_
        if not isinstance(name_, str):
            raise TypeError("Имя должно быть написано буквами")

        self.age = age_
        if not isinstance(age_, int):
            raise TypeError("Возраст должен быть целым числом")
        if age_ < 0:
            raise ValueError("Возраст должен быть положительным числом")

        self.weight = weight_
        if not isinstance(weight_, int):
            raise TypeError("Вес должен быть целым числом")
        if weight_ < 0:
            raise ValueError("Вес должен быть положительным числом")

    def say(self) -> None:
        """ 
            Метод демонстрирует, как может общаться кот.
            Ничего не принимает (кроме self) и не возвращает (кроме None)

            :return: None

            Пример:
            >>> cat = Cat("Barsik", 8, 5)
            >>> cat.say()
            Meow
        """
        print("Meow")

    def sleep(self, time_in_hours: float) -> float:
        """ 
            Метод показывает, что кот может спать.
            Принимает и возвращает количество времени (в часах), которое кот спит

            :param time_in_hours: Количество времени (в часах), которое кот спит
            :return: возвращает количество времени (в часах), которое кот спит

            :raise TypeError: Если количество часов сна не является числом с плавающей точкой, вызываем ошибку
            :raise ValueError: Если количество часов сна не является положительным числом, вызываем ошибку

            Примеры:
            >>> cat = Cat("Barsik", 8, 5)
            >>> cat.sleep(7.5)
            Z-z-z-z-z-z
            7.5
        """
        if not isinstance(time_in_hours, float):
            raise TypeError("Количество часов должно быть числом с плавающей точкой")
        if time_in_hours <= 0:
            raise ValueError("Количество часов должно быть положительным числом")
        print("Z-z-z-z-z-z")
        return time_in_hours


class Hedgehog:
    def __init__(self, name_: str, age_: int):

        """
            Создание и подготовка к работе объекта "Ёж"

            :param name_: Имя ежа
            :param age_: Возраст ежа

            :raise TypeError: Если имя написано не буквами, вызываем ошибку
            :raise TypeError: Если возраст не является целым числом, вызываем ошибку
            :raise ValueError: Если возраст не является положительным числом, вызываем ошибку

            Примеры:
            >>> hedgehog = Hedgehog("Emma", 5)  # инициализация экземпляра класса
        """

        self.name = name_
        if not isinstance(name_, str):
            raise TypeError("Имя должно быть написано буквами")

        self.age = age_
        if not isinstance(age_, int):
            raise TypeError("Возраст должен быть целым числом")
        if age_ < 0:
            raise ValueError("Возраст должен быть положительным числом")

    def say(self) -> None:
        """
            Метод демонстрирует, как может общаться ёж.
            Ничего не принимает (кроме self) и не возвращает (кроме None)

            :return: None

            Примеры:
            >>> hedgehog = Hedgehog("Emma", 5)
            >>> hedgehog.say()
            F-r-r-r-r
        """
        print("F-r-r-r-r")

    def run(self, time_in_hours: float) -> float:
        """
            Метод показывает, что ёж может бегать.
            Принимает и возвращает количество времени (в часах), которое ёж бегает

            :param time_in_hours: Количество времени (в часах), которое ёж бегает
            :return: возвращает количество времени (в часах), которое ёж бегает

            :raise TypeError: Если количество часов бега не является числом с плавающей точкой, вызываем ошибку
            :raise ValueError: Если количество часов бега не является положительным числом, вызываем ошибку

            Примеры:
            >>> hedgehog = Hedgehog("Emma", 5)
            >>> hedgehog.run(1.2)
            Top-top-top
            1.2
        """

        if not isinstance(time_in_hours, float):
            raise TypeError("Количество часов должно быть числом с плавающей точкой")
        if time_in_hours <= 0:
            raise ValueError("Количество часов должно быть положительным числом")
        print("Top-top-top")
        return time_in_hours

class Rabbit:
    def __init__(self, name_: str, age_: int):

        """
            Создание и подготовка к работе объекта "Кролик"

            :param name_: Имя кролика
            :param age_: Возраст кролика

            :raise TypeError: Если имя написано не буквами, вызываем ошибку
            :raise TypeError: Если возраст не является целым числом, вызываем ошибку
            :raise ValueError: Если возраст не является положительным числом, вызываем ошибку

            Примеры:
            >>> rabbit = Rabbit("Piter", 5)  # инициализация экземпляра класса
        """

        self.name = name_
        if not isinstance(name_, str):
            raise TypeError("Имя должно быть написано буквами")

        self.age = age_
        if not isinstance(age_, int):
            raise TypeError("Возраст должен быть целым числом")
        if age_ < 0:
            raise ValueError("Возраст должен быть положительным числом")

    def get_name(self) -> str:
        """
            Метод возвращает имя кролика
            :return: имя кролика

            Пример:
            >>> rabbit = Rabbit("Piter", 5)
            >>> rabbit.get_name()
            'Piter'
        """
        return self.name

    def jump(self, count_of_jumps: int) -> int:
        """
            Метод показывает, что кролик может прыгать.
            Принимает и возвращает количество прыжков

            :param count_of_jumps: Количество прыжков кролика

            :raise TypeError: Если количество прыжковне является целым числом, вызываем ошибку
            :raise ValueError: Если количество прыжков не является положительным числом, вызываем ошибку

            Пример:
            >>> rabbit = Rabbit("Piter", 5)
            >>> rabbit.jump(8)
            Hop-hop-hop
            8
        """
        if not isinstance(count_of_jumps, int):
            raise TypeError("Количество прыжков должно быть целым числом")
        if count_of_jumps <= 0:
            raise ValueError("Количество прыжков должно быть положительным числом")
        print("Hop-hop-hop")
        return count_of_jumps


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    doctest.testmod()  # тестирование примеров, которые находятся в документации

    pass
