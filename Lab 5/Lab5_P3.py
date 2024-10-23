# Chess Move Validator for the King
def I_Love_VinUni(start, end):
    # Convert columns from letters to numbers (a-h to 1-8)
    start_col = ord(start[0]) - ord('a') + 1
    start_row = int(start[1])
    
    end_col = ord(end[0]) - ord('a') + 1
    end_row = int(end[1])
    
    # Calculate the difference in rows and columns
    col_diff = abs(end_col - start_col)
    row_diff = abs(end_row - start_row)
    
    # The King can move one square in any direction
    return (col_diff <= 1 and row_diff <= 1) and (col_diff + row_diff > 0)

# Input
start = input()
end = input()

# Print result
print(I_Love_VinUni(start, end))