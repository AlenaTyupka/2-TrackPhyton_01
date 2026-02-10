# TODO Написать 3 класса с документацией и аннотацией типов

from abc import ABC, abstractmethod
from typing import Optional


class Vehicle(ABC):
    """
    Абстрактный класс, описывающий транспортное средство.

    Attributes:
        max_speed (float): Максимальная скорость в км/ч (должна быть положительной).
        weight (float): Вес в кг (должен быть положительным).
        fuel_capacity (float): Ёмкость топливного бака в литрах (должна быть неотрицательной).
    """

    def __init__(self, max_speed: float, weight: float, fuel_capacity: float) -> None:
        """
        Инициализация транспортного средства.

        Args:
            max_speed: Максимальная скорость в км/ч
            weight: Вес в кг
            fuel_capacity: Ёмкость топливного бака в литрах

        Raises:
            ValueError: Если какие-либо параметры не удовлетворяют ограничениям.

        Examples:
            >>> car = Vehicle(200, 1500, 60)  # doctest: +SKIP
            Traceback (most recent call last):
            ...
            TypeError: Can't instantiate abstract class Vehicle...

            >>> class Car(Vehicle):
            ...     def accelerate(self, target_speed: float) -> float: ...
            ...     def brake(self, deceleration: float) -> float: ...
            ...     def refuel(self, amount: float) -> float: ...
            >>> test_car = Car(200, 1500, 60)
            >>> test_car.max_speed
            200
        """
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительной")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным")
        if fuel_capacity < 0:
            raise ValueError("Ёмкость топливного бака не может быть отрицательной")

        self.max_speed = max_speed
        self.weight = weight
        self.fuel_capacity = fuel_capacity

    @abstractmethod
    def accelerate(self, target_speed: float) -> float:
        """
        Ускорить транспортное средство до заданной скорости.

        Args:
            target_speed: Целевая скорость в км/ч

        Returns:
            float: Фактическая достигнутая скорость

        Examples:
            >>> class Car(Vehicle):
            ...     def accelerate(self, target_speed: float) -> float:
            ...         return min(target_speed, self.max_speed)
            ...     def brake(self, deceleration: float) -> float: ...
            ...     def refuel(self, amount: float) -> float: ...
            >>> car = Car(200, 1500, 60)
            >>> car.accelerate(150)
            150
            >>> car.accelerate(250)
            200
        """
        ...

    @abstractmethod
    def brake(self, deceleration: float) -> float:
        """
        Затормозить транспортное средство.

        Args:
            deceleration: Величина замедления в м/с² (должна быть положительной)

        Returns:
            float: Скорость после торможения

        Raises:
            ValueError: Если deceleration <= 0

        Examples:
            >>> class Car(Vehicle):
            ...     def accelerate(self, target_speed: float) -> float: ...
            ...     def brake(self, deceleration: float) -> float:
            ...         if deceleration <= 0:
            ...             raise ValueError("Замедление должно быть положительным")
            ...         return 0.0
            ...     def refuel(self, amount: float) -> float: ...
            >>> car = Car(200, 1500, 60)
            >>> car.brake(5)
            0.0
        """
        ...

    @abstractmethod
    def refuel(self, amount: float) -> float:
        """
        Заправить транспортное средство.

        Args:
            amount: Количество топлива для заправки в литрах

        Returns:
            float: Фактически заправленное количество топлива

        Examples:
            >>> class Car(Vehicle):
            ...     def __init__(self, max_speed: float, weight: float, fuel_capacity: float):
            ...         super().__init__(max_speed, weight, fuel_capacity)
            ...         self.fuel = 0
            ...     def accelerate(self, target_speed: float) -> float: ...
            ...     def brake(self, deceleration: float) -> float: ...
            ...     def refuel(self, amount: float) -> float:
            ...         fuel_needed = self.fuel_capacity - self.fuel
            ...         added = min(amount, fuel_needed)
            ...         self.fuel += added
            ...         return added
            >>> car = Car(200, 1500, 60)
            >>> car.refuel(70)
            60
        """
        ...


