def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem.
    
    Parameters:
    n (int): Number of disks
    source (str): The source tower
    target (str): The target tower
    auxiliary (str): The auxiliary tower
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary, using target as auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move the n-1 disks from auxiliary to target, using source as auxiliary
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example usage:
num_disks = int(input("Number of disks: "))  # Change this value for more or fewer disks
tower_of_hanoi(num_disks, 'Left', 'Right', 'Middle')