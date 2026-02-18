import random
import time


def event_generator(count):
    """Generates a stream of random game events one by one."""
    actions = ["killed monster", "found treasure", "leveled up"]
    players = ["alice", "bob", "charlie", "david", "eve"]
    print(f"Processing {count} game events...\n")
    for i in range(1, count + 1):
        player = random.choice(players)
        level = random.randint(1, 20)
        action = random.choice(actions)
        yield {"id": i, "player": player, "level": level, "action": action}


def fibonacci_gen(n):
    """Generates the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n):
    """Generates the first n prime numbers."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    count, num = 0, 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


if (__name__ == "__main__"):
    nb = 1000
    nb_fibo = 10
    nb_prime = 5
    fibo_lst = []
    first = True
    high_level_count = 0
    treasure_events = 0
    levelup_events = 0
    print("=== Game Data Stream Processor ===")
    start_time = time.time()
    stream = event_generator(nb)
    for event in event_generator(nb):
        if event["id"] <= 3:
            print(f"Event {event['id']}: Player {event['player']} (level \
{event['level']}) {event['action']}")
        if event["id"] == 4:
            print("...")
        if event["level"] >= 10:
            high_level_count += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            levelup_events += 1
    end_time = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {nb}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")
    print("\n=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first {nb_fibo}):", end=" ")
    fibo = fibonacci_gen(nb_fibo)
    for e in fibo:
        if not first:
            print(", ", end="")
        print(e, end="")
        first = False
    print()
    print(f"Prime numbers (first {nb_prime}): ", end=" ")
    prime = prime_gen(nb_prime)
    first = True
    for e in prime:
        if not first:
            print(", ", end="")
        print(e, end="")
        first = False
    print()
