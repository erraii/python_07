import ex1


def main() -> None:

    print("Testing Creature with healing capability")
    print(" base:")
    factory_heal = ex1.HealingCreatureFactory()
    base_creature1 = factory_heal.create_base()
    print(base_creature1.describe())
    print(base_creature1.attack())
    print(base_creature1.heal())
    print(" evolved:")
    evolved_creature1 = factory_heal.create_evolved()
    print(evolved_creature1.describe())
    print(evolved_creature1.attack())
    print(evolved_creature1.heal("itself and others"))

    print("\nTesting Creature with transform capability")
    print(" base:")
    factory_trans = ex1.TransformCreatureFactory()
    base_creature2 = factory_trans.create_base()
    print(base_creature2.describe())
    print(base_creature2.attack())
    print(base_creature2.transform())
    print(base_creature2.attack())
    print(base_creature2.revert())
    print(" evolved:")
    evolved_creature2 = factory_trans.create_evolved()
    print(evolved_creature2.describe())
    print(evolved_creature2.attack())
    print(evolved_creature2.transform())
    print(evolved_creature2.attack())
    print(evolved_creature2.revert())


if __name__ == "__main__":
    main()
