def convert_input(player_string):
    """Convert the initial input string into a nested list of players and their scores."""
    players = []
    for entry in player_string.split(','):
        name, score = entry.strip().rsplit(' ', 1)  # Split on the last space
        players.append([name, int(score)])  # Append as [PlayerName, Score]
    return players

def perform_operations(players, operations):
    """Perform operations on the player list."""
    for operation in operations.split(','):
        parts = operation.strip().split()
        command = parts[0]

        if command == 'insert':
            # Insert a new player
            name = parts[1]
            score = int(parts[2])
            players.append([name, score])
        
        elif command == 'remove':
            # Remove a player
            name = parts[1]
            players = [player for player in players if player[0] != name]
        
        elif command == 'adjust':
            # Adjust a player's score
            name = parts[1]
            score_change = int(parts[2])
            for player in players:
                if player[0] == name:
                    player[1] += score_change  # Adjust the score
                    break

    return players

def sort_players(players):
    """Sort the list of players by score (descending) and then by name (alphabetically)."""
    return sorted(players, key=lambda x: (-x[1], x[0]))

# Input from the user
player_list_input = input("")
operation_list_input = input("")

# Convert input to nested list
players = convert_input(player_list_input)

# Perform operations on the player list
players_after_operations = perform_operations(players, operation_list_input)

# Sort the final list of players
sorted_players = sort_players(players_after_operations)

# Print sorted player names in one line
print(" ".join(player[0] for player in sorted_players))