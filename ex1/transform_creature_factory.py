import abc
from ex0.creature_factory import Creature
from ex0.creature_factory import CreatureFactory


# Abstract Healing Capability
class HealCapability(abc.ABC):

    @abc.abstractmethod
    def heal(self, target: str) -> str:
        pass


class Sproutling(Creature, HealCapability):

    def __init__(self) -> None:
        self._name = "Sproutling"
        self._type = "Grass"

    def attack(self) -> str:
        return (f"{self._name} uses Vine Whip!")

    def heal(self, target: str) -> str:
        return (f"{self._name} heals {target} for a small amount")


class Bloomelle(Creature, HealCapability):

    def __init__(self) -> None:
        self._name = "Bloomelle"
        self._type = "Grass/Fairy"

    def attack(self) -> str:
        return (f"{self._name} uses Petal Dance!")

    def heal(self, target: str) -> str:
        return (f"{self._name} heals {target} for a large amount")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


# Abstract Transform Capability
class TransformCapability(abc.ABC):

    def __init__(self) -> None:
        self._state = "base"

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        self._name = "Flameling"
        self._type = "Fire"

    def attack(self) -> str:
        return (f"{self._name} uses Ember!")


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        self._name = "Pyrodon"
        self._type = "Fire/Flying"

    def attack(self) -> str:
        return (f"{self._name} uses Flamethrower!")


class TransformCreatureFactory(CreatureFactory):
    @abc.abstractmethod
    def create_base(self) -> Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        pass
