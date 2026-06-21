import ex0
import ex1
import ex2


def battle(opponents: list[tuple[ex2.CreatureFactory,
                                 ex2.BattleStrategy]]) -> None:

    for i in range(len(opponents)):
      for j in range(i + 1, len(opponents)):
        opponent1 = opponents[i][0].create_base()
        opponent2 = opponents[j][0].create_base()
        opponent1.describe()
        opponent2.describe()
        opponent1_strategy = opponents[i][1]
        opponent2_strategy = opponents[j][1]


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
