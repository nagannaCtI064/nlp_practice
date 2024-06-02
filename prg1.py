def climbingLeaderboard(ranked, player):
    # Remove duplicates and keep the ranked list in descending order
    unique_ranked = sorted(set(ranked), reverse=True)
    
    results = []
    index = len(unique_ranked) - 1  # Start from the end of the unique ranked list
    print("Index",index)
    for score in player:
        # Move up the leaderboard until we find the correct position for the player's score
        while index >= 0 and score >= unique_ranked[index]:
            index -= 1
        # The player's rank is the index + 2 because we moved one step too far
        results.append(index + 2)
    
    return results

# Sample Input
ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]

# Get the player's rankings after each game
result = climbingLeaderboard(ranked, player)

# Print the results
for rank in result:
    print(rank)
