import doctest


class Car:
    """ Базовый класс автомобиля. """
    def __init__(self, colour: str, model: str, brand: str):
        """
               Создание и подготовка к работе объекта "Автомобиль"

               :param colour: Цвет автомобиля
               :param model: Модель автомобиля
               :param brand: Марка автомобиля

               :raise TypeError: Если цвет автомобиля, его модель или марка не строкового типа, вызываем ошибку

               Примеры:
               >>> car = Car("Silver", "GLE", "Mercedes-Benz")  # инициализация экземпляра класса

            """
        if not isinstance(colour, str) or not isinstance(model, str) or not isinstance(brand, str):
            raise TypeError("Цвет автомобиля, его модель и марка должны быть строкового типа")
        self._colour = colour
        self._model = model
        self._brand = brand

    def __str__(self):
        """
            "Магический" метод __str__
            Ничего не принимает (кроме self)
            Возвращает строку, содержащую информацию об экземпляре класса

            :return: f"Цвет автомобиля: {self._colour}. Модель: {self._model}. Марка: {self._brand}"

            Примеры:
            >>> car = Car("Silver", "GLE", "Mercedes-Benz")
            >>> print(f"{car}")
            Цвет автомобиля: Silver. Модель: GLE. Марка: Mercedes-Benz
        """
        return f"Цвет автомобиля: {self._colour}. Модель: {self._model}. Марка: {self._brand}"

    def __repr__(self):
        """
            "Магический" метод __repr__
            Ничего не принимает (кроме self)
            Возвращает строку, по которой можно инициализировать экземпляр класса

            :return: f"{self.__class__.__name__}(colour={self._colour!r}, model={
            self._model!r}, brand={self._brand!r})"

            Примеры:
            >>> car = Car("Silver", "GLE", "Mercedes-Benz")
            >>> print(f"{car!r}")
            Car(colour='Silver', model='GLE', brand='Mercedes-Benz')
        """
        return f"{self.__class__.__name__}(colour={self._colour!r}, model={self._model!r}, brand={self._brand!r})"

    @property
    def colour(self) -> str:
        """
           Метод get. Возвращает значение атрибута colour (цвет автомобиля). Ничего не принимает (кроме self) У
           атрибута есть только getter, так как цвет автомобиля редко меняется с момента его производства, поэтому
           задаётся только один раз при создании объекта

           :return: self._colour

        """
        return self._colour

    @property
    def model(self) -> str:
        """
            Метод get. Возвращает значение атрибута model (модель автомобиля). Ничего не принимает (кроме self) У
            атрибута есть только getter, так как модель автомобиля не меняется с момента его производства, поэтому
            задаётся только один раз при создании объекта

            :return: self._model

        """
        return self._model

    @property
    def brand(self) -> str:
        """
           Метод get. Возвращает значение атрибута brand (марка автомобиля). Ничего не принимает (кроме self) У
           атрибута есть только getter, так как марка автомобиля не меняется с момента его производства, поэтому
           задаётся только один раз при создании объекта

           :return: self._brand

        """
        return self._brand

    def drive(self, speed: float) -> float:
        """
           Метод показывает, что автомобиль может ехать.
           Принимает и возвращает сокрость (в км/ч), с которой автомобиль едет

           :param speed: сокрость (в км/ч), с которой автомобиль едет
           :return: возвращает сокрость (в км/ч), с которой автомобиль едет

           :raise TypeError: Если скорость автомобиля не является числом с плавающей точкой, вызываем ошибку
           :raise ValueError: Если скорость автомобиля не является положительным числом, вызываем ошибку

           Примеры:
           >>> car = Car("Silver", "GLE", "Mercedes-Benz")
           >>> car.drive(65.6)
           65.6
        """
        if not isinstance(speed, float):
            raise TypeError("Скорость автомобиля должна быть числом с плавающей точкой")
        if speed <= 0:
            raise ValueError("Скорость автомобиля должна быть больше нуля")
        return speed

    def transport_people(self, count_of_people: int) -> None:
        """
                 Метод показывает, что автомобиль может перевозить людей.
                 Принимает количество пассажиров
                 Ничего не возвращает (кроме None)
                 Выводит сообщение: "Пассажиры доехали до пункта назначения"

                 :param count_of_people: количество людей, которых автомобиль перевозит
                 :return: None

                 :raise TypeError: Если количество людей в автомобиле не является целым числом, вызываем ошибку
                 :raise ValueError: Если количество людей в автомобиле не является положительным числом, вызываем ошибку

                 Примеры:
                 >>> car = Car("Silver", "GLE", "Mercedes-Benz")
                 >>> car.transport_people(5)
                 Пассажиры доехали до пункта назначения

            """
        if not isinstance(count_of_people, int):
            raise TypeError("Количество людей в автомобиле должно быть целым числом")
        if count_of_people <= 0:
            raise ValueError("Количество людей в автомобиле должно быть больше нуля")
        print("Пассажиры доехали до пункта назначения")


