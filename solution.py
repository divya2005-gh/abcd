from collections import deque

def find_min_operations(n, shuffled, original):
    # edge case: already in order
    if shuffled == original:
        return 0
    
    # BFS to find shortest path
    initial = tuple(shuffled)
    goal = tuple(original)
    
    queue = deque([(initial, 0)])
    visited = {initial}
    
    while queue:
        state, ops = queue.popleft()
        
        # try all possible cut and insert operations
        current = list(state)
        
        # choose segment to cut [i, j]
        for i in range(n):
            for j in range(i, n):
                # cut out the segment
                cut_segment = current[i:j+1]
                rest = current[:i] + current[j+1:]
                
                # try inserting at each position
                for insert_at in range(len(rest) + 1):
                    # build new configuration
                    new_config = rest[:insert_at] + cut_segment + rest[insert_at:]
                    new_state = tuple(new_config)
                    
                    # found solution?
                    if new_state == goal:
                        return ops + 1
                    
                    # explore if not seen before
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, ops + 1))
    
    return -1  # shouldn't happen


n = int(input())
input()  # read "shuffled"

shuffled_instructions = []
for _ in range(n):
    shuffled_instructions.append(input())

input()  # read "original"

original_instructions = []
for _ in range(n):
    original_instructions.append(input())

result = find_min_operations(n, shuffled_instructions, original_instructions)
print(result)
