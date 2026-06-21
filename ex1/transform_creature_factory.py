import abc
from ex0.creature_factory import Creature, CreatureFactory


# Abstract Healing Capability
class HealCapability(abc.ABC):

    @abc.abstractmethod
    def heal(self, target: str) -> str:
        pass


class Sproutling(Creature, HealCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return (f"{self._name} uses Vine Whip!")

    def heal(self, target: str) -> str:
        return (f"{self._name} heals {target} for a small amount")


class Bloomelle(Creature, HealCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return (f"{self._name} uses Petal Dance!")

    def heal(self, target: str) -> str:
        return (f"{self._name} heals {target} for a large amount")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


# Abstract Transform Capability
class TransformCapability(abc.ABC):

    def __init__(self) -> None:
        self._state = "normal"

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._state == "normal":
            return (f"{self._name} attacks normally.")
        else:
            return (f"{self._name} performs a boosted strike!")

    def transform(self) -> str:
        if self._state == "normal":
            self._state = "sharper"
        return (f"{self._name} shifts into a sharper form!")

    def revert(self) -> str:
        if self._state == "sharper":
            self._state = "normal"
        return (f"{self._name} returns to normal.")


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._state == "normal":
            return (f"{self._name} attacks normally.")
        else:
            return (f"{self._name} unleashes a devastating morph strike!")

    def transform(self) -> str:
        if self._state == "normal":
            self._state = "dragonic battle"
        return (f"{self._name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        if self._state == "dragonic battle":
            self._state = "normal"
        return (f"{self._name} stabilizes its form.")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