class PassengerCar(Car):
    """ Класс легкового автомобиля. """

    def __init__(self, colour: str, model: str, brand: str, child_seat: bool):
        """
           Создание и подготовка к работе объекта "Легковой автомобиль"

           :param colour: Цвет автомобиля
           :param model: Модель автомобиля
           :param brand: Марка автомобиля
           :param child_seat: Наличие детского сиденья в автомобиле

           Сначала вызывается конструктор базового класса (в него передаются первые 3 параметра)
           Добавляется параметр child_seat (наличие детского сиденья), т. к. детей можно перевозить
           не в любом автомобиле
           :raise TypeError: Если наличие или отсутствие детского сиденья в легковом автомобиле не является
           логическим значением, вызываем ошибку

           Примеры:
           >>> car = PassengerCar("Silver", "GLE", "Mercedes-Benz", True)  # инициализация экземпляра класса

        """
        super().__init__(colour=colour, model=model, brand=brand)
        self.child_seat = child_seat

    def __repr__(self):
        """
           "Магический" метод __repr__
           Ничего не принимает (кроме self).
           Возвращает строку, по которой можно инициализировать экземпляр класса.
           Метод переопределяется в производном классе, так как у этого класса другие название и количество
           параметров.
           Соотвестственно, и строка, по которой можно инициализировать экземпляр класса, будет выглядеть
           немного по-другому

           :return: f"{self.__class__.__name__}(colour={self._colour!r}, model={self._model!r},
           brand={self._brand!r}, " \
           f"child_seat={self._child_seat})"

           Примеры:
           >>> car = PassengerCar("Silver", "GLE", "Mercedes-Benz", True)
           >>> print(f"{car!r}")
           PassengerCar(colour='Silver', model='GLE', brand='Mercedes-Benz', child_seat=True)

        """

        return f"{self.__class__.__name__}(colour={self._colour!r}, model={self._model!r}, brand={self._brand!r}, " \
               f"child_seat={self._child_seat})"

    def __str__(self):
        """
           "Магический" метод __str__
           Ничего не принимает (кроме self)
           Возвращает строку, содержащую информацию об экземпляре класса.
           Переопределяется, так как в производном классе добавляется атрибут

           :return: f"Цвет автомобиля: {self._colour}. Модель: {self._model}. Марка: {self._brand}.
           Наличие детского сиденья: {self._child_seat}"

           Примеры:
           >>> car = PassengerCar("Silver", "GLE", "Mercedes-Benz", True)
           >>> print(f"{car}")
           Цвет автомобиля: Silver. Модель: GLE. Марка: Mercedes-Benz. Наличие детского сиденья: True

        """

        return f"Цвет автомобиля: {self._colour}. Модель: {self._model}. Марка: {self._brand}. " \
               f"Наличие детского сиденья: {self._child_seat}"

    @property
    def child_seat(self) -> bool:
        """
           Метод get. Возвращает значение атрибута child_seat (наличие детского сиденья в автомобиле).
           Ничего не принимает (кроме self)

           :return: self._child_seat

           Примеры:
           >>> car = PassengerCar("Silver", "GLE", "Mercedes-Benz", True)
           >>> print(car._child_seat)
           True
        """
        return self._child_seat

    @child_seat.setter
    def child_seat(self, child_seat: bool) -> None:
        """
           Метод set. Устанавливает значение атрибута child_seat (наличие детского сиденья в автомобиле).
           У атрибута есть setter, так как он может меняться (можно поставить сиденье или убрать)

           :param child_seat: наличие или отсутствие детского сиденья в автомобиле (True или False)
           :return: None
           :raise TypeError: Если наличие или отсутствие детского сиденья в легковом автомобиле не является
           логическим значением, вызываем ошибку

           Примеры:
           >>> car = PassengerCar("Silver", "GLE", "Mercedes-Benz", True)
           >>> car._child_seat = False

        """
        if not isinstance(child_seat, int):
            raise TypeError("Наличие или отсутствие детского сиденья в легковом автомобиле должно быть логическим "
                            "значением")
        self._child_seat = child_seat

    def transportation_of_people(self, count_of_people: int) -> None:
        """
           Метод показывает, что легковой автомобиль может перевозить людей.
           Принимает количество пассажиров.
           Ничего не возвращает (кроме None).
           Выводит сообщение: "Пассажиры доехали до пункта назначения".
           Если атрибут child_seat = True, выводит сообщение: "Можно перевозить детей".
           Метод переопределяется в производном классе, так как выполняет дополнительную проверку

           :param count_of_people: количество людей, которых автомобиль перевозит
           :return: None

           :raise TypeError: Если количество людей в автомобиле не является целым числом, вызываем ошибку
           :raise ValueError: Если количество людей в автомобиле не является положительным числом, вызываем ошибку

           Примеры:
           >>> car = Car("Silver", "GLE", "Mercedes-Benz")
           >>> car.transport_people(5)
           Пассажиры доехали до пункта назначения

        """
        if not isinstance(count_of_people, int):
            raise TypeError("Количество людей в автомобиле должно быть целым числом")
        if count_of_people <= 0:
            raise ValueError("Количество людей в автомобиле должно быть больше нуля")
        if self._child_seat:
            print("Можно перевозить детей")
        print("Пассажиры доехали до пункта назначения")


