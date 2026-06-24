import ex0
import ex1
import ex2


def battle(opponents: list[tuple[ex0.CreatureFactory,
                                 ex2.BattleStrategy]]) -> None:

    print("*** Tournament ***")
    total_opponents = len(opponents)
    print(f"{total_opponents} opponents involved")
    for i in range(total_opponents):
        for j in range(i + 1, total_opponents):
            print("\n* Battle *")
            opponent1 = opponents[i][0].create_base()
            opponent2 = opponents[j][0].create_base()
            print(opponent1.describe())
            print(" vs.")
            print(opponent2.describe())
            print(" now fight!")
            opponent1_strategy = opponents[i][1]
            opponent2_strategy = opponents[j][1]
            try:
                opponent1_strategy.act(opponent1)
                opponent2_strategy.act(opponent2)
            except ex2.InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    factory_flame = ex0.FlameFactory()
    normal_strategy = ex2.NormalStrategy()
    factory_healing = ex1.HealingCreatureFactory()
    defensive_strategy = ex2.DefensiveStrategy()
    tournament0 = [(factory_flame, normal_strategy),
                   (factory_healing, defensive_strategy)]
    battle(tournament0)

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    factory_flame = ex0.FlameFactory()
    aggressive_strategy = ex2.AggressiveStrategy()
    factory_healing = ex1.HealingCreatureFactory()
    defensive_strategy = ex2.DefensiveStrategy()
    tournament1 = [(factory_flame, aggressive_strategy),
                   (factory_healing, defensive_strategy)]
    battle(tournament1)

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    factory_aqua = ex0.AquaFactory()
    normal_strategy = ex2.NormalStrategy()
    factory_healing = ex1.HealingCreatureFactory()
    defensive_strategy = ex2.DefensiveStrategy()
    factory_transform = ex1.TransformCreatureFactory()
    aggressive_strategy = ex2.AggressiveStrategy()
    tournament2 = [(factory_aqua, normal_strategy),
                   (factory_healing, defensive_strategy),
                   (factory_transform, aggressive_strategy)]
    battle(tournament2)


if __name__ == "__main__":
    main()
