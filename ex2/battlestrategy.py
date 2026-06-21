import abc
from ex0.creature_factory import (
    Creature,
    CreatureFactory,
)
from ex1.transform_creature_factory import (
    HealCapability,
    TransformCapability,
)


# Abstract Battle Strategy
class BattleStrategy(abc.ABC):

    @abc.abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return creature.attack()
        else:
            raise Exception("Invalid Strategy-Creature combination!")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        else:
            return False


class AggressiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return capability.attack()
        else:
            raise Exception("Invalid Strategy-Creature combination!")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False


class DefensiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> str:
        if self.is_valid(capability):
            return capability.attack()
        else:
            raise Exception("Invalid Strategy-Creature combination!")

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature: Creature):
            return True
        else:
            return False
