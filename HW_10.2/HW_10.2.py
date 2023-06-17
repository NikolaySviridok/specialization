# Задание 2
# Возьмите 1-3 любые задачи из прошлых семинаров 
# (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в 
# свойства. Задачи должны решаться через вызов методов 
# экземпляра.

from HW_10_2_1 import Mammal, Bird, Fish, Animal


class AnimalFabric:
    _tmp_parameters = {}

    @classmethod
    def build(cls, animal_type: str,
              name: str, age: int,
              color: str = None,
              voice: str = None,
              hair: str = None,
              ) -> Animal:
        cls._tmp_parameters = dict(name=name, age=age,
                                   color=color,
                                   voice=voice,
                                   hair=hair)
        return cls._choice(animal_type)

    @classmethod
    def _choice(cls, animal_type):
        match animal_type:
            case 'Mammal':
                return cls._create_mammal(**cls._tmp_parameters)
            case 'Bird':
                return cls._create_bird(**cls._tmp_parameters)
            case 'Fish':
                return cls._create_fish(**cls._tmp_parameters)
            case _:
                return Animal('Cadaver', 1000)

    @classmethod
    def _create_mammal(cls, name, age, voice, hair, **_) -> Mammal:
        return Mammal(name=name, age=age, voice=voice, hair=hair, )

    @classmethod
    def _create_bird(cls, name, age, color, voice, **_) -> Bird:
        return Bird(name=name, age=age, color=color, voice=voice)

    @classmethod
    def _create_fish(cls, name, age, color, **_) -> Fish:
        return Fish(name=name, age=age, color=color)


def main():
    dog = AnimalFabric.build(animal_type='Mammal', name='Fido', age=5, voice='Woof!', hair='Pale, long')
    fish = AnimalFabric.build(animal_type='Fish', name='Vanda', age=1, color='Rainbow')
    bird = AnimalFabric.build(animal_type='Bird', name='Carl', age=8, color='Black', voice='CRAW!')
    unidentified = AnimalFabric.build(animal_type='Non-type', name='Fail-Tester',
                                      age=100, color='Green', voice='Boo', hair='blonde')
    print(dog.get_info(), '\n')
    print(fish.get_info(), '\n')
    print(bird.get_info(), '\n')
    print(unidentified.get_info())


if __name__ == '__main__':
    main()