import random

def play(p1, p2, num_games, verbose=False):
    """
    Play a match between two players
    p1, p2: player functions
    num_games: number of games to play
    verbose: print each game result
    """
    p1_wins = 0
    p2_wins = 0
    p1_prev = ""
    p2_prev = ""
    
    for _ in range(num_games):
        p1_move = p1(p2_prev)
        p2_move = p2(p1_prev)
        
        p1_prev = p1_move
        p2_prev = p2_move
        
        if p1_move == p2_move:
            result = "tie"
        elif (p1_move == "R" and p2_move == "S") or \
             (p1_move == "S" and p2_move == "P") or \
             (p1_move == "P" and p2_move == "R"):
            p1_wins += 1
            result = "p1"
        else:
            p2_wins += 1
            result = "p2"
        
        if verbose:
            print(f"Player 1: {p1_move}  Player 2: {p2_move}  Result: {result}")
    
    print(f"\nResults: Player 1 wins: {p1_wins}, Player 2 wins: {p2_wins}")
    print(f"Player 1 win rate: {p1_wins / num_games * 100:.1f}%")
    return p1_wins, p2_wins


def quincy(prev_play):
    """Bot that plays: R, P, S, R, P, S pattern"""
    if prev_play == "":
        return "R"
    
    quincy_plays = ["R", "P", "S"]
    if not hasattr(quincy, "counter"):
        quincy.counter = 0
    
    quincy.counter = (quincy.counter + 1) % 3
    return quincy_plays[quincy.counter]


def abbey(prev_play):
    """Bot that counts opponent moves and plays counter"""
    if prev_play == "":
        return "R"
    
    if not hasattr(abbey, "play_count"):
        abbey.play_count = {"R": 0, "P": 0, "S": 0}
    
    abbey.play_count[prev_play] += 1
    
    most_frequent = max(abbey.play_count, key=abbey.play_count.get)
    
    if most_frequent == "R":
        return "P"
    elif most_frequent == "P":
        return "S"
    else:
        return "R"


def kris(prev_play):
    """Bot that plays opposite of what you played last time"""
    if prev_play == "":
        return "R"
    
    if prev_play == "R":
        return "P"
    elif prev_play == "P":
        return "S"
    else:
        return "R"


def mrugby(prev_play):
    """Bot that plays randomly"""
    return random.choice(["R", "P", "S"])
