from typing import Callable

X = "\033[0m"     # Clear text formatting
H = "\033[1;93m"  # Header
D = "\033[2m"     # Dim


def spell_combiner(
        spell1: Callable[[str], int],
        spell2: Callable[[str], int]
        ) -> Callable[[str], int]:
    print(f"{D}\nCombining spells...{X}")

    def combined_spell(target: str) -> str:
        result = spell1(target)
        print("and ", end="")
        return result + spell2(target)
    return combined_spell


def power_amplifier(
        base_spell: Callable[[str], int],
        multiplier: int
        ) -> Callable[[str], int]:
    print(f"{D}\nAmplifiying spell...{X}")

    def amplified_spell(target: str) -> int:
        return base_spell(target) * multiplier
    return amplified_spell


def conditional_caster(
        condition: Callable[[str], bool],
        spell: Callable[[str], int]
        ) -> Callable[[str], int | str]:
    print(f"{D}\nMaking spell conditional...{X}")

    def conditional_spell(target: str) -> int | str:
        if not condition(target):
            return "Spell fizzled"
        return spell(target)
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    print(f"{D}\nChaining spells...{X}")

    def sequential_spells(target: str) -> list[int | str]:
        result = []
        for spell in spells:
            result += [spell(target)]
        return result
    return sequential_spells


def fireball(target: str) -> int:
    print(f"Fireball hits {target}")
    return 10


def heal(target: str) -> int:
    print(f"Heal soothes {target}")
    return 5


def is_dragon(target: str) -> bool:
    return target.lower() == "dragon"


print(f"{D}\nBasic spells...{X}")
fireball("Dragon")
heal("Dragon")

combined_spell = spell_combiner(fireball, heal)
combined_spell("Dragon")

print(f"{D}\nBasic spell effect...{X}")
print("Original:", fireball("Goblin"))
amplified_spell = power_amplifier(fireball, 3)
print("Amplified:", amplified_spell("Goblin"))

conditional_spell = conditional_caster(is_dragon, fireball)
print(f"{H}Target: Dragon{X}")
print(f"Result: {conditional_spell("Dragon")}")
print(f"{H}Target: Goblin{X}")
print(f"Result: {conditional_spell("Goblin")}")

spellchain = spell_sequence([
    fireball,
    heal,
    combined_spell,
    amplified_spell,
    conditional_spell
])

result = spellchain("Dragon")
print(f"{H}Result: {result}")
print(X)
result = spellchain("Goblin")
print(f"{H}Result: {result}")
print(X)
