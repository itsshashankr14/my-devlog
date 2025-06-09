def merge_the_tools(string, k):
    # Step 1: Divide the string into parts of size 'k'
    for i in range(0, len(string), k):
        part = string[i:i+k]  # Get the substring of length 'k'
        
        # Step 2: Remove duplicate characters while preserving order
        seen = set()
        result = ''
        for char in part:
            if char not in seen:
                seen.add(char)       # Mark the character as seen
                result += char       # Append to the result only if not already seen

        # Step 3: Print the result for this part
        print(result)


# Main logic to take input and call the function
if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)