class Furniture(ABC):
    """
    Абстрактный класс, описывающий предмет мебели.

    Attributes:
        material (str): Материал изготовления (не пустая строка).
        dimensions (tuple[float, float, float]): Габариты (длина, ширина, высота) в см.
        color (str): Цвет предмета мебели.
    """

    def __init__(self, material: str, dimensions: tuple[float, float, float], color: str) -> None:
        """
        Инициализация предмета мебели.

        Args:
            material: Материал изготовления
            dimensions: Кортеж из трёх чисел (длина, ширина, высота) в см
            color: Цвет

        Raises:
            ValueError: Если material - пустая строка или dimensions содержит неположительные значения

        Examples:
            >>> chair = Furniture("wood", (50, 50, 100), "brown")  # doctest: +SKIP
            Traceback (most recent call last):
            ...
            TypeError: Can't instantiate abstract class Furniture...

            >>> class Chair(Furniture):
            ...     def assemble(self) -> bool: ...
            ...     def disassemble(self) -> bool: ...
            ...     def repaint(self, new_color: str) -> None: ...
            >>> my_chair = Chair("wood", (50, 50, 100), "brown")
            >>> my_chair.material
            'wood'
        """
        if not material or not material.strip():
            raise ValueError("Материал не может быть пустым")
        if len(dimensions) != 3:
            raise ValueError("Размерности должны содержать 3 значения")
        for dim in dimensions:
            if dim <= 0:
                raise ValueError("Все размеры должны быть положительными")

        self.material = material
        self.dimensions = dimensions
        self.color = color

    @abstractmethod
    def assemble(self) -> bool:
        """
        Собрать предмет мебели.

        Returns:
            bool: True если сборка успешна, False в противном случае

        Examples:
            >>> class Chair(Furniture):
            ...     def __init__(self, material: str, dimensions: tuple[float, float, float], color: str):
            ...         super().__init__(material, dimensions, color)
            ...         self.is_assembled = False
            ...     def assemble(self) -> bool:
            ...         self.is_assembled = True
            ...         return True
            ...     def disassemble(self) -> bool: ...
            ...     def repaint(self, new_color: str) -> None: ...
            >>> chair = Chair("wood", (50, 50, 100), "brown")
            >>> chair.assemble()
            True
        """
        ...

    @abstractmethod
    def disassemble(self) -> bool:
        """
        Разобрать предмет мебели.

        Returns:
            bool: True если разборка успешна, False в противном случае

        Examples:
            >>> class Chair(Furniture):
            ...     def __init__(self, material: str, dimensions: tuple[float, float, float], color: str):
            ...         super().__init__(material, dimensions, color)
            ...         self.is_assembled = True
            ...     def assemble(self) -> bool: ...
            ...     def disassemble(self) -> bool:
            ...         self.is_assembled = False
            ...         return True
            ...     def repaint(self, new_color: str) -> None: ...
            >>> chair = Chair("wood", (50, 50, 100), "brown")
            >>> chair.disassemble()
            True
        """
        ...

    @abstractmethod
    def repaint(self, new_color: str) -> None:
        """
        Перекрасить предмет мебели.

        Args:
            new_color: Новый цвет

        Raises:
            ValueError: Если new_color - пустая строка

        Examples:
            >>> class Chair(Furniture):
            ...     def assemble(self) -> bool: ...
            ...     def disassemble(self) -> bool: ...
            ...     def repaint(self, new_color: str) -> None:
            ...         if not new_color or not new_color.strip():
            ...             raise ValueError("Цвет не может быть пустым")
            ...         self.color = new_color
            >>> chair = Chair("wood", (50, 50, 100), "brown")
            >>> chair.repaint("white")
            >>> chair.color
            'white'
        """
        ...


