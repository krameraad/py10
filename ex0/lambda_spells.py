from data_generator import FuncMageDataGenerator

X = "\033[0m"     # Clear text formatting
H = "\033[1;93m"  # Header
D = "\033[2m"     # Dim


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    print(f"{H}\nSorting artifacts...{X}")
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def print_artifacts(artifacts: list[dict]) -> None:
    print(f"{D}\nPrinting artifacts...{X}")
    print(f"{"Name":<24} {"Power":>8} {"Type":>16}")
    print(D + "-" * 50 + X)
    for x in artifacts:
        print(f"{x["name"]:<24} {x["power"]:>8} {x["type"]:>16}")


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    print(f"{H}\nFiltering mages...{X}")
    return filter(lambda x: x["power"] >= min_power, mages)


def print_mages(mages: list[dict]) -> None:
    print(f"{D}\nPrinting mages...{X}")
    print(f"{"Name":<24} {"Power":>8} {"Element":>16}")
    print(D + "-" * 50 + X)
    for x in mages:
        print(f"{x["name"]:<24} {x["power"]:>8} {x["element"]:>16}")


def spell_transformer(spells: list[str]) -> list[str]:
    print(f"{H}\nTransforming spells...{X}")
    return map(lambda x: "* " + x + " *", spells)


def mage_stats(mages: list[dict]) -> dict:
    result: dict = {}
    result["max_power"] = max(mages, key=lambda x: x["power"])["power"]
    result["min_power"] = min(mages, key=lambda x: x["power"])["power"]
    result["avg_power"] = sum(map(lambda x: x["power"], mages)) / len(mages)
    return result


gen = FuncMageDataGenerator()
artifacts = gen.generate_artifacts()
print_artifacts(artifacts)
print_artifacts(artifact_sorter(artifacts))

mages = gen.generate_mages()
print_mages(mages)
print_mages(power_filter(mages, 70))

spells = gen.generate_spells()
print(f"{D}\nPrinting spells...{X}")
for x in spells:
    print(x)

spells = spell_transformer(spells)
print(f"{D}\nPrinting spells...{X}")
for x in spells:
    print(x)

stats = mage_stats(mages)
print(f"{D}\nPrinting mage stats...{X}")
print("Maximum power:", stats["max_power"])
print("Minimum power:", stats["min_power"])
print("Average power:", stats["avg_power"])
