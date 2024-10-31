def count_valleys(steps):
    level = 0  # Current level relative to sea level
    valleys = 0  # Count of valleys
    in_valley = False  # Flag to indicate if we are in a valley

    for step in steps:
        # Update the current level
        if step == 'U':
            level += 1
        elif step == 'D':
            level -= 1
        
        # Check if we are entering a valley
        if level < 0 and not in_valley:
            in_valley = True
        
        # Check if we are exiting a valley
        if level == 0 and in_valley:
            valleys += 1
            in_valley = False

    return valleys

# Input from the user
path = input()
print(count_valleys(path))