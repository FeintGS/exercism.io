def solve_knapsack(max_weight, items):
    # Declare our own locally named variables, to ease computations
    # by improving readability and brevity
    MAX_W = max_weight
    W = [int(item['weight']) for item in items]
    V = [int(item['value'])  for item in items]
    N = len(items)

    # Construct a zero-initialized array grid, responsible for remembering
    # old subproblems which we already computed the solution to
    #
    # X-axis = going right, increasingly higher maximum weight
    # Y-axis = going down, the Nth item
    memo = []
    for y in range(0, N+1):
        new_list = list()
        for x in range(0, MAX_W+1):
            new_list.append(0)
        memo.append(new_list)

    # Let's start solving for the local maximum for the
    # subproblems, which will build up to our global max
    #
    # n=the nth item, w=the max subweight
    #
    # The trivial base cases are when our knapsack can
    # carry a max weight of 0 units (-> therefore a max
    # value of 0), and we have 0 items to choose from
    # (-> likewise, a max value of 0)
    for n in range(1, N+1):
        for w in range(1, MAX_W+1):
            if n==0 or w==0:
                memo[n][w] = 0

            wi = W[n-1]
            vi = V[n-1]
            if wi <= w:
                memo[n][w] = max(vi + memo[n-1][w-wi], memo[n-1][w])
            else:
                memo[n][w] = memo[n-1][w]

    # The last grid element contains our final computation,
    # i.e. the solution
    return memo[N][MAX_W]

