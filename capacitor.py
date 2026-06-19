import ex1


def main() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    factory = ex1.HealingCreatureFactory()
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal("itself"))
    print(" evolved:")
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal("itself and others"))


if __name__ == "__main__":
    main()
