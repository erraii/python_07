import ex0


def verify_creature(factory: ex0.CreatureFactory) -> None:
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def fight_creature(factory1: ex0.CreatureFactory,
                   factory2: ex0.CreatureFactory) -> None:
    base_creature1 = factory1.create_base()
    base_creature2 = factory2.create_base()

    print(base_creature1.describe())
    print(" vs.")
    print(base_creature2.describe())

    print(" fight!")
    print(base_creature1.attack())
    print(base_creature2.attack())


def main() -> None:
    print("Testing factory")
    verify_creature(ex0.FlameFactory())

    print("\nTesting factory")
    verify_creature(ex0.AquaFactory())

    print("\nTesting battle")
    fight_creature(ex0.FlameFactory(), ex0.AquaFactory())


if __name__ == "__main__":
    main()
