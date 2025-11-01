# Order It - Recipe Instructions Reordering

## Problem Summary
Given a shuffled list of recipe instructions and the original order, find the minimum number of cut-and-insert operations needed to restore the original sequence. Each operation cuts a contiguous segment and inserts it elsewhere (cost = 1).

## Solution Approach

### Key Insights

1. **Longest Increasing Subsequence (LIS)**: Elements that don't need to move form the LIS when mapped to their target positions in the original list.

2. **Contiguity Requirement**: Elements can only be moved together in a single operation if they are:
   - Contiguous in the shuffled list, AND
   - Contiguous in their target positions in the original list

3. **Minimum Operations**: Count the number of groups of elements (not in LIS) that satisfy the contiguity requirement.

### Algorithm Steps

1. **Map to Target Positions**: Create a mapping of each instruction to its position in the original list, then map the shuffled list to target positions.

2. **Find LIS**: Use dynamic programming with parent tracking to find the Longest Increasing Subsequence. Elements in the LIS are already in correct relative order and don't need to move.

3. **Group Elements to Move**: For elements NOT in the LIS:
   - Sort them by target position
   - Group consecutive elements that are also consecutive in the shuffled list
   - Each group requires one cut-and-insert operation

4. **Count Operations**: Return the number of groups.

### Example Walkthrough

**Example 1:**
```
Shuffled: [Whisk(1), Bake(2), Season(4), Fold flour(0), Fold lettuce(3)]
Original: [Fold flour(0), Whisk(1), Bake(2), Fold lettuce(3), Season(4)]
Target positions: [1, 2, 4, 0, 3]
```

- **LIS**: [1, 2, 4] at indices [0, 1, 2] (length 3)
- **Elements to move**: 
  - Index 3 → target 0
  - Index 4 → target 3
- **Analysis**: 
  - Sorted by target: [(3→0), (4→3)]
  - Target positions 0 and 3 are NOT contiguous
  - Shuffled indices 3 and 4 ARE contiguous, but targets aren't
  - Result: 2 separate operations needed
- **Answer**: 2 ✓

**Example 2:**
```
Shuffled: [Dice onion(3), Dice rice(4), Pour(0), Stir(1), Fold(2), Serve(5)]
Original: [Pour(0), Stir(1), Fold(2), Dice onion(3), Dice rice(4), Serve(5)]
Target positions: [3, 4, 0, 1, 2, 5]
```

- **LIS**: [0, 1, 2, 5] at indices [2, 3, 4, 5] (length 4)
- **Elements to move**:
  - Index 0 → target 3
  - Index 1 → target 4
- **Analysis**:
  - Sorted by target: [(0→3), (1→4)]
  - Target positions 3 and 4 ARE contiguous
  - Shuffled indices 0 and 1 ARE contiguous
  - Result: Can be moved together in 1 operation
- **Answer**: 1 ✓

### Complexity
- **Time**: O(n²) for LIS computation + O(n log n) for sorting = O(n²)
- **Space**: O(n) for DP array, parent tracking, and mappings

### Usage
```bash
python3 solution.py < input.txt
```

## Test Cases

- **test_input1.txt**: Example 1 from problem (expected: 2)
- **test_input2.txt**: Example 2 from problem (expected: 1)
- **test_input3.txt**: Already sorted list (expected: 0)
- **test_input4.txt**: Reverse order list (expected: 2)

## Files
- `solution.py`: Main solution implementing the algorithm
- `test_input*.txt`: Test cases
- `README.md`: This file
