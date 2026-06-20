import ex1


def main() -> None:

    print("Testing Creature with healing capability")
    print(" base:")
    factoryHeal = ex1.HealingCreatureFactory()
    base_creature1 = factoryHeal.create_base()
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