class Truck(Car):
    """ Класс грузового автомобиля. """
    def __init__(self, colour: str, model: str, brand: str, body_capacity: float):
        """
           Создание и подготовка к работе объекта "Грузовой автомобиль"

           :param colour: Цвет автомобиля
           :param model: Модель автомобиля
           :param brand: Марка автомобиля
           :param body_capacity: Ёмкость кузова грузового автомобиля

           Сначала вызывается конструктор базового класса (в него передаются первые 3 параметра)
           Добавляется параметр body_capacity (ёмкость кузова), т. к. кузов с определённой ёмкостью есть
           не в любом автомобиле
           :raise TypeError: Если ёмкость кузова грузового автомобиля не является числом с плавающей точкой,
           вызываем ошибку
           :raise ValueError: Если ёмкость кузова грузового автомобиля не является положительным значением,
           вызываем ошибку

           Примеры:
           >>> car = Truck("Yellow", "MB700", "Mercedes-Benz", 50.0)  # инициализация экземпляра класса

        """
        super().__init__(colour=colour, model=model, brand=brand)
        self.body_capacity = body_capacity

    def __repr__(self):
        """
           "Магический" метод __repr__
           Ничего не принимает (кроме self).
           Возвращает строку, по которой можно инициализировать экземпляр класса.
           Метод переопределяется в производном классе, так как у этого класса другие название и количество
           параметров.
           Соотвестственно, и строка, по которой можно инициализировать экземпляр класса, будет выглядеть
           немного по-другому

           :return: f"{self.__class__.__name__}(colour={self._colour!r}, model={self._model!r},
           brand={self._brand!r}, " \
           f"body_capacity={self._body_capacity})"

           Примеры:
           >>> car = Truck("Yellow", "MB700", "Mercedes-Benz", 50.0)
           >>> print(f"{car!r}")
           Truck(colour='Yellow', model='MB700', brand='Mercedes-Benz', body_capacity=50.0)

        """

        return f"{self.__class__.__name__}(colour={self._colour!r}, model={self._model!r}, brand={self._brand!r}, " \
               f"body_capacity={self._body_capacity})"

    def __str__(self):
        """
           "Магический" метод __str__
           Ничего не принимает (кроме self).
           Возвращает строку, содержащую информацию об экземпляре класса.
           Переопределяется, так как в производном классе добавляется атрибут

           :return: f"Цвет автомобиля: {self._colour}. Модель: {self._model}. Марка: {self._brand}.
           Ёмкость кузова: {self._body_capacity}"

           Примеры:
           >>> car = Truck("Yellow", "MB700", "Mercedes-Benz", 50.0)
           >>> print(f"{car}")
           Цвет автомобиля: Yellow. Модель: MB700. Марка: Mercedes-Benz. Ёмкость кузова: 50.0

        """

        return f"Цвет автомобиля: {self._colour}. Модель: {self._model}. Марка: {self._brand}. " \
               f"Ёмкость кузова: {self._body_capacity}"

    @property
    def body_capacity(self) -> float:
        """
           Метод get. Возвращает значение атрибута body_capacity (ёмкость кузова автомобиля).
           Ничего не принимает (кроме self)

           :return: self._body_capacity

           Примеры:
           >>> car = Truck("Silver", "GLE", "Mercedes-Benz", 50.0)
           >>> print(car._body_capacity)
           50.0
        """
        return self._body_capacity

    @body_capacity.setter
    def body_capacity(self, body_capacity: float) -> None:
        """
           Метод set. Устанавливает значение атрибута body_capacity (ёмкость кузова автомобиля).
           У атрибута есть setter, так как он может меняться (можно убрать кузов).

           :param body_capacity: Ёмкость кузова автомобиля
           :return: None
           :raise TypeError: Если ёмкость кузова грузового автомобиля не является числом с плавающей точкой,
           вызываем ошибку
           :raise ValueError: Если ёмкость кузова грузового автомобиля не является положительным значением,
           вызываем ошибку

           Примеры:
           >>> car = Truck("Yellow", "MB700", "Mercedes-Benz", 50.0)
           >>> car._body_capacity = 55.0

        """
        if not isinstance(body_capacity, float):
            raise TypeError("Ёмкость кузова грузового автомобиля должна быть числом с плавающей точкой")
        if body_capacity <= 0:
            raise ValueError("Ёмкость кузова грузового автомобиля должна быть больше нуля")
        self._body_capacity = body_capacity

    def transport_people(self, count_of_people: int) -> None:
        """
           Метод показывает, что грузовой автомобиль может перевозить людей.
           Принимает количество пассажиров.
           Ничего не возвращает (кроме None).
           Выводит сообщение: "Пассажиры доехали до пункта назначения".
           Если атрибут body_capacity > 36, выводит сообщение: "Можно перевозить большие грузы".
           Метод переопределяется в производном классе, так как выполняет дополнительную проверку

           :param count_of_people: количество людей, которых автомобиль перевозит
           :return: None

           :raise TypeError: Если количество людей в автомобиле не является целым числом, вызываем ошибку
           :raise ValueError: Если количество людей в автомобиле не является положительным числом, вызываем ошибку

           Примеры:
           >>> car = Truck("Yellow", "MB700", "Mercedes-Benz", 50.0)
           >>> car.transport_people(5)
           Можно перевозить большие грузы
           Пассажиры доехали до пункта назначения

        """
        if not isinstance(count_of_people, int):
            raise TypeError("Количество людей в автомобиле должно быть целым числом")
        if count_of_people <= 0:
            raise ValueError("Количество людей в автомобиле должно быть больше нуля")
        if self.body_capacity > 36:
            print("Можно перевозить большие грузы")
        print("Пассажиры доехали до пункта назначения")


if __name__ == "__main__":

    doctest.testmod()  # тестирование примеров, которые находятся в документации

    pass
