import ex0
import ex1
import ex2


def battle(opponents: list[tuple[ex2.CreatureFactory,
                                 ex2.BattleStrategy]]) -> None:
    base_opponents = []
    for opponent in opponents:
        base_opponent = opponent[0].create_base()
        base_opponents.append(base_opponent)
        base_opponent.describe()


def main() -> None:

    print("Tournament 0 (basic)")
    factory_flame = ex0.FlameFactory()
    normal_strategy = ex2.NormalStrategy()
    factory_flame = ex0.FlameFactory()
    normal_strategy = ex2.NormalStrategy()
    tournament0 = [(factory_flame, normal_strategy),()]
    battle(factory_flame, normal_strategy)
    factory_heal = ex1.HealingCreatureFactory()
    base_heal = factory_heal.create_base()
    defensive_strategy = ex2.DefensiveStrategy()
    print(base_creature1.describe())
    print(base_creature1.attack())
    print(base_creature1.heal("itself"))
    print(" evolved:")
    evolved_creature1 = factoryHeal.create_evolved()
    print(evolved_creature1.describe())
    print(evolved_creature1.attack())
    print(evolved_creature1.heal("itself and others"))

    print("\nTesting Creature with healing capability")
    print(" base:")
    factoryTrans = ex1.TransformCreatureFactory()
    base_creature2 = factoryTrans.create_base()
    print(base_creature2.describe())
    print(base_creature2.attack())
    print(base_creature2.transform())
    print(base_creature2.attack())
    print(base_creature2.revert())
    print(" evolved:")
    evolved_creature2 = factoryTrans.create_evolved()
    print(evolved_creature2.describe())
    print(evolved_creature2.attack())
    print(evolved_creature2.transform())
    print(evolved_creature2.attack())
    print(evolved_creature2.revert())


if __name__ == "__main__":
    main()
