def player(prev_play, opponent_history=[]):
    # Append the previous play to history only if it's not an empty string
    if prev_play:
        opponent_history.append(prev_play)

    # Initialize strategies and counters
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    if len(opponent_history) == 0:
        return "R"  # Default move for the first round

    # Analyze the opponent's most frequent move in history
    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        move_counts[move] += 1
    most_frequent_move = max(move_counts, key=move_counts.get)
    # Predict the opponent's next move based on patterns
    # For Abbey bot, use a pattern-based strategy
    if len(opponent_history) > 1:
        last_two = "".join(opponent_history[-2:])
        pattern_counts = {"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0}
        for i in range(len(opponent_history) - 1):
            pattern = "".join(opponent_history[i:i + 2])
            if pattern in pattern_counts:
                pattern_counts[pattern] += 1

        # Predict the next move based on the most frequent two-pattern
        if last_two in pattern_counts:
            predicted_next = max(
                {k: v for k, v in pattern_counts.items() if k.startswith(last_two[1])},
                key=pattern_counts.get,
                default="R",
            )[-1]
        else:
            predicted_next = most_frequent_move

        # Counter the predicted move
        guess = counter_moves[predicted_next]
    else:
        # Use frequency-based strategy initially
        guess = counter_moves[most_frequent_move]

    return guess