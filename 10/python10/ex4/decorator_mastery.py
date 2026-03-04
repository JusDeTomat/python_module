import functools
import time


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(nb1: int, nb2: int) -> any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(nb1, nb2)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.4f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                power = args[-1]
            if int(power) >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(max_time) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func()
                except Exception:
                    print(f"Spell failed, retrying... \
                          ({attempt}/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main():
    print("Testing spell timer")

    @spell_timer
    def long_thing(nb1: int, nb2: int) -> int:
        total = 0
        for i in range(1, 10_000_000):
            total += (i * nb1) % (nb2 + 1)
        return total
    print(f"Result: {long_thing(2, 3)}")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Albus Dumbledore"))
    print(MageGuild.validate_mage_name("R2-D2"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Ice", 5))


if (__name__ == "__main__"):
    main()
