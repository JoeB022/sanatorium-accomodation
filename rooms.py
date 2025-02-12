def solution(A):
    A.sort()  # Sort guest preferences in ascending order
    rooms = 0
    i = 0
    
    while i < len(A):
        rooms += 1
        capacity = A[i]
        count = 0
        
        while i < len(A) and count < capacity:
            count += 1
            i += 1
    
    return rooms

# Test cases
print(solution([1, 1, 1, 1, 1]))
print(solution([2, 1, 4]))
print(solution([2, 7, 2, 9, 8]))
print(solution([7, 3, 1, 1, 4, 5, 4, 9]))
