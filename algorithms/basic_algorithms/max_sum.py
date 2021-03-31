'''
maxSubArrayRecursive(arr, start, stop)     T(n)
  1. if (start==stop):
      return arr[start]

  2. Calculate mid index       constant

  3. L = maxSubArrayRecursive(arr, start, mid)       T( 𝑛2 )

  4. R = maxSubArrayRecursive(arr, mid+1, stop)       T( 𝑛2 )

  5. C = maxCrossingSum(arr, start, mid, stop)         Θ(𝑛) 

  6. return max(C, max(L,R))       constant


Total time of execution  𝑇(𝑛)  =  2∗𝑇(𝑛2)+Θ(𝑛)≡𝑂(𝑛𝑙𝑜𝑔𝑛)
'''


# Test your code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))     # Outputs 6


# Test your code
arr = [-4, 14, -6, 7]
print("Maximum Sum = ", maxSubArray(arr))     # Outputs 15


# Test your code
arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))     # Outputs 10


# Test your code
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ", maxSubArray(arr))     # Outputs 7
