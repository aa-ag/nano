# Solution
'''Helper Function - Find the max crossing sum w.r.t. middle index'''


def maxCrossingSum(arr, start, mid,  stop):
    '''LEFT PHASE - Traverse the Left part 
    starting from mid element'''
    # Denotes the sum of left part from mid element
    # to the current element
    leftSum = arr[mid]
    # Keep track of maximum sum
    leftMaxSum = arr[mid]

    # Traverse in reverse direction from (mid-1) to start
    # The second argument of range is not inclusive.
    # Third argument is the step size.
    for i in range(mid-1, start-1, -1):
        leftSum = leftSum + arr[i]
        # Update leftMaxSum
        if (leftSum > leftMaxSum):
            leftMaxSum = leftSum

    '''RIGHT PHASE - Traverse the Right part, 
    starting from (mid+1)'''
    # Denotes the sum of right part from (mid+1)
    # element to the current element
    rightSum = arr[mid + 1]
    # Keep track of maximum sum
    rightMaxSum = arr[mid+1]

    # Traverse in forward direction from (mid+2) to stop
    # The second argument of range is not inclusive
    for j in range(mid+2, stop+1):
        rightSum = rightSum + arr[j]
        # Update rightMaxSum
        if (rightSum > rightMaxSum):
            rightMaxSum = rightSum

    '''Both rightMaxSum and lefttMaxSum each would 
    contain value of atleast one element from the arr'''
    return (rightMaxSum + leftMaxSum)


'''Recursive function'''


# start and stop are the indices
def maxSubArrayRecursive(arr, start, stop):
    # Base case
    if (start == stop):
        return arr[start]

    if(start < stop):
        # Get the middle index
        mid = (start+stop)//2
        # Recurse on the Left part
        L = maxSubArrayRecursive(arr, start, mid)
        # Recurse on the Right part
        R = maxSubArrayRecursive(arr, mid+1, stop)
        # Find the max crossing sum w.r.t. middle index
        C = maxCrossingSum(arr, start, mid, stop)
        # Return the maximum of (L,R,C)
        return max(C, max(L, R))

    # If ever start > stop. Not feasible.
    else:
        return arr[start]


def maxSubArray(arr):
    start = 0  # staring index of original array
    stop = len(arr) - 1  # ending index of original array
    return maxSubArrayRecursive(arr, start, stop)


# Test 1
arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ", maxSubArray(arr))
# Outputs 13

# Test 2
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))
# Outputs 6

# Test 3
arr = [-4, 14, -6, 7]
print("Maximum Sum = ", maxSubArray(arr))
# Outputs 15

# Test 4
arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))
# Outputs 10

# Test 5
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ", maxSubArray(arr))
# Outputs 7
