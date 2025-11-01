def find_min_operations(n, shuffled, original):
    """
    Find minimum cut-and-insert operations to transform shuffled to original.
    
    Key insight: Elements that don't need to move form the Longest Increasing 
    Subsequence (LIS) when mapped to their target positions. For elements NOT 
    in the LIS, we can only move them together if they are:
    1. Contiguous in the shuffled list
    2. Contiguous in their target positions
    """
    
    # Create a mapping of instruction to its position in original list
    original_pos = {instr: i for i, instr in enumerate(original)}
    
    # Map shuffled instructions to their target positions
    target_positions = [original_pos[instr] for instr in shuffled]
    
    # Dynamic programming to find LIS lengths
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if target_positions[j] < target_positions[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
    
    max_lis_length = max(dp) if dp else 0
    
    # Find the ending index of an LIS with maximum length
    max_idx = -1
    for i in range(n):
        if dp[i] == max_lis_length:
            max_idx = i
            break
    
    # Reconstruct the LIS by following parent pointers
    lis_indices = set()
    idx = max_idx
    while idx != -1:
        lis_indices.add(idx)
        idx = parent[idx]
    
    # Collect elements not in LIS with their target positions
    elements_to_move = []
    for i in range(n):
        if i not in lis_indices:
            elements_to_move.append((i, target_positions[i]))
    
    if not elements_to_move:
        return 0
    
    # Sort by target position to group contiguous target positions
    elements_to_move.sort(key=lambda x: x[1])
    
    # Count groups: elements can be moved together only if they are
    # contiguous in BOTH shuffled list AND target positions
    operations = 0
    i = 0
    
    while i < len(elements_to_move):
        # Start a new group
        operations += 1
        current_shuffled_idx = elements_to_move[i][0]
        current_target_pos = elements_to_move[i][1]
        j = i + 1
        
        # Try to extend the group
        while j < len(elements_to_move):
            next_shuffled_idx = elements_to_move[j][0]
            next_target_pos = elements_to_move[j][1]
            
            # Can extend if both shuffled indices and target positions are consecutive
            if (next_shuffled_idx == current_shuffled_idx + 1 and 
                next_target_pos == current_target_pos + 1):
                current_shuffled_idx = next_shuffled_idx
                current_target_pos = next_target_pos
                j += 1
            else:
                break
        
        i = j
    
    return operations


# Read input
n = int(input())
input()  # Read "shuffled"

shuffled = []
for _ in range(n):
    shuffled.append(input())

input()  # Read "original"

original = []
for _ in range(n):
    original.append(input())

# Calculate and print result
result = find_min_operations(n, shuffled, original)
print(result)
