import random
import time


def waiting_game():
    num = random.randint(3, 5)
    print(f"Timer runs out in {num} secs")
    input(f"Press Enter to start")
    start = time.perf_counter()
    input(f"Press Enter in {num} secs")
    elapsed = time.perf_counter() - start
    print(f"Elapsed time: {elapsed} secs")
    if elapsed == num:
        print("Unbelievable! Perfect Timing")
    elif elapsed < num:
        print(f"{num - elapsed} seconds fast")
    else:
        print(f"{elapsed - num} seconds slow")


waiting_game()
