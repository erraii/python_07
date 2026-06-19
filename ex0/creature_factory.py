import abc


# Abstract Creatures
class Creature(abc.ABC):

    def __init__(self) -> None:
        self._name = ""
        self._type = ""

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self._name} is a {self._type} type Creature")


class Flameling(Creature):

    def __init__(self) -> None:
        self._name = "Flameling"
        self._type = "Fire"

    def attack(self) -> str:
        return (f"{self._name} uses Ember!")


class Pyrodon(Creature):

    def __init__(self) -> None:
        self._name = "Pyrodon"
        self._type = "Fire/Flying"

    def attack(self) -> str:
        return (f"{self._name} uses Flamethrower!")


class Aquabub(Creature):

    def __init__(self) -> None:
        self._name = "Aquabub"
        self._type = "Water"

    def attack(self) -> str:
        return (f"{self._name} uses Water Gun!")


class Torragon(Creature):

    def __init__(self) -> None:
        self._name = "Torragon"
        self._type = "Water"

    def attack(self) -> str:
        return (f"{self._name} uses Hydro Pump!")


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
