# Function to print alphabet rangoli of a given size
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

    lines = []  # List to store each line of the rangoli

    for i in range(size):
        # Get the left half characters (from current letter to 'a')
        left = [alpha[size - j - 1] for j in range(i + 1)]
        
        # Create the right half by reversing left (excluding the center)
        right = left[:-1][::-1]
        
        # Combine both halves with '-' in between
        line = '-'.join(left + right)
        
        # Center the line to match the width of the final rangoli
        # Width = 4*size - 3 (to align properly with hyphens)
        lines.append(line.center(4 * size - 3, '-'))

    # Print the full rangoli:
    # Top + Middle part (stored in lines)
    # Bottom part (reverse of lines excluding the middle)
    print('\n'.join(lines + lines[-2::-1]))


# Code entry point: this block runs only if the file is executed directly
if __name__ == "__main__":
    # Take size input from user
    n = int(input("Enter size of rangoli (1–26): "))
    
    # Validate the size
    if 1 <= n <= 26:
        print_rangoli(n)  # Call the rangoli function
    else:
        print("Please enter a number between 1 and 26.")
