import abc
from ex0.creature_factory import Creature
from ex1.creature_capability_factory import (
    HealCapability,
    TransformCapability,
)


class InvalidStrategyError(Exception):
    pass


# Abstract Battle Strategy
class BattleStrategy(abc.ABC):

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                "for this normal strategy"
            )

        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        else:
            return False


class AggressiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                "for this aggressive strategy"
            )

        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False


class DefensiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                "for this defensive strategy"
            )

        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False
