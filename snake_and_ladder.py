import random
import time


SNAKES = {
    16: 6,
    46: 25,
    49: 11,
    62: 19,
    64: 60,
    74: 53,
    89: 68,
    92: 88,
    95: 75,
    99: 80,
}

LADDERS = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    78: 98,
    87: 94,
}


def roll_dice():
    return random.randint(1, 6)


def apply_snakes_ladders(pos):
    if pos in LADDERS:
        return LADDERS[pos], "ladder"
    if pos in SNAKES:
        return SNAKES[pos], "snake"
    return pos, None


def pretty_positions(players, positions):
    s = []
    for name, pos in zip(players, positions):
        s.append(f"{name}: {pos}")
    return " | ".join(s)


def play_game():
    print("Welcome to Snake & Ladder (CLI)")
    while True:
        try:
            n = int(input("Number of players (1-4): ").strip())
            if 1 <= n <= 4:
                break
        except Exception:
            pass
        print("Please enter a number between 1 and 4.")

    players = []
    is_computer = []
    for i in range(n):
        name = input(f"Enter name for player {i+1} (leave empty for Computer): ").strip()
        if not name:
            name = f"Computer{i+1}"
            is_computer.append(True)
        else:
            is_computer.append(False)
        players.append(name)

    positions = [0] * n
    turn = 0
    winner = None

    print("Game start! Reach exactly 100 to win.")
    print(pretty_positions(players, positions))

    while True:
        name = players[turn]
        pc = is_computer[turn]

        if pc:
            print(f"{name} (computer) is rolling...")
            time.sleep(0.8)
            rolled = roll_dice()
        else:
            cmd = input(f"{name}'s turn — press Enter to roll (or 'q' to quit): ")
            if cmd.strip().lower() == 'q':
                print("Game ended by user.")
                return
            rolled = roll_dice()

        print(f"{name} rolled a {rolled}.")

        new_pos = positions[turn] + rolled
        if new_pos > 100:
            print(f"Roll exceeds 100 (at {positions[turn]}). Need exact roll.")
        else:
            positions[turn] = new_pos
            # check snakes or ladders
            final_pos, effect = apply_snakes_ladders(positions[turn])
            if effect == 'ladder':
                print(f"Yay! {name} climbed a ladder from {positions[turn]} to {final_pos}.")
                positions[turn] = final_pos
            elif effect == 'snake':
                print(f"Oh no! {name} got bitten by a snake from {positions[turn]} to {final_pos}.")
                positions[turn] = final_pos

        print(pretty_positions(players, positions))

        if positions[turn] == 100:
            winner = name
            print(f"\n{winner} wins! Congratulations!")
            break

        turn = (turn + 1) % n


if __name__ == '__main__':
    play_game()
