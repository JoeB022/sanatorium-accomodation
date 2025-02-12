# Minimum Rooms for Sanatorium

## Description
This program calculates the minimum number of rooms needed to accommodate guests in a sanatorium according to their preferences. Each guest has a preference indicating the maximum number of people they can share a room with, including themselves.

## Approach
1. **Sort the Preferences**: The guests' preferences are sorted in ascending order to efficiently group them.
2. **Greedy Room Allocation**: Iterate through the sorted list and allocate guests to rooms while respecting their constraints.
3. **Open New Rooms When Necessary**: If a guest cannot be accommodated in an existing room, a new room is opened.

## Function Definition
```python
def solution(A):
    A.sort()  # Sort guest preferences in ascending order
    rooms = 0
    i = 0  # Pointer to track guests
    
    while i < len(A):
        rooms += 1  # Open a new room
        capacity = A[i]  # Maximum number of guests allowed in this room
        count = 0  # Number of guests accommodated in the current room
        
        while i < len(A) and count < capacity:
            count += 1  # Add guest to the current room
            i += 1  # Move to the next guest
    
    return rooms
```

## Example Usage
```python
print(solution([1, 1, 1, 1, 1]))  # Output: 5
print(solution([2, 1, 4]))  # Output: 2
print(solution([2, 7, 2, 9, 8]))  # Output: 2
print(solution([7, 3, 1, 1, 4, 5, 4, 9]))  # Output: 4
```

## Complexity Analysis
- **Sorting**: \(O(N \log N)\)
- **Processing Guests**: \(O(N)\)
- **Overall Complexity**: \(O(N \log N)\), making it efficient for large inputs.

## Assumptions
- The number of guests \(N\) is between `1` and `100,000`.
- Each preference value in `A` is between `1` and `100,000`.

## Constraints
- The solution does not use additional space apart from sorting overhead.
- Ensures correctness while maintaining efficiency.

# sanatorium-accomodation
