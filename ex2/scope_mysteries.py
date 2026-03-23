from typing import Any, Callable

X = "\033[0m"     # Clear text formatting
H = "\033[1;93m"  # Header
D = "\033[2m"     # Dim


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], None]:
    power = initial_power

    def accumulator(added_power: int):
        nonlocal power
        power += added_power
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(name: str) -> str:
        return enchantment_type + " " + name
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        print(f"Storing '{value}' in '{key}'")
        memory[key] = value

    def recall(key: str) -> Any:
        print(f"Recalling from '{key}'", end=": ")
        return memory[key]

    return {"store": store, "recall": recall}


print(f"\n{D}Testing mage counter...{X}")
counter = mage_counter()
print("Call 1:", counter())
print("Call 2:", counter())
print("Call 3:", counter())

print(f"\n{D}Testing accumulator...{X}")
accumulator = spell_accumulator(5)
print("Add 2 :", accumulator(2))
print("Add 10:", accumulator(10))
print("Add 3 :", accumulator(3))

print(f"\n{D}Testing enchantment factory...{X}")
enchant_flaming = enchantment_factory("Flaming")
print(enchant_flaming("Sword"))
enchant_frozen = enchantment_factory("Frozen")
print(enchant_frozen("Shield"))
print(enchant_flaming("Whip"))

print(f"\n{D}Testing memory vault...{X}")
vault = memory_vault()
vault["store"]("kaas", 10)
vault["store"]("worm", 5)
print(vault["recall"]("kaas"))
print(vault["recall"]("worm"))
