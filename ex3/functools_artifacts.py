from functools import reduce, partial, lru_cache, singledispatch
from time import perf_counter
from operator import add, mul
from typing import Callable

X = "\033[0m"     # Clear text formatting
H = "\033[1;93m"  # Header
D = "\033[2m"     # Dim


def spell_reducer(spells: list[int], operation: str) -> int:
    STR_TO_OP = {
        "add": add,
        "mul": mul,
        "max": max,
        "min": min,
    }
    op = STR_TO_OP[operation]
    return reduce(op, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    result = {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }
    return result


def enchant(power: int, element: str, target: str) -> None:
    print(f"Adding {power} {element} power to {target}")


@lru_cache
def memoized_fibonacci(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(spell) -> str:
        return f"Unknown spell type ('{spell}')"

    @cast.register
    def _(spell: int) -> str:
        return f"Spell deals {spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"Spell applies enchantment '{spell}'"

    @cast.register
    def _(spell: list) -> str:
        return f"Spell multi-casts everything from {spell}"

    return cast


print(f"\n{D}Testing spell reducer...{X}")
print("Input:", [2, 3, 5, 10])
print(f"Sum:        {spell_reducer([2, 3, 5, 10], "add"):>8}")
print(f"Product:    {spell_reducer([2, 3, 5, 10], "mul"):>8}")
print(f"Maximum:    {spell_reducer([2, 3, 5, 10], "max"):>8}")
print(f"Minimum:    {spell_reducer([2, 3, 5, 10], "min"):>8}")


print(f"\n{D}Testing partial enchanter...{X}")
enchant(25, "physical", "Great Sword")
enchants = partial_enchanter(enchant)
enchants["fire_enchant"]("Flail")
enchants["ice_enchant"]("Helmet")
enchants["lightning_enchant"]("Spear")

print(f"\n{D}Testing memoized fibonacci...{X}")
print("100000 numbers, performance in seconds")
print(f"\n{H}First fibonacci call:{X}")
start = perf_counter()
memoized_fibonacci(100000)
end = perf_counter()
print(f"{end - start:.10f}")

print(f"\n{H}Second fibonacci call:{X}")
start = perf_counter()
memoized_fibonacci(100000)
end = perf_counter()
print(f"{end - start:.10f}")

print(f"\n{D}Testing spell dispatch...{X}")
print(spell_dispatcher()(40))
print(spell_dispatcher()("Flaming"))
print(spell_dispatcher()(["Fireball", "Heal", "Petrify"]))
print(spell_dispatcher()(12.5))
