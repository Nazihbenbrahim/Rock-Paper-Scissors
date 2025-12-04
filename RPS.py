def player(prev_play, opponent_history=[]):
    """
    AI player for Rock Paper Scissors that learns opponent patterns
    and adapts strategy to win at least 60% of games against each bot.
    """
    
    # Append the previous play to history
    if prev_play:
        opponent_history.append(prev_play)
    
    # On first move, start with rock
    if not opponent_history:
        return "R"
    
    # Define counter moves
    def counter(move):
        if move == "R":
            return "P"  # Paper beats Rock
        elif move == "P":
            return "S"  # Scissors beats Paper
        elif move == "S":
            return "R"  # Rock beats Scissors
        return "R"
    
    # Strategy 1: Detect if opponent always plays the same move
    if len(set(opponent_history)) == 1:
        return counter(opponent_history[-1])
    
    # Strategy 2: Detect patterns in recent moves (look for repeating sequences)
    if len(opponent_history) >= 4:
        # Check for 2-move pattern
        if opponent_history[-2] == opponent_history[-4] and opponent_history[-1] == opponent_history[-3]:
            return counter(opponent_history[-1])
        
        # Check for 3-move pattern
        if len(opponent_history) >= 6:
            if (opponent_history[-3] == opponent_history[-6] and 
                opponent_history[-2] == opponent_history[-5] and 
                opponent_history[-1] == opponent_history[-4]):
                return counter(opponent_history[-1])
    
    # Strategy 3: Most common move in recent history (last 10 games)
    recent_moves = opponent_history[-10:] if len(opponent_history) >= 10 else opponent_history
    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in recent_moves:
        if move in move_counts:
            move_counts[move] += 1
    
    # Counter the most frequent move
    most_common = max(move_counts, key=move_counts.get)
    if move_counts[most_common] > 0:
        return counter(most_common)
    
    # Strategy 4: Counter the immediate last move
    return counter(opponent_history[-1])