class SocialNetwork(ABC):
    """
    Абстрактный класс, описывающий социальную сеть.

    Attributes:
        name (str): Название социальной сети.
        active_users (int): Количество активных пользователей.
        max_storage_gb (float): Максимальный объём хранилища в ГБ.
    """

    def __init__(self, name: str, active_users: int, max_storage_gb: float) -> None:
        """
        Инициализация социальной сети.

        Args:
            name: Название социальной сети
            active_users: Количество активных пользователей
            max_storage_gb: Максимальный объём хранилища в ГБ

        Raises:
            ValueError: Если параметры не удовлетворяют ограничениям

        Examples:
            >>> network = SocialNetwork("MyNetwork", 1000, 500.5)  # doctest: +SKIP
            Traceback (most recent call last):
            ...
            TypeError: Can't instantiate abstract class SocialNetwork...

            >>> class MySocialNetwork(SocialNetwork):
            ...     def add_user(self, username: str) -> bool: ...
            ...     def remove_user(self, username: str) -> bool: ...
            ...     def calculate_storage_usage(self) -> float: ...
            >>> net = MySocialNetwork("MyNetwork", 1000, 500.5)
            >>> net.name
            'MyNetwork'
        """
        if not name or not name.strip():
            raise ValueError("Название не может быть пустым")
        if active_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        if max_storage_gb <= 0:
            raise ValueError("Объём хранилища должен быть положительным")

        self.name = name
        self.active_users = active_users
        self.max_storage_gb = max_storage_gb

    @abstractmethod
    def add_user(self, username: str) -> bool:
        """
        Добавить нового пользователя в социальную сеть.

        Args:
            username: Имя пользователя

        Returns:
            bool: True если пользователь успешно добавлен, False в противном случае

        Raises:
            ValueError: Если username - пустая строка

        Examples:
            >>> class MySocialNetwork(SocialNetwork):
            ...     def __init__(self, name: str, active_users: int, max_storage_gb: float):
            ...         super().__init__(name, active_users, max_storage_gb)
            ...         self.users = set()
            ...     def add_user(self, username: str) -> bool:
            ...         if not username or not username.strip():
            ...             raise ValueError("Имя пользователя не может быть пустым")
            ...         if username in self.users:
            ...             return False
            ...         self.users.add(username)
            ...         self.active_users += 1
            ...         return True
            ...     def remove_user(self, username: str) -> bool: ...
            ...     def calculate_storage_usage(self) -> float: ...
            >>> net = MySocialNetwork("MyNetwork", 0, 500.5)
            >>> net.add_user("john_doe")
            True
            >>> net.active_users
            1
        """
        ...

    @abstractmethod
    def remove_user(self, username: str) -> bool:
        """
        Удалить пользователя из социальной сети.

        Args:
            username: Имя пользователя для удаления

        Returns:
            bool: True если пользователь успешно удалён, False в противном случае

        Examples:
            >>> class MySocialNetwork(SocialNetwork):
            ...     def __init__(self, name: str, active_users: int, max_storage_gb: float):
            ...         super().__init__(name, active_users, max_storage_gb)
            ...         self.users = {"john_doe"}
            ...     def add_user(self, username: str) -> bool: ...
            ...     def remove_user(self, username: str) -> bool:
            ...         if username in self.users:
            ...             self.users.remove(username)
            ...             self.active_users = max(0, self.active_users - 1)
            ...             return True
            ...         return False
            ...     def calculate_storage_usage(self) -> float: ...
            >>> net = MySocialNetwork("MyNetwork", 1, 500.5)
            >>> net.remove_user("john_doe")
            True
            >>> net.active_users
            0
        """
        ...

    @abstractmethod
    def calculate_storage_usage(self) -> float:
        """
        Рассчитать текущее использование хранилища.

        Returns:
            float: Использованный объём хранилища в ГБ

        Examples:
            >>> class MySocialNetwork(SocialNetwork):
            ...     def __init__(self, name: str, active_users: int, max_storage_gb: float):
            ...         super().__init__(name, active_users, max_storage_gb)
            ...         self.storage_used = 50.5
            ...     def add_user(self, username: str) -> bool: ...
            ...     def remove_user(self, username: str) -> bool: ...
            ...     def calculate_storage_usage(self) -> float:
            ...         return self.storage_used
            >>> net = MySocialNetwork("MyNetwork", 1000, 500.5)
            >>> net.calculate_storage_usage()
            50.5
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
