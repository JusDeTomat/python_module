def check_temperature(temp_str: str) -> int:
    """Verify if the input temperature is a valid number and safe
    for plant grow."""
    try:
        print(f"Testing temperature: {temp_str}")
        temp_str = int(temp_str)
        if (40 < temp_str):
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        elif (0 > temp_str):
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!")
            return temp_str
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")
        return -1


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    check_temperature("25")
    print()
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


if (__name__ == "__main__"):
    main()
