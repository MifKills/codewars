# My Solution
def height(n, m):
    # Solution from sum of Binomial coefficients (m k) with k from 1 to min(n,m)
    if n == 0 or m == 0:
        return 0
    else:
        result = 0
        const = 1  # Start coefficient (m 0) = 1
        for k in range(1, min(n, m) + 1):
            # (m k) binomial coefficient from (m k-1)
            const = const * (m-k+1)//k
            result += const
        return result


# Good Explaning of solution fron Baha2490
''' This code is way too easy compared to the process of finding it, so here is the explanation:

1) First we establish that h(n, m) = 1 + h(n, m-1) + h(n-1, m-1) by reasoning on the outcomes of an egg drop at a given floor f:
   - if it breaks, we have n-1 eggs and m-1 tries left, and we know the target floor is at most f-1, so to be guaranteed to find
     the target floor, f-1 <= h(n-1, m-1).
   - otherwise, we have n eggs and m-1 tries left, and we know the target floor is at least f+1, so to be guaranteed to find the
     target floor, h(n, m) - f <= h(n, m-1)
   This allows us to implement a naive dynamic programming approach, or a square and multiply approach with the corresponding
   matrix (good for small n and big m), but both are unfortunately too costly to pass the tests.
   
2) Then comes the hard part (at least for me, maybe there's a simpler way): realizing that h(n, m) is actually the sum of
   Pascal's triangle m first rows truncated at n first elements (a.k.a. n first columns truncated at row m).
   One way to see that is to start recursively expanding h(n,m): (abbreviated notation hij = h(n-i, m-j))
   
   h00 = 1[00] + h01 + h11
       = 1[00] + (1[01] + h02 + h12) + (1[11] + h12 + h22)
       = 1[00] + 1[01] + 1[11] + h02 + 2*h12 + h22
       = 1[00] + 1[01] + 1[11] + (1[02] + h03 + h13) + 2*(1[12] + h13 + h23) + (1[22] + h23 + h33)
       = 1[00] + 1[01] + 1[11] + 1[02] + 2[12] + 1[22] + h03 + 3*h13 + 3*h23 + h33
       = 1[00] +
         1[01] + 1[11] +
         1[02] + 2[12] + 1[22] +
         1[03] + 3[13] + 3[23] + 1[33] + ...
   
3) Finally, we can use the fact that the sum of a column k of Pascal's triangle (k,k) + (k+1,k) + ... + (m,k) is equal to
   (m+1,k+1), so we only need to compute the sum of the 2nd to n+1st element of row m+1.
'''
