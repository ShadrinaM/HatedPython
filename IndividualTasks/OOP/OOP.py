# Класс «Волшебник» (Wizard)

# Экземпляр класса при инициализации принимает аргументы:
# – рейтинг;
# – на какой возраст выглядит.

# Класс должен обеспечивать функциональность:

# – change_rating(value) – изменять рейтинг на значение value; 
# не может стать больше 100 и меньше 1, изменяется только до достижения экстремального значения; 
# при увеличении рейтинга уменьшается возраст на abs(value)  // 10, 
# но только до 18, дальше не уменьшается; 
# при уменьшении рейтинга возраст соответственно увеличивается;

# – к экземпляру класса можно прибавить строку: (wd += string), значение рейтинга увеличивается 
# на ее длину, а возраст, соответственно, уменьшается на длину // 10, условия изменения такие же;

# – экземпляр класса можно вызвать с аргументом-числом; возвращает значение: 
# (аргумент - возраст) * рейтинг;

# – экземпляры класса можно сравнивать: сначала по рейтингу, затем по возрасту, 
# затем по имени по алфавиту; для этого нужно реализовать методы сравнения.

# Создать класс-наследник от класса «Волшебник», например, «Ледяной Волшебник». 

# Обязательно использование конструктора, декораторов и метода __str__.



class Wizard:
    def __init__(self, rating, age):
        if not (1 <= rating <= 100):
            raise ValueError("Рейтинг должен быть в диапазоне от 1 до 100.")
        if age < 18:
            raise ValueError("Возраст не может быть меньше 18 лет.")

        self.rating = rating
        self.age = age

    # декораторы, делают атрибуты только для чтения
    @property
    def rating(self):
        """Рейтинг волшебника (только для чтения)."""
        return self._rating

    @property
    def age(self):
        """Возраст волшебника (только для чтения)."""
        return self._age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError("Возраст не может быть меньше 18 лет.")
        self._age = value

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 100):
            raise ValueError("Рейтинг должен быть в диапазоне от 1 до 100.")
        self._rating = value

    # требуемый в задании метод
    def change_rating(self, value):
        """Изменяет рейтинг и корректирует возраст."""
        new_rating = self.rating + value

        if new_rating > 100:
            value = 100 - self.rating
        elif new_rating < 1:
            value = 1 - self.rating

        self.rating += value

        # Коррекция возраста
        age_change = abs(value) // 10
        if value > 0:  # Увеличение рейтинга
            self.age = max(18, self.age - age_change)
        elif value < 0:  # Уменьшение рейтинга
            self.age += age_change

    # оператор +=
    def __iadd__(self, string):
        """Увеличивает рейтинг на длину строки и уменьшает возраст."""
        if not isinstance(string, str):
            raise ValueError("Можно добавлять только строку.")

        length = len(string)
        self.change_rating(length)
        return self

    # вызов объекта как функции
    def __call__(self, number):
        """Вычисляет (аргумент - возраст) * рейтинг."""
        return (number - self.age) * self.rating

    # строковое представление объекта
    def __str__(self):
        """Строковое представление волшебника."""
        return f"Волшебник(rating={self.rating}, age={self.age})"

    # оператор ==
    def __eq__(self, other):   
        if not isinstance(other, Wizard):
            return NotImplemented
        return (self.rating, self.age) == (other.rating, other.age)
    # Если other не является экземпляром Wizard (или его наследника), метод возвращает NotImplemented

    # оператор < сравнения
    def __lt__(self, other):
        if not isinstance(other, Wizard):
            return NotImplemented
        if self.rating != other.rating:
            return self.rating < other.rating
        if self.age != other.age:
            return self.age < other.age
        return self.__class__.__name__ < other.__class__.__name__

# Наследник класса Wizard
class IceWizard(Wizard):
    def __init__(self, rating, age, ice):
        super().__init__(rating, age)
        self.ice = ice

    def __str__(self):
        return f"Ледяной волшебник(rating={self.rating}, age={self.age}, ice={self.ice})"

# Пример использования:
wizard = Wizard(50, 30)
print(wizard)  # Wizard(rating=50, age=30)

wizard.change_rating(10)
print(wizard)  # Wizard(rating=60, age=29)

wizard += "magic"
print(wizard)  # Wizard(rating=65, age=28)

print(wizard(100))  # (100 - 28) * 65

ice_wizard = IceWizard(40, 25, 300)
print(ice_wizard)  # IceWizard(rating=40, age=25, ice_power=300)

print(wizard < ice_wizard)  # Сравнение по рейтингу, возрасту, имени
