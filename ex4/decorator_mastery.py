import random
from functools import wraps
from time import perf_counter, sleep
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

X = "\033[0m"     # Clear text formatting
H = "\033[1;93m"  # Header
D = "\033[2m"     # Dim


def spell_timer(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Callable[P, R]:
        print(f"Casting {func.__name__}...")
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[P, R]:
    def wrapper_factory(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs):
            if args[2] < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return wrapper_factory


def retry_spell(max_attempts: int) -> Callable[P, R]:
    def wrapper_factory(func) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except RuntimeError:
                    attempts += 1
                    print("Spell failed, retrying... "
                          f"(attempt {attempts}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return wrapper_factory


@spell_timer
@retry_spell(5)
def fireball(power: int) -> str:
    if random.randint(0, 2):
        raise RuntimeError("Failed to cast fireball")
    sleep(random.uniform(0.125, 0.5))
    return f"Fireball cast with {power} power"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


print(f"\n{D}Testing spell timer...{X}")
print(fireball(5) + "\n")
print(fireball(10) + "\n")
print(fireball(15) + "\n")


print(f"\n{D}Testing mage name validation...{X}")
name = "Alice"
print(f"{name:<20} {str(MageGuild.validate_mage_name(name)):>5}")
name = "Bob Bobbinson"
print(f"{name:<20} {str(MageGuild.validate_mage_name(name)):>5}")
name = "???"
print(f"{name:<20} {str(MageGuild.validate_mage_name(name)):>5}")
name = "Me"
print(f"{name:<20} {str(MageGuild.validate_mage_name(name)):>5}")


print(f"\n{D}Testing mage guild spells...{X}")
guild = MageGuild()
print(guild.cast_spell("Lightning", 5))
print(guild.cast_spell("Lightning", 15))
